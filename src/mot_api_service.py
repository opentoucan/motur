from hishel import AsyncCacheTransport
import httpx
import msal
from config import VehicleSettings
from datetime import date, datetime
from pydantic import BaseModel, Field

class MotTestDefect(BaseModel):
    text: str | None = Field(alias="text", default=None)
    type: str | None = Field(alias="type", default=None)
    dangerous: bool | None = Field(alias="dangerous", default=None)

class MotTest(BaseModel):
    completed_date: datetime | None = Field(alias="completedDate", default=None)
    test_result: str | None = Field(alias="testResult", default=None)
    odometer_read_result: str | None = Field(alias="odometerResultType", default=None)
    datasource: str | None = Field(alias="dataSource", default=None)
    registration_at_time_of_test: str | None = Field(alias="registrationAtTimeOfTest", default=None)
    expiry_date: str | None = Field(alias="expiryDate", default=None)
    odometer_value: str | None = Field(alias="odometerValue", default=None)
    odometer_unit: str | None = Field(alias="odometerUnit", default=None)
    mot_test_number: str | None = Field(alias="motTestNumber", default=None)
    defects: list[MotTestDefect] = Field(alias="defects", default=[])

class MotSummaryInformation(BaseModel):
    registration_plate: str | None = Field(alias="registration", default=None)
    make: str | None = Field(alias="make", default=None)
    model: str | None = Field(alias="model", default=None)
    fuel_type: str | None = Field(alias="fuelType", default=None)
    colour: str | None = Field(alias="primaryColour", default=None)
    engine_size: str | None = Field(alias="engineSize", default=None)
    registation_date: date | None = Field(alias="registrationDate", default=None)
    manufacture_date: date | None = Field(alias="manufactureDate", default=None)
    first_mot_test_due_date: date | None = Field(alias="motTestDueDate", default=None)
    mot_tests: list[MotTest] = Field(alias="motTests", default=[])

class MotErrorResponse(BaseModel):
    error_code: str | None = Field(alias="errorCode")
    error_message: str | None = Field(alias="errorMessage")
    request_id: str | None = Field(alias="requestId")

class MotApiService:
    http_transport: AsyncCacheTransport
    vehicle_settings: VehicleSettings

    def __init__(self, http_transport, vehicle_settings):
        self.http_transport = http_transport
        self.vehicle_settings = vehicle_settings

    async def fetch_mot_history(self, reg: str) -> MotSummaryInformation | MotErrorResponse:
        client_id = self.vehicle_settings.mot_client_id
        tenant_id = self.vehicle_settings.mot_tenant_id
        client_secret = self.vehicle_settings.mot_client_secret
        mot_api_key = self.vehicle_settings.mot_api_key

        msal_client = msal.ConfidentialClientApplication(client_id, authority=f"https://login.microsoftonline.com/{tenant_id}", client_credential=client_secret)
        result = msal_client.acquire_token_for_client(scopes=["https://tapi.dvsa.gov.uk/.default"])
        if type(result) is not dict or 'access_token' not in result:
            return MotErrorResponse(errorCode="403", errorMessage="Unable to authenticate with the MOT API", requestId=None)

        async with httpx.AsyncClient(transport=self.http_transport) as client:
            headers = {'accept': 'application/json','Authorization': f'{result['token_type']} {result['access_token']}','X-API-Key': f'{mot_api_key}'}
            response = await client.get(f'https://history.mot.api.gov.uk/v1/trade/vehicles/registration/{reg}', headers=headers)
            if response.status_code == 200:
                return MotSummaryInformation.model_validate_json(response.content)
            else:
                return MotErrorResponse.model_validate_json(response.content)

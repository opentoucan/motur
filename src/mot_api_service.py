import msal
from config import vehicle_settings
from datetime import date, datetime
from pydantic import BaseModel, Field
from generated.mot_client import Client as MotClient
from generated.mot_client.models.new_reg_vehicle_response import NewRegVehicleResponse
from generated.mot_client.models.vehicle_with_mot_response import VehicleWithMotResponse
from generated.mot_client.api.mot_history_api import get_v1_trade_vehicles_registration_registration
from generated.mot_client.models.error_response import ErrorResponse

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
    error_message: str = Field(alias="errorMessage")

MotApiResponseType = ErrorResponse | NewRegVehicleResponse | VehicleWithMotResponse | None
MotInformationResponseType = MotSummaryInformation | MotErrorResponse | None

async def MapToMotSummaryInformation(vehicle_mot_response: MotApiResponseType) -> MotInformationResponseType:
        if type(vehicle_mot_response) is ErrorResponse:
            return MotErrorResponse.model_validate(vehicle_mot_response.to_dict())
        elif vehicle_mot_response is not None:
            return MotSummaryInformation.model_validate(vehicle_mot_response.to_dict())

async def fetch_mot_history(reg: str) -> MotInformationResponseType:
    client_id = vehicle_settings.mot_client_id
    tenant_id = vehicle_settings.mot_tenant_id
    client_secret = vehicle_settings.mot_client_secret
    mot_api_key = vehicle_settings.mot_api_key

    msal_client = msal.ConfidentialClientApplication(client_id, authority=f"https://login.microsoftonline.com/{tenant_id}", client_credential=client_secret)
    result = msal_client.acquire_token_for_client(scopes=["https://tapi.dvsa.gov.uk/.default"])
    if type(result) is not dict or 'access_token' not in result:
        return MotErrorResponse(errorMessage="Unable to authenticate with the MOT API")
    headers = {'accept': 'application/json','Authorization': f'{result['token_type']} {result['access_token']}','X-API-Key': f'{mot_api_key}'}
    mot_client = MotClient(base_url="https://history.mot.api.gov.uk", headers=headers)
    async with mot_client:
        vehicle_mot_response: MotApiResponseType = await get_v1_trade_vehicles_registration_registration.asyncio(client=mot_client, registration=reg)
        return await MapToMotSummaryInformation(vehicle_mot_response)

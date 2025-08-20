import msal
from config import vehicle_settings
from datetime import date, datetime
from pydantic import BaseModel
from generated.mot_client import Client as MotClient
from generated.mot_client.models.new_reg_vehicle_response import NewRegVehicleResponse
from generated.mot_client.models.vehicle_with_mot_response import VehicleWithMotResponse
from generated.mot_client.api.mot_history_api import get_v1_trade_vehicles_registration_registration
from generated.mot_client.models.cvs_mot_test import CVSMotTest
from generated.mot_client.models.defect import Defect
from generated.mot_client.models.dvsa_mot_test import DVSAMotTest
from generated.mot_client.models.error_response import ErrorResponse
from generated.mot_client.models.new_reg_vehicle_response import NewRegVehicleResponse
from generated.mot_client.models.vehicle_with_mot_response import VehicleWithMotResponse
from generated.mot_client.types import Unset

class MotTestDefect(BaseModel):
    text: str | None
    type: str | None
    dangerous: bool | None

class MotTest(BaseModel):
    completed_date: datetime | None
    test_result: str | None
    odometer_read_result: str | None
    datasource: str | None
    registration_at_time_of_test: str | None
    odometer_value: str | None
    odometer_unit: str | None
    mot_test_number: str | None

class MotSummaryInformation(BaseModel):
    registration_plate: str | None
    make: str | None
    model: str | None
    fuel_type: str | None
    colour: str | None
    engine_size: str | None
    registation_date: date | None
    manufacture_date: date | None
    mot_test_due_date: date | None
    mot_tests: list[MotTest]

class MotErrorResponse(BaseModel):
    error_message: str

async def MapToMotSummaryInformation(vehicle_mot_response: ErrorResponse | NewRegVehicleResponse | VehicleWithMotResponse | None) -> MotSummaryInformation | MotErrorResponse | None:
        if type(vehicle_mot_response) is ErrorResponse:
            return MotErrorResponse(error_message=vehicle_mot_response.error_message if type(vehicle_mot_response.error_message) is str else "")
        elif type(vehicle_mot_response) is NewRegVehicleResponse:
            return MotSummaryInformation(
                registration_plate=vehicle_mot_response.registration if type(vehicle_mot_response.registration) is str else None,
                make=vehicle_mot_response.make if type(vehicle_mot_response.make) is str else None,
                model=vehicle_mot_response.model if type(vehicle_mot_response.model) is str else None,
                fuel_type=vehicle_mot_response.fuel_type if type(vehicle_mot_response.fuel_type) is str else None,
                colour=vehicle_mot_response.primary_colour if type(vehicle_mot_response.primary_colour) is str else None,
                engine_size=None,
                registation_date=vehicle_mot_response.registration_date if type(vehicle_mot_response.registration_date) is date else None,
                manufacture_date=vehicle_mot_response.manufacture_date if type(vehicle_mot_response.manufacture_date) is date else None,
                mot_test_due_date=vehicle_mot_response.mot_test_due_date if type(vehicle_mot_response.mot_test_due_date) is date else None,
                mot_tests=[])
        elif type(vehicle_mot_response) is VehicleWithMotResponse:
            mot_tests: list[MotTest] = []
            for mot_test_response in vehicle_mot_response.mot_tests:
              mot_test_defects: list[MotTestDefect] = []
              if (type (mot_test_response) is DVSAMotTest or type(mot_test_response) is CVSMotTest) and type(mot_test_response.defects) is list[Defect]:
                  for defect in mot_test_response.defects:
                      mot_test_defects.append(MotTestDefect(text=defect.text, type=defect.type_, dangerous=defect.dangerous)) # type: ignore
              mot_test = MotTest(
                  completed_date=mot_test_response.completed_date,
                  test_result=mot_test_response.test_result,
                  odometer_read_result=mot_test_response.odometer_result_type,
                  odometer_value=mot_test_response.odometer_value if type(mot_test_response.odometer_value) is str else None,
                  odometer_unit=mot_test_response.odometer_unit if type(mot_test_response.odometer_unit) is not Unset else None, # type: ignore
                  mot_test_number=mot_test_response.mot_test_number if type(mot_test_response.mot_test_number) is str else None,
                  registration_at_time_of_test=mot_test_response.registration_at_time_of_test if type(mot_test_response.registration_at_time_of_test) is str else None,
                  datasource=mot_test_response.data_source)
              mot_tests.append(mot_test)

            return MotSummaryInformation(
                registration_plate=vehicle_mot_response.registration if type(vehicle_mot_response.registration) is str else None,
                make=vehicle_mot_response.make if type(vehicle_mot_response.make) is str else None,
                model=vehicle_mot_response.model if type(vehicle_mot_response.model) is str else None,
                fuel_type=vehicle_mot_response.fuel_type if type(vehicle_mot_response.fuel_type) is str else None,
                colour=vehicle_mot_response.primary_colour if type(vehicle_mot_response.primary_colour) is str else None,
                engine_size=vehicle_mot_response.engine_size if type(vehicle_mot_response.engine_size) is str else None,
                registation_date=vehicle_mot_response.registration_date if type(vehicle_mot_response.registration_date) is date else None,
                manufacture_date=vehicle_mot_response.manufacture_date if type(vehicle_mot_response.manufacture_date) is date else None,
                mot_test_due_date=None,
                mot_tests=mot_tests)

async def fetch_mot_history(reg: str) -> MotSummaryInformation | MotErrorResponse | None:
    client_id = vehicle_settings.mot_client_id
    tenant_id = vehicle_settings.mot_tenant_id
    client_secret = vehicle_settings.mot_client_secret
    mot_api_key = vehicle_settings.mot_api_key

    msal_client = msal.ConfidentialClientApplication(client_id, authority=f"https://login.microsoftonline.com/{tenant_id}", client_credential=client_secret)
    result = msal_client.acquire_token_for_client(scopes=["https://tapi.dvsa.gov.uk/.default"])
    if type(result) is not dict:
        return MotErrorResponse(error_message="Unable to authenticate with the MOT API") # type: ignore
    headers = {'accept': 'application/json','Authorization': f'{result['token_type']} {result['access_token']}','X-API-Key': f'{mot_api_key}'}
    mot_client = MotClient(base_url="https://history.mot.api.gov.uk", headers=headers)
    async with mot_client:
        vehicle_mot_response: ErrorResponse | NewRegVehicleResponse | VehicleWithMotResponse | None = await get_v1_trade_vehicles_registration_registration.asyncio(client=mot_client, registration=reg)
        return await MapToMotSummaryInformation(vehicle_mot_response)

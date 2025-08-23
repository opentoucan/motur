from pydantic import BaseModel
from error_details import ErrorDetails
from ves_api_service import VesApiService, VehicleRegistrationDetails
from mot_api_service import MotApiService, VehicleMotDetails


class RegistrationResponse(BaseModel):
   details: VehicleRegistrationDetails | None
   error_details: ErrorDetails | None

class MotResponse(BaseModel):
   details: VehicleMotDetails | None
   error_details: ErrorDetails | None

class RegistrationAndMotResponse(BaseModel):
    registration_response: RegistrationResponse | None
    mot_response: MotResponse | None

class VehicleService:
  mot_api_service: MotApiService
  ves_api_service: VesApiService

  def __init__(self, mot_api_service: MotApiService, ves_api_service: VesApiService):
    self.mot_api_service = mot_api_service
    self.ves_api_service = ves_api_service

  async def fetch_vehicle_information(self, registration_plate: str) -> RegistrationAndMotResponse:

    normalised_reg = bytes(registration_plate, 'utf-8').decode('utf-8', 'ignore').replace(" ", "").upper()
    ves_api_response = await self.ves_api_service.fetch_vehicle_info(normalised_reg)
    mot_api_response = await self.mot_api_service.fetch_mot_history(reg=normalised_reg)

    ves_details : VehicleRegistrationDetails | None = ves_api_response if type(ves_api_response) is VehicleRegistrationDetails else None
    ves_error_details : ErrorDetails | None = ves_api_response if type(ves_api_response) is ErrorDetails else None
    mot_details : VehicleMotDetails | None = mot_api_response if type(mot_api_response) is VehicleMotDetails else None
    mot_error_details : ErrorDetails | None = mot_api_response if type(mot_api_response) is ErrorDetails else None
    return RegistrationAndMotResponse(registration_response=RegistrationResponse(details=ves_details, error_details=ves_error_details), mot_response=MotResponse(details=mot_details, error_details=mot_error_details))

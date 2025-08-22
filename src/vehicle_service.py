from pydantic import BaseModel
from ves_api_service import VesApiService, VehicleInformation, VehicleErrorResponse
from mot_api_service import MotApiService, MotErrorResponse, MotSummaryInformation

class VehicleAndMotInformation(BaseModel):
    mot_information: MotSummaryInformation | MotErrorResponse | None
    vehicle_information: VehicleInformation | VehicleErrorResponse | None

class VehicleService:
  mot_api_service: MotApiService
  ves_api_service: VesApiService

  def __init__(self, mot_api_service: MotApiService, ves_api_service: VesApiService):
    self.mot_api_service = mot_api_service
    self.ves_api_service = ves_api_service

  async def fetch_vehicle_information(self, registration_plate: str) -> VehicleAndMotInformation:

    vehicle_information = await self.ves_api_service.fetch_vehicle_info(registration_plate)
    mot_summary = await self.mot_api_service.fetch_mot_history(reg=registration_plate)
    vehicle_and_mot_information = VehicleAndMotInformation.model_validate({"mot_information" : mot_summary, "vehicle_information": vehicle_information})
    return vehicle_and_mot_information

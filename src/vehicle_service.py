from pydantic import BaseModel
from mot_api_service import MotErrorResponse, MotSummaryInformation
from ves_api_service import VehicleInformation, VehicleErrorResponse
import mot_api_service
import ves_api_service

class VehicleAndMotInformation(BaseModel):
    mot_information: MotSummaryInformation | MotErrorResponse | None
    vehicle_information: VehicleInformation | VehicleErrorResponse | None

async def fetch_vehicle_information(registration_plate: str) -> VehicleAndMotInformation:
  vehicle_information = await ves_api_service.fetch_vehicle_info(registration_plate)
  mot_summary = await mot_api_service.fetch_mot_history(registration_plate)
  return VehicleAndMotInformation(mot_information=mot_summary, vehicle_information=vehicle_information)

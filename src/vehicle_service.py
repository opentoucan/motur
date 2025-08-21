from pydantic import BaseModel
from mot_api_service import MotErrorResponse, MotSummaryInformation
from ves_api_service import VehicleInformation, VehicleErrorResponse
from generated.ves_client import Client as VesClient
import mot_api_service
import ves_api_service

class VehicleAndMotInformation(BaseModel):
    mot_information: MotSummaryInformation | MotErrorResponse | None
    vehicle_information: VehicleInformation | VehicleErrorResponse | None

async def fetch_vehicle_information(registration_plate: str) -> VehicleAndMotInformation:
  headers = {'accept': 'application/json'}
  ves_client = VesClient(base_url="https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry", headers=headers)
  vehicle_information = await ves_api_service.fetch_vehicle_info(ves_client, registration_plate)
  mot_summary = await mot_api_service.fetch_mot_history(registration_plate)
  vehicle_and_mot_information = VehicleAndMotInformation.model_validate({"mot_information" : mot_summary, "vehicle_information": vehicle_information})
  return vehicle_and_mot_information

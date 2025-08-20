from config import vehicle_settings
from datetime import date
from pydantic import BaseModel
from generated.ves_client import Client as VesClient
from generated.ves_client.api.vehicle import get_vehicle_details_by_registration_number
from generated.ves_client.models.vehicle import Vehicle
from generated.ves_client.models.vehicle_mot_status import VehicleMotStatus
from generated.ves_client.models.vehicle_request import VehicleRequest
from generated.ves_client.models.error_response import ErrorResponse
from generated.ves_client.models.errors import Errors
from generated.ves_client.models.vehicle_tax_status import VehicleTaxStatus

class VehicleInformation(BaseModel):
    registration_plate: str
    tax_status: str | None
    tax_due_date: date | None
    additional_tax_rate_end_date: date | None
    mot_status: str | None
    mot_expiry_date: date | None
    make: str | None
    month_of_first_registration: date | None
    year_of_manufacture: int | None
    engine_capacity_in_cc: int | None
    co2_emissions_in_gram_per_km: int | None
    fuel_type: str | None
    colour: str | None
    approval_category: str | None
    wheelplan: str | None
    revenue_weight_in_kg: int | None
    real_driving_emissions: str | None
    date_of_last_v5c_issued: date | None
    euro_status: str | None
    automated_vehicle: bool | None

class VehicleErrorResponse(BaseModel):
    error_message: str


async def MapToVehicleInformation(ves_response: ErrorResponse | Vehicle | None) -> VehicleInformation | VehicleErrorResponse | None:
        if type(ves_response) is ErrorResponse:
            error_message = ''.join(str(x.detail) for x in ves_response.errors) # type: ignore
            return VehicleErrorResponse(error_message=error_message)
        elif type(ves_response) is Vehicle:
            return VehicleInformation(
                registration_plate=ves_response.registration_number,
                tax_status=ves_response.tax_status if type(ves_response.tax_status) is VehicleTaxStatus else None,
                tax_due_date=ves_response.tax_due_date if type(ves_response.tax_due_date) is date else None,
                additional_tax_rate_end_date=ves_response.art_end_date if type(ves_response.art_end_date) is date else None,
                mot_status=ves_response.mot_status if type(ves_response.mot_status) is VehicleMotStatus else None,
                mot_expiry_date=ves_response.mot_expiry_date if type(ves_response.mot_expiry_date) is date else None,
                make=ves_response.make if type(ves_response.make) is str else None,
                month_of_first_registration=ves_response.month_of_first_registration if type(ves_response.month_of_first_registration) is date else None,
                year_of_manufacture=ves_response.year_of_manufacture if type(ves_response.year_of_manufacture) is int else None,
                engine_capacity_in_cc=ves_response.engine_capacity if type(ves_response.engine_capacity) is int else None,
                co2_emissions_in_gram_per_km=ves_response.co_2_emissions if type(ves_response.co_2_emissions) is int else None,
                fuel_type=ves_response.fuel_type if type(ves_response.fuel_type) is str else None,
                colour=ves_response.colour if type(ves_response.colour) is str else None,
                approval_category=ves_response.type_approval if type(ves_response.type_approval) is str else None,
                wheelplan=ves_response.wheelplan if type(ves_response.wheelplan) is str else None,
                revenue_weight_in_kg=ves_response.revenue_weight if type(ves_response.revenue_weight) is int else None,
                real_driving_emissions=ves_response.real_driving_emissions if type(ves_response.real_driving_emissions) is str else None,
                date_of_last_v5c_issued=ves_response.date_of_last_v5c_issued if type(ves_response.date_of_last_v5c_issued) is date else None,
                euro_status=ves_response.euro_status if type(ves_response.euro_status) is str else None,
                automated_vehicle=ves_response.automated_vehicle if type(ves_response.automated_vehicle) is bool else None)

async def fetch_vehicle_info(reg: str) -> VehicleInformation | VehicleErrorResponse | None:
  headers = {'accept': 'application/json'}
  ves_client = VesClient(base_url="https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry", headers=headers)
  async with ves_client:
      ves_response: ErrorResponse | Vehicle | None = await get_vehicle_details_by_registration_number.asyncio(client=ves_client, x_api_key=vehicle_settings.ves_api_key, body=VehicleRequest(registration_number=reg))
      return await MapToVehicleInformation(ves_response)

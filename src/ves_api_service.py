from config import vehicle_settings
from datetime import date
from pydantic import BaseModel, Field
from generated.ves_client import Client as VesClient
from generated.ves_client.api.vehicle import get_vehicle_details_by_registration_number
from generated.ves_client.models.vehicle import Vehicle
from generated.ves_client.models.vehicle_request import VehicleRequest
from generated.ves_client.models.error_response import ErrorResponse


class VehicleInformation(BaseModel):
    registration_plate: str = Field(alias="registrationNumber")
    tax_status: str | None = Field(alias="taxStatus", default=None)
    tax_due_date: date | None = Field(alias="taxDueDate", default=None)
    additional_tax_rate_end_date: date | None = Field(alias="artEndDate", default=None)
    mot_status: str | None = Field(alias="motStatus", default=None)
    mot_expiry_date: date | None = Field(alias="motExpiryDate", default=None)
    make: str | None = Field(alias="make", default=None)
    month_of_first_registration: date | None = Field(alias="monthOfFirstDvlaRegistration", default=None)
    year_of_manufacture: int | None = Field(alias="yearOfManufacture", default=None)
    engine_capacity_in_cc: int | None = Field(alias="engineCapacity", default=None)
    co2_emissions_in_gram_per_km: int | None = Field(alias="co2Emissions", default=None)
    fuel_type: str | None = Field(alias="fuelType", default=None)
    colour: str | None = Field(alias="colour", default=None)
    approval_category: str | None = Field(alias="typeApproval", default=None)
    wheelplan: str | None = Field(alias="wheelplan", default=None)
    revenue_weight_in_kg: int | None = Field(alias="revenueWeight", default=None)
    real_driving_emissions: str | None = Field(alias="realDrivingEmissions", default=None)
    date_of_last_v5c_issued: date | None = Field(alias="dateOfLastV5CIssued", default=None)
    euro_status: str | None = Field(alias="euroStatus", default=None)
    automated_vehicle: bool | None = Field(alias="automatedVehicle", default=None)

class VehicleErrorResponse(BaseModel):
    error_message: str

async def MapToVehicleInformation(ves_response: ErrorResponse | Vehicle | None) -> VehicleInformation | VehicleErrorResponse | None:
        if type(ves_response) is ErrorResponse:
            return VehicleErrorResponse(error_message=str(ves_response.to_dict()))
        elif type(ves_response) is Vehicle:
            return VehicleInformation.model_validate(ves_response.to_dict())

async def fetch_vehicle_info(reg: str) -> VehicleInformation | VehicleErrorResponse | None:
  headers = {'accept': 'application/json'}
  ves_client = VesClient(base_url="https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry", headers=headers)
  async with ves_client:
      ves_response: ErrorResponse | Vehicle | None = await get_vehicle_details_by_registration_number.asyncio(client=ves_client, x_api_key=vehicle_settings.ves_api_key, body=VehicleRequest(registration_number=reg))
      return await MapToVehicleInformation(ves_response)

from hishel import AsyncCacheTransport
import httpx
from config import Settings
from datetime import date
from pydantic import BaseModel, Field

from error_details import ErrorDetails

class VehicleRegistrationDetails(BaseModel):
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

class Error(BaseModel):
    status: str = Field(alias="status")
    code: str = Field(alias="code")
    title: str = Field(alias="title")
    detail: str = Field(alias="detail")

class VehicleErrorResponse(BaseModel):
    errors: list[Error] = Field(alias="errors")

class VesApiService:
    http_transport: AsyncCacheTransport
    settings: Settings

    def __init__(self, http_transport, settings):
        self.http_transport = http_transport
        self.settings = settings

    async def fetch_vehicle_info(self, reg: str) -> VehicleRegistrationDetails | ErrorDetails:
        async with httpx.AsyncClient(transport=self.http_transport) as client:
            headers = {'accept': 'application/json','x-api-key': f'{self.settings.ves_api.api_key}'}
            response = await client.post('https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles', headers=headers, json={'registrationNumber': reg})
            if response.status_code == 200:
                return VehicleRegistrationDetails.model_validate_json(response.content)
            else:
                error_response = VehicleErrorResponse.model_validate_json(response.content)
                error = error_response.errors[0]
                return ErrorDetails(internal_code=error.code, http_status_code=response.status_code, reason=error.detail)

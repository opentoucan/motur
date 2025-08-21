from unittest.mock import ANY
from generated.ves_client.models.error_response import ErrorResponse
from generated.ves_client.models.errors import Errors
from generated.ves_client.models.vehicle_request import VehicleRequest
import pytest
from generated.ves_client.models.vehicle import Vehicle
from generated.ves_client.models.vehicle_tax_status import VehicleTaxStatus
from ves_api_service import VehicleErrorResponse, VehicleInformation, fetch_vehicle_info

@pytest.mark.asyncio
async def test_fetch_vehicle_info_returns_vehicle_information(mocker):
  mock_response = Vehicle(
    registration_number="AA11 AAA",
    tax_status=VehicleTaxStatus.TAXED)
  mock_ves_client = mocker.patch("ves_api_service.get_vehicle_details_by_registration_number.asyncio", return_value=mock_response)

  result = await fetch_vehicle_info("AA11 AAA")

  assert result == VehicleInformation(
    registrationNumber=mock_response.registration_number,
    taxStatus=mock_response.tax_status # type: ignore
    )
  mock_ves_client.assert_called_once_with(client=ANY, x_api_key=ANY, body=VehicleRequest(registration_number=mock_response.registration_number))

@pytest.mark.asyncio
async def test_fetch_vehicle_info_returns_error(mocker):
  mock_response = ErrorResponse(errors=[Errors(title="title_error", status="400", code="105", detail="No registration found")])
  mock_ves_client = mocker.patch("ves_api_service.get_vehicle_details_by_registration_number.asyncio", return_value=mock_response)
  registration_plate = "AA11 AAA"

  result = await fetch_vehicle_info(registration_plate)

  assert result == VehicleErrorResponse(error_message=mock_response.errors[0].detail) # type: ignore
  mock_ves_client.assert_called_once_with(client=ANY, x_api_key=ANY, body=VehicleRequest(registration_number=registration_plate))

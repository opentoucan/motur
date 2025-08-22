from httpx import Response
import pytest
import hishel
from config import VehicleSettings
from ves_api_service import Error, VehicleErrorResponse, VehicleInformation, VesApiService

vehicle_settings = VehicleSettings(mot_client_id="blah", mot_tenant_id="blah", mot_api_key="blah", mot_client_secret="blah", ves_api_key="blah")
mock_http_transport = hishel.MockAsyncTransport()
ves_api_service: VesApiService = VesApiService(mock_http_transport, vehicle_settings)

@pytest.mark.asyncio
async def test_fetch_vehicle_info_returns_vehicle_information():
  registration_plate = "AA11 AAA"
  tax_status = "SORN"
  colour = "Red"
  response_json = VehicleInformation(registrationNumber=registration_plate, taxStatus=tax_status, colour=colour).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=200, content=response_json)])

  result = await ves_api_service.fetch_vehicle_info(registration_plate)

  assert result == VehicleInformation(
    registrationNumber=registration_plate,
    taxStatus=tax_status,
    colour=colour
  )

@pytest.mark.asyncio
async def test_fetch_vehicle_info_403_returns_error_response():
  error_status = "forbidden"
  error_code = "403"
  error_title="error title"
  error_detail="You are not allowed to access this resource"
  error_list: list[Error] = [Error(status=error_status, code=error_code, title=error_title, detail=error_detail)]
  response_json = VehicleErrorResponse(errors=error_list).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=403, content=response_json)])

  result = await ves_api_service.fetch_vehicle_info("AA11 AAA")

  assert result == VehicleErrorResponse(errors=[Error(status=error_status, code=error_code, title=error_title, detail=error_detail)])

from httpx import Response
from config import Settings
from error_details import ErrorDetails
import pytest
import hishel
from ves_api_service import Error, VehicleErrorResponse, VehicleRegistrationDetails, VesApiService

fake_settings = Settings(
  ves_api=Settings.VesApi(api_key="blah"),
  mot_api=Settings.MotApi(client_id="blah", tenant_id="blah", api_key="blah", client_secret="blah"),
  enabled_sites=[""],
  scraper=Settings.ScraperSettings(chrome_binary_location="dummy_path", disable_sandbox=False, image_path="dummy_path"))

mock_http_transport = hishel.MockAsyncTransport()
ves_api_service: VesApiService = VesApiService(mock_http_transport, fake_settings)

@pytest.mark.asyncio
async def test_fetch_vehicle_info_returns_vehicle_information():
  registration_plate = "AA11 AAA"
  tax_status = "SORN"
  colour = "Red"
  response_json = VehicleRegistrationDetails(registrationNumber=registration_plate, taxStatus=tax_status, colour=colour).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=200, content=response_json)])

  result = await ves_api_service.fetch_vehicle_info(registration_plate)

  assert result == VehicleRegistrationDetails(
    registrationNumber=registration_plate,
    taxStatus=tax_status,
    colour=colour
  )

@pytest.mark.asyncio
async def test_fetch_vehicle_info_403_returns_error_response():
  http_status_code = 403
  error_status = "forbidden"
  error_code = "403"
  error_title="error title"
  error_detail="You are not allowed to access this resource"
  error_list: list[Error] = [Error(status=error_status, code=error_code, title=error_title, detail=error_detail)]
  response_json = VehicleErrorResponse(errors=error_list).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=http_status_code, content=response_json)])

  result = await ves_api_service.fetch_vehicle_info("AA11 AAA")

  assert result == ErrorDetails(internal_code=error_code, http_status_code=http_status_code, reason=error_detail)

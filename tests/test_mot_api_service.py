from datetime import datetime
import hishel
from httpx import Response
from config import Settings
from error_details import ErrorDetails
from mot_api_service import MotApiService, VehicleMotDetails, VehicleMotDetailsErrorResponse, MotTest, Defect
import pytest

fake_settings = Settings(
  ves_api=Settings.VesApi(api_key="blah"),
  mot_api=Settings.MotApi(client_id="blah", tenant_id="blah", api_key="blah", client_secret="blah"),
  enabled_sites=[""],
  scraper=Settings.Scraper(chrome_binary_location="dummy_path", disable_sandbox=False, image_path="dummy_path"),
  redis=None)

mock_http_transport = hishel.MockAsyncTransport()
mot_api_service: MotApiService = MotApiService(mock_http_transport, fake_settings)

@pytest.mark.asyncio
async def test_fetch_vehicle_invalid_bearer_token_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  result = await mot_api_service.fetch_mot_history(registration_plate)
  assert result == ErrorDetails(internal_code=None, http_status_code=403, reason="Unable to authenticate with the MOT API")

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_old_vehicle_returns_mot_summary_information(mocker):
  registration_plate = "AA11 AAA"
  now = datetime.now()
  response_json = VehicleMotDetails(
    registration="AA11 AAA",
      make="ford",
      motTests=[MotTest(
        completedDate=now,
          testResult="PASSED",
            dataSource="DVSA",
            odometerResultType="READ",
              defects=[Defect(
                  text="Rover won't turn over",
                  type="MAJOR",
                  dangerous=False
              )])]).model_dump_json(by_alias=True)

  mock_http_transport.add_responses(responses=[Response(status_code=200, content=response_json)])
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})
  result = await mot_api_service.fetch_mot_history(registration_plate)
  assert result == VehicleMotDetails(
    registration=registration_plate,
    make="ford",
    motTests=[MotTest(completedDate=now, testResult="PASSED", dataSource="DVSA", odometerResultType="READ", defects=[Defect(text="Rover won't turn over", type="MAJOR", dangerous=False)])])

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_new_reg_vehicle_returns_mot_summary_information(mocker):
  registration_plate = "AA11 AAA"
  make = "ford"
  mot_due_date = datetime.now().date()
  response_json = VehicleMotDetails(
    registration=registration_plate,
    make=make,
    motTestDueDate=mot_due_date).model_dump_json(by_alias=True)

  mock_http_transport.add_responses(responses=[Response(status_code=200, content=response_json)])
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})

  result = await mot_api_service.fetch_mot_history(registration_plate)

  assert result == VehicleMotDetails(
    registration=registration_plate,
    make=make,
    motTestDueDate=mot_due_date,
    motTests=[])

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_no_matching_reg_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  error_code = "404"
  error_message = f"Vehicle not found with reg [{registration_plate}]"
  response_json = VehicleMotDetailsErrorResponse(errorCode=error_code, errorMessage=error_message, requestId=None).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=int(error_code), content=response_json)])
  mock_msal_client = mocker.Mock()

  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})

  result = await mot_api_service.fetch_mot_history(registration_plate)

  assert result == ErrorDetails(internal_code=error_code, http_status_code=int(error_code), reason=error_message)

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_invalid_api_key_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  error_code = "403"
  error_message = "Not allowed to access this resource"
  response_json = VehicleMotDetailsErrorResponse(errorCode=error_code, errorMessage=error_message, requestId=None).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=int(error_code), content=response_json)])
  mock_msal_client = mocker.Mock()

  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})

  result = await mot_api_service.fetch_mot_history(registration_plate)

  assert result == ErrorDetails(internal_code=error_code, http_status_code=int(error_code), reason=error_message)

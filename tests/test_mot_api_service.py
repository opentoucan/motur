from datetime import datetime
import hishel
from httpx import Response
from config import VehicleSettings
from mot_api_service import MotApiService, MotErrorResponse, MotSummaryInformation, MotTest, MotTestDefect
import pytest

vehicle_settings = VehicleSettings(mot_client_id="blah", mot_tenant_id="blah", mot_api_key="blah", mot_client_secret="blah", ves_api_key="blah")
mock_http_transport = hishel.MockAsyncTransport()
mot_api_service: MotApiService = MotApiService(mock_http_transport, vehicle_settings)

@pytest.mark.asyncio
async def test_fetch_vehicle_invalid_bearer_token_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  result = await mot_api_service.fetch_mot_history(registration_plate)
  assert result == MotErrorResponse(errorMessage="Unable to authenticate with the MOT API", errorCode="403", requestId=None)

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_old_vehicle_returns_mot_summary_information(mocker):
  registration_plate = "AA11 AAA"
  now = datetime.now()
  response_json = MotSummaryInformation(
    registration="AA11 AAA",
      make="ford",
      motTests=[MotTest(
        completedDate=now,
          testResult="PASSED",
            dataSource="DVSA",
            odometerResultType="READ",
              defects=[MotTestDefect(
                  text="Rover won't turn over",
                  type="MAJOR",
                  dangerous=False
              )])]).model_dump_json(by_alias=True)

  mock_http_transport.add_responses(responses=[Response(status_code=200, content=response_json)])
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})
  result = await mot_api_service.fetch_mot_history(registration_plate)
  assert result == MotSummaryInformation(
    registration=registration_plate,
    make="ford",
    motTests=[MotTest(completedDate=now, testResult="PASSED", dataSource="DVSA", odometerResultType="READ", defects=[MotTestDefect(text="Rover won't turn over", type="MAJOR", dangerous=False)])])

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_new_reg_vehicle_returns_mot_summary_information(mocker):
  registration_plate = "AA11 AAA"
  make = "ford"
  mot_due_date = datetime.now().date()
  response_json = MotSummaryInformation(
    registration=registration_plate,
    make=make,
    motTestDueDate=mot_due_date).model_dump_json(by_alias=True)

  mock_http_transport.add_responses(responses=[Response(status_code=200, content=response_json)])
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})

  result = await mot_api_service.fetch_mot_history(registration_plate)

  assert result == MotSummaryInformation(
    registration=registration_plate,
    make=make,
    motTestDueDate=mot_due_date,
    motTests=[])

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_no_matching_reg_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  error_code = "404"
  error_message = f"Vehicle not found with reg [{registration_plate}]"
  response_json = MotErrorResponse(errorCode=error_code, errorMessage=error_message, requestId=None).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=int(error_code), content=response_json)])
  mock_msal_client = mocker.Mock()

  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})

  result = await mot_api_service.fetch_mot_history(registration_plate)

  assert result == MotErrorResponse(errorCode=error_code, errorMessage=error_message, requestId=None)

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_invalid_api_key_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  error_code = "403"
  error_message = "Not allowed to access this resource"
  response_json = MotErrorResponse(errorCode=error_code, errorMessage=error_message, requestId=None).model_dump_json(by_alias=True)
  mock_http_transport.add_responses(responses=[Response(status_code=int(error_code), content=response_json)])
  mock_msal_client = mocker.Mock()

  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})

  result = await mot_api_service.fetch_mot_history(registration_plate)

  assert result == MotErrorResponse(errorCode=error_code, errorMessage=error_message, requestId=None)

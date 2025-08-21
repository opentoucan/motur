import datetime
from unittest.mock import ANY
from generated.mot_client.models.defect import Defect
from generated.mot_client.models.defect_type import DefectType
from generated.mot_client.models.dvsa_mot_test import DVSAMotTest
from generated.mot_client.models.dvsa_mot_test_data_source import DVSAMotTestDataSource
from generated.mot_client.models.dvsa_mot_test_odometer_result_type import DVSAMotTestOdometerResultType
from generated.mot_client.models.dvsa_mot_test_test_result import DVSAMotTestTestResult
from generated.mot_client.models.error_response import ErrorResponse
from generated.mot_client.models.new_reg_vehicle_response import NewRegVehicleResponse
from generated.mot_client.models.new_reg_vehicle_response_has_outstanding_recall import NewRegVehicleResponseHasOutstandingRecall
from generated.mot_client.models.vehicle_with_mot_response import VehicleWithMotResponse
from generated.mot_client.models.vehicle_with_mot_response_has_outstanding_recall import VehicleWithMotResponseHasOutstandingRecall
from mot_api_service import MotErrorResponse, MotSummaryInformation, MotTest, MotTestDefect, fetch_mot_history
import pytest

@pytest.mark.asyncio
async def test_fetch_vehicle_invalid_bearer_token_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_mot_client = mocker.patch("mot_api_service.get_v1_trade_vehicles_registration_registration.asyncio")
  result = await fetch_mot_history(registration_plate)

  assert result == MotErrorResponse(errorMessage="Unable to authenticate with the MOT API")
  mock_mot_client.assert_not_called()

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_old_vehicle_returns_mot_summary_information(mocker):
  registration_plate = "AA11 AAA"
  now = datetime.datetime.now()
  mock_response = VehicleWithMotResponse(
    registration=registration_plate,
    make="ford",
    has_outstanding_recall=VehicleWithMotResponseHasOutstandingRecall.UNKNOWN,
    mot_tests=[DVSAMotTest(completed_date=now, test_result=DVSAMotTestTestResult.PASSED, data_source=DVSAMotTestDataSource.DVSA, odometer_result_type=DVSAMotTestOdometerResultType.READ, defects=[Defect(text="Rover won't turn over", type_=DefectType.DANGEROUS, dangerous=True)])]) # type: ignore
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})
  mock_mot_client = mocker.patch("mot_api_service.get_v1_trade_vehicles_registration_registration.asyncio", return_value=mock_response)
  result = await fetch_mot_history(registration_plate)

  assert result == MotSummaryInformation(
    registration=mock_response.registration, # type: ignore
    make=mock_response.make, # type: ignore
    motTests=[MotTest(completedDate=now, testResult="PASSED", dataSource="DVSA", odometerResultType="READ", defects=[MotTestDefect(text="Rover won't turn over", type=DefectType.DANGEROUS, dangerous=True)])]) # type: ignore
  mock_mot_client.assert_called_once_with(client=ANY, registration=registration_plate)

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_new_reg_vehicle_returns_mot_summary_information(mocker):
  registration_plate = "AA11 AAA"
  now = datetime.datetime.now()
  mock_response = NewRegVehicleResponse(
    registration=registration_plate,
    make="ford",
    has_outstanding_recall=NewRegVehicleResponseHasOutstandingRecall.UNKNOWN,
    mot_test_due_date=now.date()) # type: ignore
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})
  mock_mot_client = mocker.patch("mot_api_service.get_v1_trade_vehicles_registration_registration.asyncio", return_value=mock_response)
  result = await fetch_mot_history(registration_plate)

  assert result == MotSummaryInformation(
    registration=mock_response.registration, # type: ignore
    make=mock_response.make, # type: ignore
    motTestDueDate=now.date(),
    motTests=[]) # type: ignore
  mock_mot_client.assert_called_once_with(client=ANY, registration=registration_plate)

@pytest.mark.asyncio
async def test_fetch_vehicle_mot_returns_mot_error_response(mocker):
  registration_plate = "AA11 AAA"
  mock_response = ErrorResponse(error_message="Vehicle does not exist")
  mock_msal_client = mocker.Mock()
  mocker.patch("mot_api_service.msal.ConfidentialClientApplication", return_value=mock_msal_client)
  mock_msal_client.acquire_token_for_client = mocker.Mock(return_value={'token_type': 'mock_token', 'access_token': 'blah'})
  mock_mot_client = mocker.patch("mot_api_service.get_v1_trade_vehicles_registration_registration.asyncio", return_value=mock_response)
  result = await fetch_mot_history(registration_plate)

  assert result == MotErrorResponse(errorMessage="Vehicle does not exist")
  mock_mot_client.assert_called_once_with(client=ANY, registration=registration_plate)

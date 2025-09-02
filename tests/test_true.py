
import os
from anpr_service import AnprService
from config import Settings
import pytest

fake_settings = Settings(
  enabled_sites=[""],
  scraper=Settings.Scraper(chrome_binary_location="dummy_path", disable_sandbox=False, image_path="dummy_path"))

anpr_service: AnprService = AnprService()

valid_data_path="./tests/data/valid_data"
invalid_data_path="./tests/data/invalid_data"

@pytest.fixture(params=os.listdir(valid_data_path))
def valid_data_image_file(request):
    return request.param

@pytest.fixture(params=os.listdir(invalid_data_path))
def invalid_data_image_file(request):
    return request.param

def test_vehicle_registration_plates_are_matched(valid_data_image_file):
  path_parts = os.path.splitext(valid_data_image_file)
  reg_to_find: str = path_parts[0]
  registration: str | None = anpr_service.find_registration_plate(f"{valid_data_path}/{valid_data_image_file}")
  assert registration == reg_to_find

def test_missing_vehicle_registration_plates_return_none(invalid_data_image_file):
  registration: str | None = anpr_service.find_registration_plate(f"{invalid_data_path}/{invalid_data_image_file}")
  assert registration is None

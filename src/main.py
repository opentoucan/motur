from pydantic import BaseModel
from mot_api_service import MotApiService
from ves_api_service import VesApiService
from vehicle_service import VehicleService
import scraper
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from urllib.parse import urlparse
from config import GetHishelTransport, VehicleSettings, settings

class WebpageScrape(BaseModel):
   url: str

app = FastAPI()
vehicle_settings: VehicleSettings = VehicleSettings() # type: ignore
http_transport = GetHishelTransport()
vehicle_service: VehicleService = VehicleService(MotApiService(http_transport, vehicle_settings), VesApiService(http_transport, vehicle_settings))

@app.get("/reg/{reg}")
async def read_mot_from_reg(reg: str):

    vehicle_information = await vehicle_service.fetch_vehicle_information(reg)
    return vehicle_information.model_dump()

@app.post("/link")
async def read_mot_from_webpage(webpage: WebpageScrape):
  domain = urlparse(webpage.url).netloc
  if domain not in settings.enabled_sites:
    raise HTTPException(status_code=400, detail=f"Website {domain} is not enabled")

  registration_plate = await scraper.scrape_link(webpage.url)
  if registration_plate is not None:
    vehicle_information = await vehicle_service.fetch_vehicle_information(registration_plate)
    return vehicle_information.model_dump()

  return "Could not find registration details"

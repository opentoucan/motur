from pydantic import BaseModel
from mot_api_service import MotApiService
from ves_api_service import VesApiService
from vehicle_service import VehicleService
from scraper_service import ScraperService
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from urllib.parse import urljoin, urlparse
from config import GetHishelTransport, Settings

class WebpageScrape(BaseModel):
   url: str

app = FastAPI()
settings = Settings() # type: ignore
http_transport = GetHishelTransport(settings)
vehicle_service: VehicleService = VehicleService(MotApiService(http_transport, settings), VesApiService(http_transport, settings))
scraper_service: ScraperService = ScraperService(settings)

@app.get("/reg/{reg}")
async def read_mot_from_reg(reg: str):
    vehicle_information = await vehicle_service.fetch_vehicle_information(reg)
    return vehicle_information.model_dump(exclude_none=True)

@app.post("/link")
async def read_mot_from_webpage(webpage: WebpageScrape):
  parsed_url = urlparse(webpage.url)
  normalised_url = urljoin(webpage.url, parsed_url.path)
  domain = parsed_url.netloc
  if domain not in settings.enabled_sites:
    raise HTTPException(status_code=400, detail=f"Website {domain} is not enabled")

  registration_plate = await scraper_service.scrape_link(normalised_url)
  if registration_plate is not None:
    vehicle_information = await vehicle_service.fetch_vehicle_information(registration_plate)
    return vehicle_information.model_dump(exclude_none=True)

  raise HTTPException(status_code=400, detail="Could not identify the vehicle on the page")

from pydantic import BaseModel
import vehicle_service
import scraper
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from urllib.parse import urlparse
from config import settings

class WebpageScrape(BaseModel):
   url: str

app = FastAPI()

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

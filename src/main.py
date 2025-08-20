import vehicle_service
import scraper
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from urllib.parse import urlparse
from config import settings

app = FastAPI()

@app.get("/reg/{reg}")
async def read_mot_from_reg(reg: str):
    return await vehicle_service.fetch_vehicle_information(reg)

@app.get("/link/{url}")
async def read_mot_from_webpage(url: str):
  domain = urlparse(url).netloc
  if domain not in settings.enabled_sites:
    raise HTTPException(status_code=400, detail=f"Website {domain} is not enabled")

  registration_plate = await scraper.scrape_link(url)
  if registration_plate is not None:
    return await vehicle_service.fetch_vehicle_information(registration_plate)

  return "Could not find registration details"

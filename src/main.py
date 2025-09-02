from pydantic import BaseModel
from scraper_service import ScraperService
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from urllib.parse import urljoin, urlparse
from config import Settings
from anpr_service import AnprService

class WebpageScrape(BaseModel):
   url: str

app = FastAPI()
settings = Settings() # type: ignore
anpr_service = AnprService()
scraper_service: ScraperService = ScraperService(settings, anpr_service)

@app.post("/link")
async def read_registration_plate_from_webpage(webpage: WebpageScrape):
  parsed_url = urlparse(webpage.url)
  normalised_url = urljoin(webpage.url, parsed_url.path)
  domain = parsed_url.netloc
  if domain not in settings.enabled_sites:
    raise HTTPException(status_code=400, detail=f"Website {domain} is not enabled")

  registration_plate = await scraper_service.scrape_link(normalised_url)
  if registration_plate is not None:
    return registration_plate

  raise HTTPException(status_code=400, detail="Could not identify the vehicle on the page")

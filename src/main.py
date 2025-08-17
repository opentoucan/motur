from fastapi import FastAPI
import mot_service
import scraper
import anpr_service
import os
import glob

app = FastAPI()

@app.get("/reg")
def read_mot_from_reg(reg: str):
    return mot_service.fetch_history(reg)

@app.get("/link")
async def read_mot_from_webpage(url: str):
  image_url_list = await scraper.scrape_link(url)
  registration_plate = anpr_service.find_registration_plate(image_url_list)
  for filename in glob.glob("*.png"):
    os.remove(filename)
  if registration_plate is not None:
    mot_history = mot_service.fetch_history(registration_plate)
    return mot_history
  return "Could not find registration details"

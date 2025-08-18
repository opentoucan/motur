import os
import glob
import validators
import anpr_service
from pydoll.browser import Chrome
from pydoll.browser.options import ChromiumOptions
from urllib.parse import urlparse
from config import settings
from typing import Optional

async def scrape_link(url: str) -> Optional[str]:
  options = ChromiumOptions()
  options.add_argument('--headless=new')
  options.add_argument('--start-maximized')
  options.add_argument('--disable-notifications')
  options.add_argument('--user-agent=new_useragent')
  options.add_argument('--disable-dev-shm-usage') # Overcome limited resource issues

  if settings.scraper.disable_sandbox:
    options.add_argument("--no-sandbox")
  options.binary_location = settings.scraper.chrome_binary_location

  registration_plate = None
  async with Chrome(options=options) as browser:

    tab = await browser.start()
    tab.expect_and_bypass_cloudflare_captcha()
    await tab.go_to(url)

    image_elements = await tab.find(tag_name='img', find_all=True)
    for element in image_elements:
      image_src = element.get_attribute('src')
      if image_src is not None and validators.url(image_src):
        img_tab = await browser.new_tab(image_src)
        image_name = os.path.basename(urlparse(image_src).path)
        await img_tab.take_screenshot(f"{settings.scraper.image_path}/{image_name}.png")
        registration_plate = anpr_service.find_registration_plate(f"{settings.scraper.image_path}/{image_name}.png")
        if registration_plate is not None:
          break

    for filename in glob.glob(f"{settings.scraper.image_path}/*.png"):
      os.remove(filename)

    await browser.stop()
    return registration_plate

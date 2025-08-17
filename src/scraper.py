from pydoll.browser import Chrome
from pydoll.browser.options import ChromiumOptions
import validators
import requests
from urllib.parse import urlparse
import os

supported_urls = ["www.autotrader.co.uk", "www.carandclassic.com"]

async def scrape_link(url: str):
  options = ChromiumOptions()
  options.add_argument('--headless=new')
  options.add_argument('--start-maximized')
  options.add_argument('--disable-notifications')
  options.add_argument('--user-agent=new_useragent')
  #options.add_argument("--no-sandbox")
  options.binary_location = '/nix/store/ixvs3iggafi1pic1vmgfy2hxn95d3qpa-google-chrome-139.0.7258.66/bin/google-chrome-stable'
  async with Chrome(options=options) as browser:

    tab = await browser.start()
    tab.expect_and_bypass_cloudflare_captcha()
    await tab.go_to(url)

    image_elements = await tab.find(tag_name='img', find_all=True)
    images = []
    for element in image_elements:
      image_src = element.get_attribute('src')
      if(validators.url(image_src)):
        img_tab = await browser.new_tab(image_src)
        image_name = os.path.basename(urlparse(image_src).path)
        await img_tab.take_screenshot(f"{image_name}.png")
        images.append(f"{image_name}.png")

    await browser.stop()
    return images

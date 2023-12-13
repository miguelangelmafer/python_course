import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests

header = {
    "Accept-Language": "es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}

# Use our Zillow-Clone website (instead of Zillow.com)
response = requests.get("https://www.idealista.com/buscar/alquiler-viviendas/valencia/", headers=header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".item-info-container a")
all_links = [link["href"] for link in all_link_elements if not link.find_parent(class_="logo-branding")]
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

# Create a list of all the addresses on the page using a CSS Selector
all_address_elements = soup.select(".item-info-container a")
all_addresses = [address["title"].replace(" | ", " ").strip() for address in all_address_elements if not address.find_parent(class_='logo-branding')]
print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)


# Create a list of all the prices on the page using a CSS Selector
all_price_elements = soup.select(".item-price")
all_prices = [price.get_text().replace("/mes","") for price in all_price_elements]
print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)

#Selenium fill survey
url_survey = os.environ.get("url_survey")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

for n in range(len(all_links)):
    driver.get(url_survey)
    time.sleep(2)

    place = driver.find_element(By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    price = driver.find_element(By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea')
    url = driver.find_element(By.XPATH,
                              value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    place.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    url.send_keys("https://www.idealista.com/" + all_links[n])
    submit_button.click()

driver.close()
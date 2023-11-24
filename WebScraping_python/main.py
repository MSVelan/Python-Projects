from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import html5lib, time
import requests
from pprint import pprint

zillowUrl = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.85381150365383%2C%22east%22%3A-122.29840365771484%2C%22south%22%3A37.69668892292081%2C%22west%22%3A-122.56825534228516%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

formUrl = "https://docs.google.com/forms/d/e/1FAIpQLScPQz2GQfeYk_BZkvI1QYCfjLvmPgWhuww3IoAxjlecyAwO0g/viewform?usp=sf_link"

endPoint = "https://www.zillow.com"
# Tasks: Use beautifulSoup/Requests to scrape data from magicBricksUrl

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB,en;q=0.9,en-US;q=0.8,ta;q=0.7",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

response = requests.get(url=zillowUrl, headers=headers)
BricksPg = response.content

soup = BeautifulSoup(BricksPg, "html5lib")
# pprint(soup)

AllPrices = soup.find_all(name="span", class_="iMKTKr")
prices = [a.getText(strip=True) for a in AllPrices]

AllLinks = soup.find_all(name="a", class_="property-card-link")
links = [a.get("href") for a in AllLinks]
fullLinks = [endPoint+a if a[0]=='/' else a for a in links]

AllAddresses = soup.find_all(name="address")
addresses = [a.getText() for a in AllAddresses]

# print(prices)
# print(fullLinks)
# print(addresses)
# Use selenium to fill in the Google form with the above information

driver = webdriver.Chrome()


for i, [a, p, l] in enumerate(zip(addresses, prices, fullLinks)):
    driver.get(url=formUrl)
    driver.implicitly_wait(5.0)
    print(a,"\n", p, "\n", l, "\n")

    time.sleep(0.5)
    
    inputs = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//input[@class='whsOnd zHQkBf'][@jsname='YPqjbf']")))

    
    inputs[0].send_keys(a)
    time.sleep(0.5)

    inputs[1].send_keys(p)
    time.sleep(0.5)

    inputs[2].send_keys(l)
    time.sleep(0.5)

    submitBtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")))
    submitBtn.click()


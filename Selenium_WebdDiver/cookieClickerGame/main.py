from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime, time

start = datetime.datetime.now()
driver = webdriver.Chrome()

cookieWebsite = "http://orteil.dashnet.org/experiments/cookie/"


def returnInt(value):
    return int(''.join(value.split(',')))


k=0
driver.get(cookieWebsite)
while True:
    now = datetime.datetime.now()
    diff = (now-start).total_seconds()
    if(diff-5*k>=0):
        elements = driver.find_elements(By.CSS_SELECTOR,"#rightPanel #store b")
        values = [(a.text).split() for a in elements[:-1]]
        values = [returnInt(value[-1]) for value in values]
        currentMoney = int(driver.find_element(By.ID,"money").text)
        for i in range(len(values)-1,-1,-1):
            if(values[i]<=currentMoney):
                elements[i].click()
                break
        k+=1
    if(diff>300):
        break
    cookie = driver.find_element(By.CSS_SELECTOR,"#middle #cookie")
    cookie.click()

driver.close()
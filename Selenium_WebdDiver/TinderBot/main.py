from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

fbEmail = "bonap32310@extemer.com"
fbPassword = "randomPerson123"

driver = webdriver.Chrome()

driver.get("https://tinder.com/")

try:
    acceptBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")))
    acceptBtn.click()
    # driver.implicitly_wait(1.0)
except:
    print("Accept Button not found")

time.sleep(2.0)
loginBtn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")))
loginBtn.click()
# driver.implicitly_wait(1.0)

time.sleep(5.0)
facebookBtn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]")))
facebookBtn.click()
# driver.implicitly_wait(1.0)

time.sleep(5.0)
tinderWindow = driver.window_handles[0]
fbWindow = driver.window_handles[1]

driver.switch_to.window(fbWindow)
# print(driver.title)

emailInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"email")))
emailInput.send_keys(fbEmail)

time.sleep(1.0)

passwordInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"pass")))
passwordInput.send_keys(fbPassword)

loginFb = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME,"login")))
loginFb.click()

time.sleep(1.0)

driver.switch_to.window(tinderWindow)
# print(driver.title)

acceptTinder = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")))
acceptTinder.click()

notification = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]")))
notification.click()

driver.implicitly_wait(20.0)

time.sleep(4.0)

firstLike = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span")))

firstLike.click()

for i in range(99):
    time.sleep(2.0)
    likeBtn = WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")))
    likeBtn.click()

time.sleep(300.0)
driver.quit()

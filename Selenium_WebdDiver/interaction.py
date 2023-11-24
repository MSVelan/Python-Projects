from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# wikipedia = "https://en.wikipedia.org/wiki/Main_Page"

# driver.get(url=wikipedia)

# articleCount = driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(articleCount.text)

# articleCount.click()

# allPortals = driver.find_element(By.LINK_TEXT,"View history")
# allPortals.click()

# searchBar = driver.find_element(By.NAME,"search")
# searchBar.send_keys("Python")
# searchBar.send_keys(Keys.ENTER)

formPage = "http://secure-retreat-92358.herokuapp.com/"
driver.get(formPage)

firstName = driver.find_element(By.NAME, "fName")
firstName.send_keys("MS")

lastName = driver.find_element(By.NAME,"lName")
lastName.send_keys("Velan")

Email = driver.find_element(By.NAME,"email")
Email.send_keys("testing@gmail.com")

btn = driver.find_element(By.TAG_NAME,"button")
btn.click()

time.sleep(2000)
driver.quit()
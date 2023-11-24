
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(url="https://www.python.org/")

# driver.close() -shutdown current tab

# shutdown entire browser

eventTimings = [a.text for a in driver.find_elements(By.CSS_SELECTOR,".event-widget time")]
events = [a.text for a in driver.find_elements(By.CSS_SELECTOR,".event-widget .menu a")]

# print(eventTimings)
# print(events)

d = {}
for i, element in enumerate(zip(eventTimings,events)):
    d[i]={"time":element[0],"name":element[1]}

print(d)
driver.quit()
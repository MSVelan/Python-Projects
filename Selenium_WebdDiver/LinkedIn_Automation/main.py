from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Endpoint = "https://www.linkedin.com/jobs/search/?currentJobId=3538511592&f_E=1%2C2&f_T=2732%2C9%2C25169%2C54%2C24%2C11845&f_WT=2&keywords=python%20developer&refresh=true&sortBy=R"

email = "muthiahsivavelan2026@gmail.com"
password = "testing12@MSV"

driver = webdriver.Chrome()
driver.get(Endpoint)

signinBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav__cta-container .nav__button-secondary")))
signinBtn.click()

emailBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
emailBtn.send_keys(email)

time.sleep(1.0)
passwordBtn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
passwordBtn.send_keys(password)

time.sleep(1.0)
formSubmit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login__form_action_container button")))
formSubmit.click()

time.sleep(6.0)
try:
    minimiseBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "ember113")))
    minimiseBtn.click()
except:
    print("Can't minimise for now")

while True:
    jobs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container")))
    n = len(jobs)
    print(n)
    for i in range(n):
        jobs = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container")))
        job = jobs[i]
        job.click()
        time.sleep(2.0)
        
        jobSaveBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-save-button")))
        if(jobSaveBtn.text != "Saved"):
            jobSaveBtn.click()

        a = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-unified-top-card__company-name a")))
        a.click()


        followBtn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "org-company-follow-button")))
        if followBtn.text != "Following":
            followBtn.click()
        
        try:
            closeBtn = WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-modal__dismiss")))
            closeBtn.click()
        except:
            print("Notification alert is not present")

        driver.back()
        jobs_container = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container")))
        driver.execute_script("return arguments[0].scrollIntoView();", jobs_container)
        driver.execute_script("window.scrollBy(0, 100);")
    jobs_container = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container")))
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollHeight;', 
        jobs_container)
    time.sleep(1.0)

time.sleep(120.0)
driver.quit()
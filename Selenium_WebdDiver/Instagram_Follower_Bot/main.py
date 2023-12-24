from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

class InstaFollower:
    driver = webdriver.Chrome()

    def __init__(self) -> None:
        pass

    def login(self):
        # URL = "https://www.instagram.com/accounts/login/"
        
        # self.driver.get(url=URL)

        # username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,"username")))
        # username_input.send_keys(USERNAME)

        # password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,"password")))
        # password_input.send_keys(PASSWORD)

        # loginBtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button")))
        # loginBtn.click()

        # try:
        #     notifyOffBtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")))
        #     notifyOffBtn.click()
        # except Exception as e:
        #     print("Error occurred: ", e)

        # time.sleep(10.0)

        # self.cookies = self.driver.get_cookies()
        # print(self.cookies)
        # pickle.dump(self.cookies, open("cookies.pkl", "wb"))

        self.driver.get("https://www.instagram.com/")
        cookies = pickle.load(open("cookies.pkl","rb"))

        for cookie in cookies:
            cookie["domain"]=".instagram.com"
            try:
                self.driver.add_cookie(cookie)
            except Exception as e:
                print(e)

        self.driver.get("https://www.instagram.com/")

    def findFollowers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        followersList = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")))
        followersList.click()

        followersDiv = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"_aano")))
        # rows = followersDiv.find_element(By.XPATH,".//div/div")
        while True:
            self.follow()
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollHeight;', 
                followersDiv)
            # time.sleep(1.0)

    def follow(self):
        rows = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"_aano")))
        for btn in WebDriverWait(rows, 10).until(EC.presence_of_all_elements_located((By.XPATH,".//button[contains(@class,'_acan')]"))):
            if(btn.text=="Follow"):
                try:
                    btn.click()
                except ElementClickInterceptedException:
                    print("ElementClickInterceptedException")
                time.sleep(1.0)

Bot = InstaFollower()
Bot.login()
Bot.findFollowers()
time.sleep(360.0)
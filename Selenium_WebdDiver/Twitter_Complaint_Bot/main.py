from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

PROMISED_UP = 1
PROMISED_DOWN = 5
TWITTER_USER = "@muthiah1822"
TWITTER_PASSWORD = "MSVgeek726"

TWEET_FORMAT = '''I wonder how to check the promised up and down speed for my current data plan
My stats according to speedtest.net
    Up speed: {up}
    Down speed: {down}'''

class waittest:
    def __init__(self, locator, value):
        self._locator = locator
        self._attribute_value = value

    def __call__(self, driver):
        element = driver.find_element(By.CLASS_NAME, self._locator)
        text = element.text.strip()
        if text and text != self._attribute_value:
            return element


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        try:
            closeCookieBtn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "onetrust-close-btn-container"))
            )
            closeCookieBtn.click()
        except:
            print("Privacy button not found")

        startBtn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "start-text"))
        )
        startBtn.click()

        wait = WebDriverWait(self.driver, 60)

        wait.until(waittest("download-speed", "—"))
        downloadElement = self.driver.find_element(By.CLASS_NAME, "download-speed")
        self.down = (downloadElement.text)

        wait.until(waittest("upload-speed", "—"))
        uploadElement = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.up = (uploadElement.text)


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10.0)

        signInBtn = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.NAME,"text")))
        signInBtn.send_keys(TWITTER_USER)
        signInBtn.send_keys(Keys.ENTER)


        passwrd = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME,"password")))
        passwrd.send_keys(TWITTER_PASSWORD)
        passwrd.send_keys(Keys.ENTER)

        msgbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div")))
        msgbox.click()
        msgbox.send_keys(TWEET_FORMAT.format(up=self.up,down=self.down))

        time.sleep(1.0)
        tweetBtn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span")))

        tweetBtn.click()
        
        print(TWEET_FORMAT.format(up=self.up,down=self.down))
        time.sleep(30.0)

    def __del__(self):
        print("Destructor is called!")
        self.driver.quit()


Bot = InternetSpeedTwitterBot()
Bot.get_internet_speed()
Bot.tweet_at_provider()
del Bot

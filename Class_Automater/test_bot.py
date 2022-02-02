from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import re
import os.path
from os import path
import sqlite3
import schedule
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import discord_webhook

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--start-maximized")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

# driver = webdriver.Chrome(chrome_options=opt,service_log_path='NUL')
# driver = webdriver.Chrome('C:/Users/a2z\Downloads\microsoft-teams-class-attender\chromedriver.exe')

URL = "https://teams.microsoft.com"

# put your teams credentials here
CREDS = {'email': 'aditya14256@hrc.edu.du.ac.in', 'passwd': 'Saymyname@12345'}


def login():
    global driver
    # login required
    print("logging in")
    time.sleep(5)
    emailField = driver.find_element_by_id("i0116")
    driver.switch_to.default_content()



# return driver

def start_browser():
    global driver
    driver = webdriver.Chrome(options=opt, service_log_path='NUL')
    driver.get(URL)


    WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(1)
    if "login.microsoftonline.com" in driver.current_url:
        driver.maximize_window()
        login()

start_browser()
import os
import selenium
from selenium import webdriver
import time
import io
import requests
from PIL import Image
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome("C:/Users/a2z/.wdm/drivers/chromedriver/win32/chromedriver.exe")
search_url="http://www.ycyeah.site/#/win"
def site_login():
    driver.get(search_url)
    driver.find_element_by_id("1").click()
    driver.find_element_by_id("email").send_keys("9667726459")
    driver.find_element_by_id ("password").send_keys("12345677")
    driver.find_element_by_id("submit").click()
site_login()


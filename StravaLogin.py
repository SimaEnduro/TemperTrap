from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()

# open strava.com
driver.get("http://www.strava.com")
assert "Strava | Run and Cycling Tracking on the Social Network for Athletes" in driver.title
assert "No results found." not in driver.title

if not (os.path.exists('./screenshots')):
    os.makedirs('./screenshots')

driver.save_screenshot('./screenshots/screenshot.png')

driver.close()

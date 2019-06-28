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

driver.save_screenshot('./screenshots/Strava_LandingPage.png')

# driver.implicitly_wait(60)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign up with Facebook')))

driver.save_screenshot('./screenshots/Strava_LandingPage_maximize.png')

driver.close()

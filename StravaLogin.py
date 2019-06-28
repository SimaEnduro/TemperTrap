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

driver.save_screenshot('./screenshots/1_Strava_LandingPage.png')

# driver.implicitly_wait(60)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign up with Facebook')))

driver.save_screenshot('./screenshots/2_Strava_LandingPage_maximize.png')


# open login screen
fb_signup = driver.find_element_by_link_text('Log In')
fb_signup.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'email')))

driver.save_screenshot('./screenshots/3_OpenLoginScreen.png')

# enter login details
username = driver.find_element_by_id('email')
username.send_keys("simona.jurenkova@gmail.com")
password = driver.find_element_by_id('password')
password.send_keys("S1mcaL1mca!1")

login = driver.find_element_by_id('login-button')
login.click()

wait = WebDriverWait(driver, 10)

driver.save_screenshot('./screenshots/4_Login.png')

driver.close()

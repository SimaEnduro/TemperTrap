from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver import ActionChains
# from selenium.webdriver import TouchActions
# from selenium.common.exceptions import ElementClickInterceptedException





driver = webdriver.Chrome()


driver.get('https://github.com/login?return_to=%2FSimaEnduro')
driver.maximize_window()
driver.find_element_by_name('login').send_keys('SimaEnduro')
driver.find_element_by_name('password').send_keys('S1mcaL1mca!1')
submit = driver.find_element_by_name('commit')
submit.click()

elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Overview'))
)

newpath = r'C:/Users/simona.jurenkova/Documents/code/GIT/TemperTrap/screens'
if not os.path.exists(newpath):
    os.makedirs(newpath)

# open strava.com
driver.get("http://www.strava.com")
assert "Strava | Run and Cycling Tracking on the Social Network for Athletes" in driver.title
assert "No results found." not in driver.title

# driver.implicitly_wait(60)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Sign up with Facebook')))

driver.save_screenshot('/screens/screenshot.png')

# open login screen
fb_signup = driver.find_element_by_link_text('Sign up with Facebook')
fb_signup.click()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'email')))

driver.save_screenshot('/screens/screenshot2.png')

# enter login details
username = driver.find_element_by_id('email')
username.send_keys("simona.jurenkova@gmail.com")
password = driver.find_element_by_id('pass')
password.send_keys("S1mcaL1mca!1")

login = driver.find_element_by_id('loginbutton')
login.click()


# open my Strava profile
wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'athlete-name')))

# by_class = driver.find_element_by_class_name('athlete-name')
# by_class = driver.find_element_by_class_name('avatar-img')
# by_class.click()

import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load JSON data
with open('user_data.json') as f:
    users = json.load(f)

last_user = users[-1]

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.xampro.org/login')

# Log in with the last registered user
driver.find_element(By.XPATH, "//input[@id='email']").send_keys(last_user['email'])
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(last_user['password'])
driver.find_element(By.XPATH, "//div[@class='account-access-submit-button']//img").click()
time.sleep(10)


driver.quit()

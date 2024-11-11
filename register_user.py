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
driver.get('https://www.xampro.org/signup')

# Fill in the registration form
driver.find_element(By.XPATH, "//input[@id='name']").send_keys(last_user['name'])
driver.find_element(By.XPATH, "//input[@id='email']").send_keys(last_user['email'])
driver.find_element(By.XPATH, "//input[@id='phoneNumber']").send_keys(last_user['phone'])
driver.find_element(By.XPATH, "//input[@id='password']").send_keys(last_user['password'])
driver.find_element(By.XPATH, "//input[@id='confirmPassword']").send_keys(last_user['password'])


driver.find_element(By.XPATH, "//div[@class='account-access-submit-button']//img").click()


time.sleep(5)

driver.quit()

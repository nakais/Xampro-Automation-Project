import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

# Navigate to profile page
time.sleep(5)
driver.get('https://www.xampro.org/profile')
driver.execute_script("window.scrollBy(0, 300);") 

# Update Date of Birth
time.sleep(5)
date_of_birth_field = driver.find_element(By.XPATH, "//input[@id='dob']")
date_of_birth_field.clear()
date_of_birth_field.send_keys('08/23/1995')  

# Update Gender
time.sleep(5)
gender_radio = driver.find_element(By.XPATH, "//input[@id='radio-gender-male']")  
gender_radio.click()

# Update Education
time.sleep(5)
education_dropdown = driver.find_element(By.XPATH, "//select[@id='education']")
education_dropdown.click()

for i in range(5):
    time.sleep(1)
    education_dropdown.send_keys(Keys.DOWN)

time.sleep(3)
education_dropdown.send_keys(Keys.ENTER)

# Update University
#time.sleep(5)
#university_dropdown = driver.find_element(By.XPATH, "//div[@class=' css-19bb58m']")
#university_dropdown.click()



time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']").click()  
time.sleep(5)

driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
time.sleep(5)

#Creating account
register_button = driver.find_element(By.XPATH,"//*[@class='btn1']")
register_button.click()
time.sleep(5)

#first name
first_name = driver.find_element(By.XPATH,"//input[@type = 'firstName']")
first_name.send_keys("Bhagyashree")
time.sleep(5)

#last name
last_name = driver.find_element(By.XPATH,"//input[@type = 'lastName']")
last_name.send_keys("Bhatia")
time.sleep(5)

#Explicit wait
#first_name = wait.until(
#    EC.visibility_of_element_located((By.NAME, "firstName"))


#email id
email_id = driver.find_element(By.XPATH,"//input[@type = 'email']")
email_id.send_keys("bhagyashree3@example.com")
time.sleep(5)

#phone number
phone_number = driver.find_element(By.XPATH,"//input[@id='userMobile' and @placeholder = 'enter your number']")

phone_number.send_keys("1234567890")
print("Phone number added successfully")
time.sleep(5)

#occupation selection
occupation = driver.find_element(By.XPATH,"//*[@class='custom-select ng-untouched ng-pristine ng-valid']")
occupation.send_keys("Engineer")
print("Occupation added successfully")
time.sleep(5)

#gender selection
gender = driver.find_element(By.XPATH,"//input[@value='Female']")
gender.click()
time.sleep(5)

#password
password = driver.find_element(By.XPATH,"//input[@id='userPassword']")
password.send_keys("Rahul@123")
time.sleep(5)

#confirm password
confirm_password = driver.find_element(By.XPATH,"//input[@id='confirmPassword']")
confirm_password.send_keys("Rahul@123")
time.sleep(5)

#check box
check_box_selection = driver.find_element(By.XPATH,"//input[@class='ng-dirty ng-valid ng-touched' or @type='checkbox']")
check_box_selection.click()
time.sleep(5)

#Registaation
registration = driver.find_element(By.XPATH,"//input[@type='submit']")
registration.click()
time.sleep(5)
print("Registration successfully done")

#login button
login = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
login.click()
time.sleep(5)

if "login" in driver.current_url:
    print("navigated to login section")
    time.sleep(5)
else:
    print("login failed")







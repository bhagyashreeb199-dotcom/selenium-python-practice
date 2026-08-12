import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.implicitly_wait(30)


#forgot password
forgot_password_xpath = "//*[@class='forgot-password-link']"
email_id_xpath = "//input[@type='email']"
password_forgot_page_xpath = "//input[@id='userPassword']"
confirm_password_forgot_page_xpath = "//input[@id='confirmPassword']"
save_new_password_xpath = "//button[@type='submit']"

# Step 1:- change password so first click on forgot password link
print("Step 1: -Clicking on forgot password link")
forgot_password = driver.find_element(By.XPATH, forgot_password_xpath)
forgot_password.click()
time.sleep(5)

# Step 2:- Verifying that user navigate to Forgot password Page
print("Step 2:- Verifying that user navigates to forgot password page")
forgot_password_header_xpath = "//*[@class='card-title text-center']"
forgot_password_header = driver.find_element(By.XPATH, forgot_password_header_xpath)
assert forgot_password_header.is_displayed()
assert forgot_password_header.text == "Enter New Password"
print("Step 3:- User navigates to forgot password page successfully")

# Step 3: - enter email id
print("Step 3:- Entering email id")
email_id = driver.find_element(By.XPATH, email_id_xpath)
email_id.send_keys("bhagyashree3@example.com")

# Step 4:- enter the new password
print("Step 4:- Entering new password")
new_password = driver.find_element(By.XPATH, password_forgot_page_xpath)
new_password.send_keys("Rahul@1234")

# Step 5:- enter the confirm password
print("Step 5:- Entering confirm password")
confirm_password = driver.find_element(By.XPATH, confirm_password_forgot_page_xpath)
confirm_password.send_keys("Rahul@1234")

# Step 6:- click on Save new password button
print("Step 6:- Clicking on Save New Password Button")
save_button = driver.find_element(By.XPATH, save_new_password_xpath)
save_button.click()
time.sleep(2)

# Step 7:- validating that user navigate to login page
print("Step 7:- Verifying user navigates back to login page")
login_page_header_xpath = "//*[@class='login-title']"
login_page_header = driver.find_element(By.XPATH, login_page_header_xpath)
assert login_page_header.is_displayed()
assert login_page_header.text == "Log in"
time.sleep(5)
print("TEST PASSED")



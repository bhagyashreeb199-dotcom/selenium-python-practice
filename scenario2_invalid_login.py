import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)


driver.find_element(By.XPATH,"//input[@name = 'username']").send_keys("admin1")
driver.find_element(By.XPATH,"//input[@name = 'password']").send_keys("password")

login_button = driver.find_element(By.XPATH,"//button[@type = 'submit']")      #web element of login button
#clicking on login button
#driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
login_button_text = login_button.text
assert login_button_text == "Login"
login_button.click()
time.sleep(5)


#get text method to check the invalid creds.
#find_element/find.elements - return web element
invalid_error_message = driver.find_element(By.XPATH,"//*[@class = 'oxd-text oxd-text--p oxd-alert-content-text']")
error_message_text = invalid_error_message.text
print(error_message_text)
#checking if pass or fail
assert error_message_text == "Invalid credentials"


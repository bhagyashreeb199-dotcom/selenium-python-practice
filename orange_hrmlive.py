import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)

#creating function for login
def login_site(driver, username, password):
    driver.find_element(By.XPATH,"//input[@name = 'username']").send_keys(username)
    driver.find_element(By.XPATH,"//input[@name = 'password']").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
    time.sleep(5)

#calling login function
login_site(driver, "admin", "admin123")
time.sleep(10)

if "dashboard" in driver.current_url:
    print("login done")

#clicking on Admin section from side menu
driver.find_element(By.XPATH,"(//span[text() ='Admin']/parent::a)").click()
time.sleep(20)

#clicking on Job option in Admin section
driver.find_element(By.XPATH,"//span[text() = 'Job ' and @class='oxd-topbar-body-nav-tab-item']").click()
time.sleep(5)

#clicking on Job titles in job option
driver.find_element(By.XPATH,"//*[@class='oxd-topbar-body-nav-tab-link' and text() = 'Job Titles']").click()
time.sleep(5)

#clicking on +add button in job titles
driver.find_element(By.XPATH,"//button[@type = 'button' and text() = ' Add ']").click()
time.sleep(5)

#adding job title
driver.find_element(By.XPATH,"(//label[text() ='Job Title']//following::input)[1]").send_keys("Quality Assurance1")
time.sleep(5)

#need to check the validation in job titles field if is shows this "already exists" message it should then clear the field

#entering job description
driver.find_element(By.XPATH,"//*[@class ='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical' and @placeholder ='Type description here']").send_keys("It's a testing job")
time.sleep(5)

#file browsing
file_browser = "/Users/bhagyashreebhatia/Downloads/WhatsApp Image 2026-05-30 at 15.26.48 (1).jpeg"
#driver.find_element(By.XPATH,"//*[@class ='oxd-file-input-div' and text() ='No file chosen']").send_keys(file_browser)
driver.find_element(By.XPATH,"//input[@type='file']").send_keys(file_browser)
time.sleep(5)

#adding notes
driver.find_element(By.XPATH,"//*[@class ='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical' and @placeholder ='Add note']").send_keys("Testing")
time.sleep(5)

#click on Save
driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
time.sleep(10)




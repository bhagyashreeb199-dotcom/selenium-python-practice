import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)

#creating function
def login(driver, username,password):

    driver.find_element(By.XPATH,"//input[@name = 'username']").send_keys(username)
    driver.find_element(By.XPATH,"//input[@name = 'password']").send_keys(password)
    driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
    time.sleep(5)

#calling functions
login(driver,"admin","admin123")

#checking if navigating to home page
if "dashboard" in driver.current_url:
    print("login done")
    
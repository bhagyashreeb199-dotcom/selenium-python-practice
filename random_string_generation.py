import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import random
import string


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com")
driver.implicitly_wait(300)
for _ in range(2):
    random_string = "".join(random.choices(string.ascii_lowercase, k=10))

#entering random sting input
    user_name_field = driver.find_element(By.XPATH,"//input[@name = 'username']")
    user_name_field.send_keys(random_string)
    time.sleep(5)

#clearing field
#driver.find_element(By.XPATH,"//input[@name = 'username']").clear()
    user_name_field.click()
    user_name_field.send_keys(Keys.COMMAND, "a")
    user_name_field.send_keys(Keys.BACKSPACE)
    #validation message
    #user_name_field_text = user_name_field.text
    #assert user_name_field_text == "Required"
    #print("showing message after field gets cleared")

    time.sleep(5)

#adding random input again
    user_name_field.send_keys(random_string)
    time.sleep(10)



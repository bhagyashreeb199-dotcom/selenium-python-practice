import time
from scenario1_login import login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from scenario1_login import login

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)

login(driver,"admin","admin123")
#driver.find_element(By.XPATH,"//input[@name = 'username']").send_keys("Admin")
#driver.find_element(By.XPATH,"//input[@name = 'password']").send_keys("admin123")
#driver.find_element(By.XPATH,"//button[@type = 'submit']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@class='oxd-userdropdown-tab']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@class='oxd-userdropdown-link' and text() = 'Change Password']").click()
time.sleep(5)

#entering current password
driver.find_element(By.XPATH,"(//*[@type='password'])[1]").send_keys("admin123")
time.sleep(5)

#entering  password
driver.find_element(By.XPATH,"(//*[@type='password'])[2]").send_keys("admin1234")
time.sleep(5)

#entering confirm password
driver.find_element(By.XPATH,"(//*[@type='password'])[3]").send_keys("admin1234")
time.sleep(5)

driver.find_element(By.XPATH,"//*[@type='submit']").click()
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='oxd-toaster_1']/div")))

print("successfully changed password")
time.sleep(20)

if "dashboard" in driver.current_url:
    print("successfully landed on dashboard")


driver.find_element(By.XPATH,"//*[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@class='oxd-userdropdown-link' and text() = 'Logout']").click()
time.sleep(5)

print("Successfully logout")


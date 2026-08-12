import selenium
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
print("login successfully")

#driver.find_element(By.XPATH,"//*[@class = 'oxd-main-menu-item' and  @class = 'oxd-main-menu-item active' or text() = 'Leave']").click()
driver.find_element(By.XPATH,"//span[text() = 'Buzz']/parent::a").click()
time.sleep(5)
print("clicked on buzz")

# enter post data "Hello team"
input_text = "Hello Team"
driver.find_element(By.XPATH,"//textarea").send_keys(input_text)
time.sleep(5)

#click on post
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)

#print("clicked on Post button")
#wait = WebDriverWait(driver, 30)
#wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='oxd-toaster_1']/div")))
#print("Posted successfully!")
#time.sleep(30)
# driver.refresh()
# time.sleep(5)


like_button_xpath = "((//*[text()='"+input_text+"']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters'])[2])//*[@id='heart']"
comment_button_xpath = "((//*[text()='"+input_text+"']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters'])[2])//*[@class='oxd-icon bi-chat-text-fill']"
comment_text_area = "((//*[text()='"+input_text+"']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters'])[2])//input"
three_dots_button = "((//*[text()='"+input_text+"']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters'])[2])//*[@class ='oxd-icon bi-three-dots']"
likes_text = "((//*[text()='"+input_text+"']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters'])[2])//*[contains(text(), 'Likes')]"
comment_text = "((//*[text()='"+input_text+"']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters'])[2])//p[contains(text(),'Comments')]"
#comment_text = "((//*[text()='asdf']//ancestor::div[@class='oxd-grid-item oxd-grid-item--gutters'])[2])//p[contains(.,"Comments")]"

driver.find_element(By.XPATH,like_button_xpath).click()
time.sleep(5)

driver.find_element(By.XPATH,comment_button_xpath).click()
time.sleep(5)

driver.find_element(By.XPATH,comment_text_area).send_keys("Automated comment" + Keys.ENTER)
time.sleep(5)

# driver.find_element(By.XPATH,three_dots_button).click()
# time.sleep(5)

# driver.find_element(By.XPATH,likes_text).click()
#time.sleep(5)

# driver.find_element(By.XPATH,comment_text).click()
#time.sleep(5)


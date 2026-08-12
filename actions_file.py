import time

import selenium
import typing_extensions
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.chrome.webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

#Acounts and List Xpath
accounts_and_list_xpath = "//div[@id='nav-link-accountList']"
time.sleep(2)
accounts_and_list = driver.find_element(By.XPATH, accounts_and_list_xpath)
time.sleep(2)

#Hover over Accounts and list
actions = ActionChains(driver)
actions.move_to_element(accounts_and_list).perform()
time.sleep(2)

#right click on amazon logo
# amazon_logo_xpath = "//a[@class='nav-logo-link nav-progressive-attribute']"
# amazon_logo = driver.find_element(By.XPATH, amazon_logo_xpath)
# actions.context_click(amazon_logo).perform()
# time.sleep(5)

# #release the right click
# actions.send_keys(keys.Keys.ESCAPE).perform()
# time.sleep(2)

#Click the search box and enter Value
amazon_search_field_xpath = "//input[@id='twotabsearchtextbox']"
amazon_search_field = driver.find_element(By.XPATH, amazon_search_field_xpath)
#actions.move_to_element(amazon_search_field).click().perform()
actions.click(amazon_search_field)
actions.send_keys("Shoes").perform()
actions.pause(2).perform()

#click on search button
amazon_button_search_xpath = "//input[@type='submit']"
amazon_button_search = driver.find_element(By.XPATH, amazon_button_search_xpath)
actions.click(amazon_button_search).perform()
time.sleep(2)

#Double-click on the product
# double_click_on_product_xpath = "//div[@role='listitem' and @data-uuid]"
# print("double click")
# double_click_on_product = driver.find_element(By.XPATH, double_click_on_product_xpath)
# actions.double_click(double_click_on_product).perform()
# time.sleep(2)

#Use of Keys_down and Keys_up
#Select the entire text in search box
amazon_search_field = driver.find_element(By.XPATH, amazon_search_field_xpath)
actions.click(amazon_search_field).perform()
actions.key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).perform()
time.sleep(2)

#Clear the Text
actions.send_keys(Keys.BACKSPACE).perform()
time.sleep(2)

#Enter the text Clothes
actions.send_keys("Clothes").perform()
time.sleep(2)

#Click on search button
amazon_button_search = driver.find_element(By.XPATH, amazon_button_search_xpath)
actions.click(amazon_button_search).perform()
time.sleep(2)



driver.quit()


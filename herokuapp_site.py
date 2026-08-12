# from selenium.webdriver.support import expected_conditions as EC
#
# import selenium
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# import time
#
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# #driver.get("https://the-internet.herokuapp.com/drag_and_drop")
# driver.get("https://the-internet.herokuapp.com/javascript_alerts?utm_source=chatgpt.com")
# driver.maximize_window()
# print(driver.get_window_size())
#
# # Scenario
# # Open the website.
# # Locate Box A.
# # Locate Box B.
# # Perform drag and drop from Box A → Box B.
# # Verify that Box A and Box B have changed positions.
#
# #Using Drag and drop
# # locate_box_a_xpath = "//div[@id='column-a']"
# # locate_box_b_xpath = "//div[@id='column-b']"
# # locate_box_a = driver.find_element(By.XPATH, locate_box_a_xpath)
# # locate_box_b = driver.find_element(By.XPATH, locate_box_b_xpath)
# # actions = ActionChains(driver)
# # actions.drag_and_drop(locate_box_a, locate_box_b).perform()
# # print("Drag and drop from box A to box B")
# # time.sleep(3)
#
# #Using click_and_hold -> move to element -> release.
# # locate_box_a_xpath = "//div[@id='column-a']"
# # locate_box_b_xpath = "//div[@id='column-b']"
# # locate_box_a = driver.find_element(By.XPATH, locate_box_a_xpath)
# # locate_box_b = driver.find_element(By.XPATH, locate_box_b_xpath)
# #
# # actions = ActionChains(driver)
# # actions.click_and_hold(locate_box_a).perform()
# # print("Click and hold")
# # time.sleep(2)
# # actions.move_to_element(locate_box_b).perform()
# # print("Move")
# # time.sleep(2)
# # actions.release().perform()
# # print("Release")
# # time.sleep(2)
# #
#
# # Handling Alerts (Accept and Dismiss)
# #Click on the popup
# click_for_js_alert_xpath = "//button[@onclick='jsAlert()']"
# click_for_js_alert = driver.find_element(By.XPATH, click_for_js_alert_xpath)
# click_for_js_alert.click()
#
# #Wait and accept the alert
# WebDriverWait(driver, 10).until(EC.alert_is_present())
# alert = driver.switch_to.alert
# alert.accept()
#
# #Print the message showing in result
# result_xpath = "//p[@id='result']"
# result = driver.find_element(By.XPATH, result_xpath)
# print(result.text)
#
#
# #
# # driver.quit()
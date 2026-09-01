# from selenium.webdriver import ActionChains
#
#
# import selenium
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
#
# from amazon_india_site_automation_xpath import campus_brand_selection_xpath, total_number_of_campus_shoes_xpath, \
#     sort_products_dropdown_xpath, low_to_high_option_xpath, selected_low_to_high_option_xpath, next_page_button_xpath, \
#     second_page_text_xpath
# from amazon_india_site_functions_file import *
#
# #
# driver = webdriver.Chrome()
#
# #Open the site
# launch_the_amazon_site(driver)
# time.sleep(5)
#
#
# #
# # # # Scenario 9 ----------------------------------------------------------------------------------
# # # # Apply Filters on Shoes
# # # # Apply filters:
# # # # Brand
# # # # Price
# # # # Customer Rating
# # # # Verify products are still displayed.
# # # # Practice:
# # # # Checkbox
# # # # Dynamic XPath
# # #
# # # #Search for the shoes
# # # print("Input the value in search field")
# # # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # # search_box.send_keys("Shoes")
# # # print("Value Entered ----------------------------------------")
# # #
# # # #Click on Search button
# # # print("Click on Search button")
# # # search_button = driver.find_element(By.XPATH, search_btn_xpath)
# # # search_button.click()
# # # print("Clicked on Search button-------------------------------")
# # # time.sleep(2)
# # #
# # # #Apply filter of Brands
# # # print("Select the check box for campus brand")
# # # campus_brand_selection = driver.find_element(By.XPATH, campus_brand_selection_xpath)
# # # campus_brand_selection.click()
# # # print("Clicked on Campus brand--------------------------------")
# # # time.sleep(5)
# # #
# # # #Check after selecting the Campus its showing Campus result
# # # print("Checking if it is showing result of campus brand")
# # # total_number_of_campus_shoes = driver.find_element(By.XPATH, total_number_of_campus_shoes_xpath)
# # # assert "Campus" in total_number_of_campus_shoes.text
# # # print("Yes, Its showing result of campus brand----------------")
# # #
# # #
# #
# #
# #
# # # Scenario 10: -----------------------------------------------------------------------------------
# # # Sort Products
# # # Search:
# # # Laptop
# # # Select:
# # # Price: Low to High
# # # Verify sort option selected.
# #
# # # #Search for the Laptop
# # # print("Input the value in search field")
# # # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # # search_box.send_keys("Laptop")
# # # print("Value Entered -----------------------------------------")
# # #
# # # #Click on Search button
# # # print("Click on Search button")
# # # search_button = driver.find_element(By.XPATH, search_btn_xpath)
# # # search_button.click()
# # # print("Clicked on Search button-------------------------------")
# # # time.sleep(2)
# # #
# # # #Click on the sort by drop down menu
# # # print("Select the sort by drop down menu")
# # # sort_products_dropdown = driver.find_element(By.XPATH, sort_products_dropdown_xpath)
# # # sort_products_dropdown.click()
# # # print("Clicked on the sort by drop down menu------------------")
# # #
# # # #Select the Low to high option
# # # print("Select the Low to High option")
# # # low_to_high_option = driver.find_element(By.XPATH, low_to_high_option_xpath)
# # # low_to_high_option.click()
# # # print("Clicked on the Low To High option----------------------")
# # # time.sleep(4)
# # #
# # # #Verify that sort option is selected
# # # print("Verify that the selected sort option is selected")
# # # selected_low_to_high_option = driver.find_element(By.XPATH, selected_low_to_high_option_xpath)
# # # assert "Price: Low to High" in selected_low_to_high_option.text
# # # print("Yes, Low to High option was selected-------------------")
# #
# #
# #
# # # Scenario 11: -----------------------------------------------------------------------------------
# # # Verify Pagination
# # # Search "Books"
# # # Scroll down.
# # # Click Next.
# # # Verify page number changes.
# #
# # # #Search for the books
# # # print("Input the value in search field")
# # # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # # search_box.send_keys("Books")
# # # print("Value Entered -----------------------------------------")
# # #
# # # #Click on Search button
# # # print("Click on Search button")
# # # search_button = driver.find_element(By.XPATH, search_btn_xpath)
# # # search_button.click()
# # # print("Clicked on Search button-------------------------------")
# # # time.sleep(2)
# # #
# # # #Scroll the page
# # # next_page_button = driver.find_element(By.XPATH, next_page_button_xpath)
# # # actions = ActionChains(driver)
# # # actions.move_to_element(next_page_button).perform()
# # # print("Page Scrolled")
# # # time.sleep(5)
# # #
# # # #Clicked on Next button
# # # next_page_button.click()
# # # print("Clicked on next page")
# # # time.sleep(5)
# # #
# # # #Scroll to bottom in 2nd page
# # # second_page_text= driver.find_element(By.XPATH, second_page_text_xpath)
# # # actions = ActionChains(driver)
# # # actions.move_to_element(second_page_text).perform()
# # # print("2 Page Scrolled")
# # # time.sleep(5)
# # #
# # # #Verify user is on second page
# # # if second_page_text.text == "2":
# # #     print("User is on Page 2")
# #
# #
# # # Scenario 12: ----------------------------------------------------------------------------------
# # # Navigate Using Browser Buttons
# # # Home
# # # Search Mobile
# # # Back
# # # Forward
# # # Refresh
# # # Verify correct pages.
# # #Search for the Mobile
# #
# print("Input the value in search field")
# search_box = driver.find_element(By.XPATH, search_box_xpath)
# search_box.send_keys("Mobile")
# print("Value Entered -----------------------------------------")
#
# #Click on Search button
# print("Click on Search button")
# search_button = driver.find_element(By.XPATH, search_btn_xpath)
# search_button.click()
# print("Clicked on Search button-------------------------------")
# time.sleep(5)
#
# #Click on Back button
# print("Clicked on back button")
# driver.back()
# print("User navigate to previous screen-----------------------")
# time.sleep(5)
#
# #Click on Forward button
# print("Clicked on Forward button")
# driver.forward()
# print("User navigate to next screen---------------------------")
# time.sleep(5)
#
# #click on Refresh button
# print("Clicked on Refresh button")
# driver.refresh()
# print("Screen Refreshed---------------------------------------")
# time.sleep(5)
# # Site was refreshed successfully
# #practice
#
# print("Taking Screenshot")
# driver.save_screenshot("screen.png")
# time.sleep(5)
# print("Screenshot saved successfully")
#
# # Closing driver
# driver.close()
#

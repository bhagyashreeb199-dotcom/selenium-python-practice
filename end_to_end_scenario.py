# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.common.by import By
#
#
# from end_to_end_scenario_xpath_file import *
#
# # Scenario 20: End-to-End Practice Scenario ⭐
# # Launch browser.
# # Open Amazon.
# # Verify home page.
# # Search "Wireless Mouse".
# # Verify results.
# # Apply Brand filter.
# # Sort by Price: Low to High.
# # Open first product.
# # Switch tab.
# # Print:Product name
# # Price
# # Rating
# #
# # Close tab.
# # Return to search results.
# # Refresh page.
# # Close browser.
#
#
# # Step 1 and 2 of launching browser and opening Amazon
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
#
#
# # Step 3 to Verify the homepage
# amazon_label = driver.find_element(By.XPATH, amazon_label_xpath)
# assert amazon_label.is_displayed() == True
# print("User is at homepage")
# time.sleep(5)
#
# #Step 4 to Search Wireless Mouse
# amazon_search_box = driver.find_element(By.XPATH, amazon_search_box_xpath)
# amazon_search_box.send_keys("Wireless Mouse")
# print("Entered Wireless Mouse value in search box")
#
# #Click on Search button
# amazon_search_button = driver.find_element(By.XPATH, amazon_search_button_xpath)
# amazon_search_button.click()
# print("Clicked on Search button")
#
# #Step 5 to Verify the Wireless Mouse results
# amazon_product_search_results = driver.find_element(By.XPATH, amazon_product_search_results_xpath)
# if (len(amazon_product_search_results.text)) > 0:
#     print("Results are showing for Wireless Mouse product")
# else:
#     print("Results are not showing for Wireless Mouse product")
#
# #Step 6 to Apply Brand filter
# amazon_brand_filter = driver.find_element(By.XPATH, amazon_brand_filter_xpath)
# amazon_brand_filter.click()
# print("Product filtered by Brand")
# time.sleep(2)
#
# #Step 7 to apply filter Sort by Price: Low to High.
# sort_by_filter = driver.find_element(By.XPATH, sort_by_filter_xpath)
# sort_by_filter.click()
# low_to_high_sort_button = driver.find_element(By.XPATH, low_to_high_sort_button_xpath)
# low_to_high_sort_button.click()
# print("Data Sort into low to high price value")
# time.sleep(2)
#
# #Step 8 to click on the first product
# open_first_product_result = driver.find_element(By.XPATH, open_first_product_result_xpath)
# open_first_product_result.click()
# print("First product is open")
# time.sleep(5)
#
# #Step 9 to Switch the tab
# #Window handles implementation for switching between tabs/windows
# all_windows = driver.window_handles
# if len(all_windows) > 1:
#     driver.switch_to.window(all_windows[1])
# time.sleep(5)
# #window_handles -> returns the unique IDs of all open browser windows or tabs
# #all_window[0] = 1st tab
# #all_window[1] = 2nd tab
# # len() returns the total number of tabs.
# #driver.switch_to.window(all_windows[1]) = Move from the current tab to the second tab.
# #if second tab is not available then Selenium through error - IndexError: list index out of range
#
# #Step 10 to Print:Product name, Price and Rating
# title_of_the_product_result = driver.find_element(By.XPATH, title_of_the_product_result_xpath)
# print("Title of the product is :- ")
# print(title_of_the_product_result.text)
# print("---------------")
#
# price_of_the_product_result = driver.find_element(By.XPATH, price_of_the_product_result_xpath)
# print("Price of the product is :- ")
# print(price_of_the_product_result.text)
# print("---------------")
#
# rating_of_the_product_result = driver.find_element(By.XPATH, rating_of_the_product_result_xpath)
# print("Rating of the product is :- ")
# print(rating_of_the_product_result.text)
# print("---------------")
#
# # Step 11 to close tab and return to default window
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(all_windows[0])
# print("Returned to the default window")
# #driver.window_handles -> returns all open tabs.
#
# # Step 12 to Refresh window
# driver.refresh()
# time.sleep(5)
#
#
# driver.close()
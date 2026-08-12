# import time
# from itertools import count
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# from amazon_india_site_functions_file import *
# from selenium.webdriver.support.ui import Select
# from amazon_india_site_automation_xpath import *
#
# driver = webdriver.Chrome()
# def launch_amazon_site():
#      print("Task - launch browser, load the site and maximize the window")
#      driver.get("https://www.amazon.in/")
#      driver.maximize_window()
#      driver.implicitly_wait(5)
#      print("Done - Browser launched, site loaded and and maximized the site")
#
# #SCENARIO FIRST ---------------------------------------------------------
# # Check if the user landes to Amazon home page
# # print("Task - Check if user lands on Amazon site home page")
# # expected_label = "Amazon.in"
# # actual_label_xpath = "//*[@aria-label='Amazon.in']"
# # actual_label = driver.find_element(By.XPATH, actual_label_xpath)
# # assert actual_label.is_displayed() == True
# # print("Done - Yes user landed to Amazon site home page")
#
# # # Check the Search box is visible
# # print("Task - Verify search box is displayed")
# # search_box_xpath = "//*[@id='twotabsearchtextbox']"
# # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # assert search_box.is_displayed() == True
# # print("Done - Search box is visible")
#
# # # Check the "ALl" category drop down
# # print("Task - Verify the All category drop down is visible")
# # all_drop_down_xpath = "//*[@class='hm-icon nav-sprite']"
# # all_drop_down = driver.find_element(By.XPATH, all_drop_down_xpath)
# # assert all_drop_down.is_displayed() == True
# # print("Done - All category drop down is visible")
#
#
# #SCENARIO SECOND -------------------------------------------------------------------------------
#
# #Open the Amazon site
# # launch_amazon_site()
# #
# # #Enter "Laptop" in search box
# # print("Enter Laptop in search box")
# # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # search_box.send_keys("Laptop")
# # print("Value 'Laptop' is added in search box")
# #
# # #Click on Search button
# # print("Click on Search button")
# # search_button = driver.find_element(By.XPATH, search_btn_xpath)
# # search_button.click()
# # driver.implicitly_wait(5)
# # print("Clicked on Search button")
# #
# #
# # #Check user navigates to laptop search result
# # print("Verify user navigates to Laptop search result")
# # if "Laptop" in driver.current_url:
# #     print("User is on laptop search result")
# # else:
# #     print("User is not on laptop search result")
# #
# #
# # #Check if URL contains s?k=Laptop
# # print("Verify if URL contains s?k=Laptop")
# # if driver.current_url.__contains__("s?k=Laptop"):
# #     print("YES.... URL contains s?k=Laptop")
# # else:
# #     print("NO.... URL doesn't contains s?k=Laptop")
# # time.sleep(10)
# #
# #
# # #Check if screen is displaying at least one product
# # print("Verify at least one product of screen")
# # result_text = driver.find_element(By.XPATH, result_text_xpath)
# # products =driver.find_elements(By.XPATH, products_xpath)
# # if (len(products)) >= 1:
# #     print("Yes, there are products on the page")
# # else:
# #     print("No, there are no products on the page")
#
#
# # # S E C O N D       S C E N A R I O        POINT 6 PART B
# # #Check no result message should show on invalid input
# #
# # #Clearning search box
# # print("Clearing the Search box")
# # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # search_box.clear()
# # print("Search box has been cleared")
# #
# # # Enter invalid input
# # print("Entering invalid input")
# # search_box.send_keys("///asdf/f/w/23/r/32v08710fy'1")
# #
# # print("Entered ///asdf/f/w/23/r/32v08710fy'1 in search box")
# # # clicking on search button
# # print("Clicking on Search button")
# # search_button = driver.find_element(By.XPATH, search_btn_xpath)
# # search_button.click()
# # print("Clicked on search button")
# #
# # #Checking if page shows No result found on invalid input
# # no_result_found = driver.find_element(By.XPATH, no_result_found_xpath)
# # print(no_result_found.text)
# # if "No results for your search query." in no_result_found.text:
# #     print("Error message found on screen - No results for your search query.")
# # else:
# #     print("Error message not found on screen")
# # time.sleep(5)
#
# #T H I R D     S C E N A R I O ------------------------------------------------------------------
# # Search multiple products through loop
#
# #Open and load the side
# # print("Amazon site loaded")
# # launch_amazon_site()
# #
# # search_product_list = ["Laptop", "Mobile", "Shoes", "watch", "Headphones"]
# #
# # for product in search_product_list:
# #     search_products(driver, product)
# #     # Check if search data is showing result
# #     print("Check if result are showing")
# #     product_count = driver.find_elements(By.XPATH, products_xpath)
# #     if (len(product_count)) > 0:
# #         print("Products are showing")
# #     # clearing search box
# #     print("Clearing search box")
# #     search_box = driver.find_element(By.XPATH, search_box_xpath)
# #     search_box.clear()
#
#
# #SCENARIO FIFTH ---------------------------------------------------------------------------------
# # Select category "Books".
# # Search "Python".
# # Verify selected category remains "Books".
# # Practice:
# # Select class
# # Dropdown handling
# # # Call the site and load it
# # launch_amazon_site()
#
#
# # # Select book category
# # print("select book category")
# # categories_selection = Select(driver.find_element(By.XPATH, categories_dropdown_xpath))
# # categories_selection.select_by_visible_text("Books")  #selecting the value through .visible text
# # categories_selection.select_by_value("search-alias=stripbooks")  # can also use the value attribute and if value attribute is not available we can use indexing also
# # print("Book category is selected and visible")
# # time.sleep(10)
#
# # Scenario 6: ----------------------------------------------------------------------------
# # Verify Search Result Count
# # Search "Mouse"
# # Count number of visible products.
# # Print total count.
# # Practice:
# # find_elements()
#
#
# #launch the site
# # launch_amazon_site()
# #
# # #add value Mouse in Search field
# # print("Insert Mouse")
# # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # search_box.send_keys("Mouse")
# # print("Mouse added in search box")
# #
# # #click on search button
# # print("click on search button")
# # search_button = driver.find_element(By.XPATH, search_btn_xpath)
# # search_button.click()
# # print("Searched button clicked")
# #
# # #Count and print total visible products
# # visible_mouse_product = driver.find_elements(By.XPATH, total_visible_product_mouse)
# # print("Counts of visible product for Mouse ")
# # print(len(visible_mouse_product))
#
#
# # Scenario 7: ---------------------------------------------------------------------------
# # Search "Keyboard"
# # Click first product.
# # Switch to new tab.
# # Verify product title exists.
# # Print product title.
# # Practice:
# # Window handling
#
# #Launch the site
# # print("Amazon site launch")
# # launch_amazon_site()
# #
# # #Input Keyboard in Search field
# # print("Enter Keyboard in search field")
# # search_box = driver.find_element(By.XPATH, search_box_xpath)
# # search_box.send_keys("Keyboard")
# # print("Data Entered")
# #
# # #Click on Search button
# # print("click on Search button")
# # search_button = driver.find_element(By.XPATH, search_btn_xpath)
# # search_button.click()
# # print("Click on Search button")
# #
# # #Click on first product
# # print("Click on the first product")
# # keyboard_result_first_product = driver.find_element(By.XPATH, keyboard_result_first_product_xpath)
# # keyboard_result_first_product.click()
# # print("First product selected")
# # time.sleep(10)
# #
# # #Switch to another window
# # all_windows = driver.window_handles
# #
# # if len(all_windows) > 1:
# #     driver.switch_to.window(all_windows[1])
# # else:
# #     print("Product opened in the same window")
# #
# # first_result_title = driver.find_element(By.XPATH, first_result_title_xpath)
# # print("Title of the product is:-")
# # print(first_result_title.text)
# # print(driver.title)
# # time.sleep(2)
#
#
# # Scenario 8: -----------------------------------------------------------------------------------
# # Verify Product Price
# # Search "Headphones"
# # Open first product.
# # Print:Product name
# # Price
# # Rating
#
# #Launch the amazon site
# print("Launch the amazon site")
# launch_amazon_site()
# print("Amazon site launched -----------------------")
#
# #Search for headphones
# print("Input the value in search field")
# search_box = driver.find_element(By.XPATH, search_box_xpath)
# search_box.send_keys("Headphones")
# print("Value Entered --------------------------")
#
# #Click on Search button
# print("Click on Search button")
# search_button = driver.find_element(By.XPATH, search_btn_xpath)
# search_button.click()
# print("Clicked on Search button-------------------------------")
# time.sleep(5)
#
# # #Open the first product
# # print("Select the first product")
# # open_the_first_product = driver.find_element(By.XPATH, open_the_first_product_xpath)
# # open_the_first_product.click()
# # print("First product selected----------------------")
# # time.sleep(30)
# #
# # # Navigate to the next tab
# # # Window handles implementation for switching between tabs/windows
# # all_windows = driver.window_handles
# # if len(all_windows) > 1:
# #     driver.switch_to.window(all_windows[1])
# #
# # #Print the Product name, Price
# # heading_of_the_product = driver.find_element(By.XPATH, heading_of_the_product_xpath)
# # print("Print the Product name")
# # print(heading_of_the_product.text)
# #
# #
# # price_of_first_product = driver.find_element(By.XPATH, price_of_first_product_xpath)
# # print("Print the Product Price")
# # print(price_of_first_product.text)
#
# #Open the first product
# print("Select the first product")
# open_the_first_product = driver.find_element(By.XPATH, open_the_first_product_xpath)
# #Storing Title into variable
# before_clicking_product_heading = driver.find_element(By.XPATH, before_clicking_product_heading_xpath)
# expected_title_text = before_clicking_product_heading.text
# #Storing Price into variable
# before_clicking_product_price = driver.find_element(By.XPATH, before_clicking_product_price_xpath)
# expected_price_text = before_clicking_product_price.text
# open_the_first_product.click()
# print("First product selected----------------------")
# time.sleep(10)
#
# #Navigate to the next tab
# #Window handles implementation for switching between tabs/windows
# all_windows = driver.window_handles
# if len(all_windows) > 1:
#     driver.switch_to.window(all_windows[1])
#
#
# # After navigating to new tab
# #Storing Actual title into variable
# heading_of_the_product = driver.find_element(By.XPATH, heading_of_the_product_xpath)
# actual_title_text = heading_of_the_product.text
# price_of_first_product = driver.find_element(By.XPATH, price_of_first_product_xpath)
# actual_price_text = price_of_first_product.text
#
# #Close the 2nd tab on which the product description page open after clicking
# driver.switch_to.window(driver.window_handles[1])
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(5)
#
# #Verify the title and Price text are same before and after clicking the product
# assert expected_title_text == actual_title_text
# print("TITLE MATCHED........")
# assert expected_price_text == actual_price_text
# print("PRICE MATCHED........")
#
#
# driver.close()
#
#
#
#
#
#
#
#

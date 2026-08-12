import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
#jab bhi get method call hota h to ja tak pura page load ni hota tab tak
#driver wait karta h and code bhi vahi ruka rehta h, code run ni hota


#login_credentials for site
def login_in_site(driver, username, password):
    driver.find_element(By.XPATH,"//input[@id='userEmail']").send_keys(username)
    driver.find_element(By.XPATH,"//input[@id='userPassword']").send_keys(password)
    login_button = driver.find_element(By.XPATH, "//input[@id='login']")
    login_button.click()
    time.sleep(5)

    if "dashboard" in driver.current_url:
        print("Site launched successfully......")
    else:
        print("Site launched failed......")

login_in_site(driver, "bhagyashree3@example.com","Rahul@1234")
time.sleep(2)


#sign_out
# sign_out_button = driver.find_element(By.XPATH," //*[@class='btn btn-custom' and text() = ' Sign Out ']")
# sign_out_button.click()
# time.sleep(5)
#
# #forgot_password
# forgot_password = driver.find_element(By.XPATH,"//*[@class='forgot-password-link']")
# forgot_password.click()
# time.sleep(5)
#
# driver.back()
# time.sleep(5)


# Search button selection
print("Task - Value in Search field")
search_button_xpath = "(//input[@name='search' and @type='text'])[2]"
search_button = driver.find_element(By.XPATH, search_button_xpath)
search_button.send_keys("ADIDAS ORIGINAL")
print("Done - Value added in search field")

# Set Minimum price range
print("Task - Setting minimum price range")
minimum_price_range_xpath = "(//input[@placeholder='Min Price'])[2]"
minimum_price = driver.find_element(By.XPATH, minimum_price_range_xpath)
minimum_price.send_keys("6000")
print("Done - Minimum price range set")

# Set Maximum price range
print("Task - Setting maximum price range")
maximum_price_range_xpath = "(//input[@placeholder='Max Price'])[2]"
maximum_price = driver.find_element(By.XPATH, maximum_price_range_xpath)
maximum_price.send_keys("15000")
print("Done - Maximum price range set")
time.sleep(5)

# Clear the Search filed
print("Task - Clear the search filed")
search_button.clear()
print("Done - Searched filed cleared")

# Clear the minimum and maximum range field and refresh the site
print("Task - Clear minimum and maximum price range field and refresh the page")
minimum_price.clear()
maximum_price.clear()
driver.refresh()
print("Done = minimum and max. price range field is cleared and site is refreshed")
time.sleep(5)

# View the product
print("Task - View the product")
view_product_xpath = "(//button[@class='btn w-40 rounded'])[1]"
view_product = driver.find_element(By.XPATH, view_product_xpath)
view_product.click()
print("Done - Viewed product")
time.sleep(5)







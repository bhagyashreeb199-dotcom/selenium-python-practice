import time

from selenium import webdriver
from amazon_homepage import AmazonHomepage

def test_search_product():

    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    time.sleep(5)
    amazon_homepage = AmazonHomepage(driver)
    amazon_homepage.search_products("Wireless Mouse")
    assert amazon_homepage.verify_logo() == True
    print("Verifying Logo")
    time.sleep(2)

    driver.quit()

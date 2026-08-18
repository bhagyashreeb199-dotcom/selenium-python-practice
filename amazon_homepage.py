from selenium.webdriver.common.by import By

class AmazonHomepage:

    SEARCH_BOX = (By.XPATH, "//input[@placeholder='Search Amazon.in']")

    def __init__(self, driver):
        self.driver = driver

    def search_products(self, product_name):
        self.driver.find_element(*self.SEARCH_BOX).send_keys(product_name)


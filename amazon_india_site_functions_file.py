import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
#from amazon_india_site_automation import driver
#from amazon_india_site_automation import launch_amazon_site
from amazon_india_site_automation_xpath import search_box_xpath, search_btn_xpath


#Lunch of the site
def launch_the_amazon_site(driver):
    print("Task - launch browser, load the site and maximize the window")
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    print("Done - Browser launched, site loaded and and maximized the site")

#Entering the input in search box
def search_products(driver, product_name):
    search_box = driver.find_element(By.XPATH, search_box_xpath)
    print("Enter data in search button")
    search_box.send_keys(product_name)
    print("Data is added to search box")
    print("Click search button")
    search_button = driver.find_element(By.XPATH, search_btn_xpath)
    search_button.click()
    print("Clicked on search button")
    time.sleep(5)






    driver.close()

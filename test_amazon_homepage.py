import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_amazon_homepage(driver):
    print("Amazon test is running")

def test_amazon_home_page(driver):
    print("Amazon homepage test")

def test_amazon_search(driver):
    print("Amazon search test")

def test_number(driver):
    a=10
    b=10
    assert a==b


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    time.sleep(5)
    yield driver
    driver.quit()

def test_amazon_title(driver):
    assert "Amazon" in driver.title




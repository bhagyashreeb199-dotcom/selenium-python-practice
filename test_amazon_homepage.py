import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_amazon_homepage():
    print("Amazon test is running")

def test_amazon_home_page():
    print("Amazon homepage test")

def test_amazon_search():
    print("Amazon search test")

def test_number():
    a=10
    b=10
    assert a==b

def test_amazon_title():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/")
    time.sleep(5)
    actual_title = driver.title
    expected_title = "Amazon.in"
    assert expected_title in actual_title

# Your exercise
# Use your existing test_amazon_homepage.py.
# Create a setup() function that:
# 1. Opens Chrome.
# 2. Maximizes it.
# 3. Opens Amazon.
# 4. Returns the driver.
# Then create this test:
# def test_amazon_title():
# Inside it:
# 1. Get the driver from setup().
# 2. Get the page title.
# 3. Verify "Amazon.in" exists in the title.
# 4. Close the browser.
# Don't use:
# @pytest.fixture
# yet.
# Don't create conftest.py yet.
# We're intentionally keeping this exercise focused on understanding Setup.





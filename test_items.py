import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, 'Button not found!'
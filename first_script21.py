from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
house = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
button2 = browser.find_element(By.CSS_SELECTOR, "#book")
button2.click()
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)
button3 = browser.find_element(By.CSS_SELECTOR, "#solve")
button3.click()
time.sleep(10)
browser.quit()
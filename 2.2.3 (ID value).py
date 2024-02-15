from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x, y):
  return x + y

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID,'num1').text
    y = browser.find_element(By.ID,'num2').text

    sum = calc(int(x),int(y))

    select = Select(browser.find_element(By.TAG_NAME,'select'))
    select.select_by_value(str(sum))
    print(sum)
#     x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
#     x = x_element.get_attribute('valuex')
#     y = calc(x)
#
#     answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer_input.send_keys(str(y))
#
#     rob_check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     rob_check.click()
#
#     rob_rad = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     rob_rad.click()
#
    butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    butt.click()
#
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
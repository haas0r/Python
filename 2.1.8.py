from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)



    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute('valuex')
    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(str(y))

    rob_check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    rob_check.click()

    rob_rad = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rob_rad.click()

    butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    butt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
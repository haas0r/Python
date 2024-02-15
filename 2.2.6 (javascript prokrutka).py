from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(str(y))
    butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    browser.execute_script("return arguments[0].scrollIntoView(true);", butt)
    rob_check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    rob_check.click()

    rob_rad = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    rob_rad.click()


    butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", butt)
    butt.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
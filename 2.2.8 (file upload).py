from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text_req = browser.find_elements(By.CSS_SELECTOR,'[type="text"]')

    for element in text_req:
        element.send_keys('Тест ' + str(datetime.datetime.now()))

    cur_dir = os.path.abspath(os.path.dirname(__file__))
    file_dir = os.path.join(cur_dir, 'file.txt')
    print(file_dir)

    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_dir)

    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
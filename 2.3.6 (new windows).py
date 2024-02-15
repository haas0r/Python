from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, 'button').click()

    # Переключение на новую вкладку
    new_windows = browser.window_handles[1]
    browser.switch_to.window(new_windows)
    # Переключение на новую вкладку



    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)


    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(str(y))


    butt = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    butt.click()

    print(browser.switch_to.alert.text) #вывод ответа из алерта в консоль

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
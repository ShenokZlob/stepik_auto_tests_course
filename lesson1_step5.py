import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    #1. Находим тег с числом 2. Записываем текст тега в переменную 3. Считаем
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    xx = calc(x)

    otvet = browser.find_element_by_id("answer")
    otvet.send_keys(xx)
    
    checkbox = browser.find_element_by_id("robotCheckbox") 
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule") 
    radio.click()
    knopka = browser.find_element_by_css_selector("button")
    knopka.click()
    
finally:
    time.sleep(10)
    browser.quit()
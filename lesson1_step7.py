import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    chest = browser.find_element_by_id("treasure")
    chest_value = chest.get_attribute("valuex")
    
    x = calc(chest_value)     
    
    otvet = browser.find_element_by_id("answer")
    otvet.send_keys(x)
    
    checkbox = browser.find_element_by_id("robotCheckbox") 
    checkbox.click()
    radio = browser.find_element_by_id("robotsRule") 
    radio.click()
    knopka = browser.find_element_by_css_selector("button")
    knopka.click()
    
finally:
    time.sleep(4)
    browser.quit()
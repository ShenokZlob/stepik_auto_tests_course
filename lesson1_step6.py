import math
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    
    people_radio = browser.find_element_by_id("peopleRule")
    
    people_checked = people_radio.get_attribute("radio")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
finally:
    time.sleep(5)
    browser.quit()
#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user = ''
pas = ''

driver = webdriver.Firefox(executable_path="/home/divyangb/Desktop/work/selenium/geckodriver")
driver.get('https://www.facebook.com/')
assert "Facebook" in driver.title
elem=driver.find_element_by_id("email")
elem.send_keys(user)
elem=driver.find_element_by_id("pass")
elem.send_keys(pas)
elem.send_keys(Keys.RETURN)

time.sleep(100)
driver.close()
driver.quit()

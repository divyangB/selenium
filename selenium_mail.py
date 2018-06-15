#!/usr/bin/python3

#importing libraries
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# account credentials
user = ''
pas = ''

# opening the web browser
driver = webdriver.Firefox(executable_path="/home/divyangb/Desktop/work/selenium/geckodriver")
# opening the page
driver.get('https://www.gmail.com')
# for the title bar
assert "Gmail" in driver.title
# input the email by id
elem=driver.find_element_by_id("identifierId")
elem.send_keys(user)
# clicking on the 'Next' button by id
elem=driver.find_element_by_id("identifierNext").click()
time.sleep(3)

# finding the password by the xpath
elem=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/content/form/div[1]/div/div[1]/div/div[1]/input")
elem.send_keys(pas)
# clicking on the 'Next' button using xpath
elem=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/content/span").click()
#elem.send_keys(Keys.RETURN)

time.sleep(100)
driver.close()
driver.quit()

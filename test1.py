#!/usr/bin/python3

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path="/home/divyangb/Desktop/work/selenium/geckodriver")
#taking input from user
city = input("Enter your city: ")
browser.get("https://openweathermap.org/find?q="+city)
#city = input("Enter your city: ")
#assert India-Weather in browser.title
elem = browser.find_element_by_xpath("/html/body/main/div[4]/div/div/div/div/table/tbody/tr[1]/td[2]/b[1]/a").click()

time.sleep(100)
browser.close()
browser.quit()

("/html/body/div[1]/div[9]/section[1]/div/div[2]/div[3]")



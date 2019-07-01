from selenium import webdriver
import time
import math
import os


link = 'http://suninjuly.github.io/cats.html'
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

browser.find_element_by_id("button")

alert = browser.switch_to.alert
print(alert.text)
browser.quit()

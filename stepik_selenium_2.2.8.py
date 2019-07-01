from selenium import webdriver
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/file_input.html'
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

first_name = browser.find_element_by_xpath('//input[@name="firstname"]')
first_name.send_keys('Sergey')
last_name = browser.find_element_by_xpath('//input[@name="lastname"]')
last_name.send_keys('Streltsov')
e_mail = browser.find_element_by_xpath('//input[@name="email"]')
e_mail.send_keys('test@microsofy.com')
file_path = '/home/mantikor/stepik_selenium/geckodriver.txt'
first_name = browser.find_element_by_xpath('//input[@name="file"]')
first_name.send_keys(file_path)

button = browser.find_element_by_xpath('//button[@type="submit"]')
button.click()
alert = browser.switch_to.alert
print(alert.text)
browser.quit()

from selenium import webdriver
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

button = browser.find_element_by_xpath('//button[@type="submit"]')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x = browser.find_element_by_xpath('//span[@id="input_value"]').text
y = calc(x)
answer = browser.find_element_by_xpath('//input[@id="answer"]')
answer.send_keys(y)

button = browser.find_element_by_xpath('//button[@type="submit"]')
button.click()
alert = browser.switch_to.alert
print(alert.text)
browser.quit()

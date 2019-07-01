import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

button = browser.find_element_by_xpath('//button[@id="book"]')
ok_price = WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR"))
button.click()

x = browser.find_element_by_xpath('//span[@id="input_value"]').text
y = calc(x)
answer = browser.find_element_by_xpath('//input[@id="answer"]')
answer.send_keys(y)

button = browser.find_element_by_xpath('//button[@type="submit"]')
button.click()
alert = browser.switch_to.alert
print(alert.text)
browser.quit()

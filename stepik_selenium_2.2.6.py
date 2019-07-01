from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/execute_script.html'
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
x = x_element.text
y = calc(x)
input_element = browser.find_element_by_xpath('//input[@id="answer"]')
input_element.send_keys(y)

button = browser.find_element_by_xpath('//button[@type="submit"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
robot_checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
robot_checkbox.click()
robot_radio = browser.find_element_by_xpath('//input[@id="robotsRule"]')
robot_radio.click()

button.click()
alert = browser.switch_to.alert
print(alert.text)
browser.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


# link = 'http://suninjuly.github.io/selects1.html'
link = 'http://suninjuly.github.io/selects2.html'
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

num1 = browser.find_element_by_xpath('//span[@id="num1"]').text
num2 = browser.find_element_by_xpath('//span[@id="num2"]').text
y = sum([int(num1), int(num2)])

select = Select(browser.find_element_by_tag_name('select'))
select.select_by_value(str(y))

button = browser.find_element_by_xpath('//button[@type="submit"]')
button.click()
alert = browser.switch_to.alert
print(alert.text)
browser.quit()

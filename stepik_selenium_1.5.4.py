import math
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
ok_link = browser.find_element_by_link_text(link_text=link_text)
ok_link.click()

input1 = browser.find_element_by_tag_name('input')
input1.send_keys("Ivan")
input2 = browser.find_element_by_name('last_name')
input2.send_keys("Petrov")
input3 = browser.find_element_by_class_name('city')
input3.send_keys("Smolensk")
input4 = browser.find_element_by_id('country')
input4.send_keys("Russia")
button = browser.find_element_by_css_selector("button.btn")
button.click()
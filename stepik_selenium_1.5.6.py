import math
from selenium import webdriver

chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get("http://suninjuly.github.io/huge_form.html")
elements = browser.find_elements_by_tag_name('input')
for element in elements:
    element.send_keys("Мой ответ")

button = browser.find_element_by_css_selector("button.btn")
button.click()
alert = browser.switch_to.alert
print(alert.text)
browser.quit()

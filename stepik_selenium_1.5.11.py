from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

Name=browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control first']")
Name.send_keys("KKK")
Sername=browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
Sername.send_keys("KKK")
Email=browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control third']")
Email.send_keys("KKK")



button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(3)


welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
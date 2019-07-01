import math
import time
from selenium import webdriver

# link = 'http://suninjuly.github.io/registration1.html'
link = 'http://suninjuly.github.io/registration2.html'
chrome_d_path = '/opt/Chrome/chromedriver'
browser = webdriver.Chrome(executable_path=chrome_d_path)
browser.get(link)

# Ваш код, который заполняет обязательные поля
input_f_name = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group first_class"]/input[@class="form-control first"]')
input_f_name.send_keys('Sergey')
input_l_name = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group second_class"]/input[@class="form-control second"]')
input_l_name.send_keys('Streltsov')
input_e_mail = browser.find_element_by_xpath('//div[@class="first_block"]/div[@class="form-group third_class"]/input[@class="form-control third"]')
input_e_mail.send_keys('test@microsoft.com')

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text

# alert = browser.switch_to.alert
# print(alert.text)
# browser.quit()

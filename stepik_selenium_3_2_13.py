import math
import time
from selenium import webdriver
import unittest


class TestPage(unittest.TestCase):
    def test_page1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        chrome_d_path = '/opt/Chrome/chromedriver'
        browser = webdriver.Chrome(executable_path=chrome_d_path)
        browser.get(link)
        input_f_name = browser.find_element_by_css_selector(".first_block .first")
        input_f_name.send_keys('Sergey')
        input_l_name = browser.find_element_by_css_selector(".first_block .second")
        input_l_name.send_keys('Streltsov')
        input_e_mail = browser.find_element_by_css_selector(".first_block .third")
        input_e_mail.send_keys('test@microsoft.com')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Поздравляем! Вы успешно зарегистировались!', 'Error in TestPage1')

    def test_page2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        chrome_d_path = '/opt/Chrome/chromedriver'
        browser = webdriver.Chrome(executable_path=chrome_d_path)
        browser.get(link)
        input_f_name = browser.find_element_by_css_selector(".first_block .first")
        input_f_name.send_keys('Sergey')
        input_l_name = browser.find_element_by_css_selector(".first_block .second")
        input_l_name.send_keys('Streltsov')
        input_e_mail = browser.find_element_by_css_selector(".first_block .third")
        input_e_mail.send_keys('test@microsoft.com')
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, 'Поздравляем! Вы успешно зарегистировались!', 'Error in TestPage2')


if __name__ == "__main__":
    unittest.main()

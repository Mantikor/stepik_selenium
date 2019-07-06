import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_d_path = '/opt/Chrome/chromedriver'
    browser = webdriver.Chrome(executable_path=chrome_d_path)
    browser.implicitly_wait(30)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    text_area = browser.find_element_by_xpath('//textarea')
    answer = math.log(int(time.time()))
    text_area.send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector('.submit-submission')
    submit_button.click()
    check_answer = browser.find_element_by_xpath('//pre[@class="smart-hints__hint"]').text
    assert check_answer == 'Correct!'

import pytest
import time
import math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    text_area = browser.find_element_by_css_selector('#ember1600')
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)
    submit_button = browser.find_element_by_css_selector('.submit-submission')
    submit_button.click()
    check_answer = browser.find_element_by_css_selector('#ember1674').text
    assert check_answer == 'Correct!'

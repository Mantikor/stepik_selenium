import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language for content - en, ru, es, fr...")


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': language})
    # chrome_d_path = '/opt/Chrome/chromedriver'
    browser = webdriver.Chrome(options=chrome_options)  #, executable_path=chrome_d_path)
    print('Language is: {}'.format(language))
    yield browser
    print('\nquit browser...')
    browser.quit()

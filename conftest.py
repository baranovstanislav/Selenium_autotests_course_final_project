import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language") 


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)        
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)        
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    time.sleep(0)
    browser.quit()
    
@pytest.fixture
def generate_password():
    length = 9
    digits =  '23456789'
    lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    chars = digits + lowercase_letters + uppercase_letters + punctuation
    password = ''.join([random.choice(chars) for i in range(length)])
    return password

@pytest.fixture
def generate_email():
    email = str(time.time()) + "@fakemail.org"
    return email
from time import time
import pytest
import time
from selenium import webdriver

#driver = webdriver.Chrome()
#@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    Link="https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/"
    time.sleep(2)
    driver.get(Link)
    yield driver
    driver.quit()
        #driver.quit()

browser()


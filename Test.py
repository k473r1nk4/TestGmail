from LogPage import Login
from selenium import webdriver
import time
import os
#import LogPage

def test_attach_file(browser):
    main_page=Login(browser)
    main_page.go_to_site()
    main_page.enter_login('testovpolzovat1.1@gmail.com')
    main_page.click_on_the_button()

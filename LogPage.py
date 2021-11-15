#from test import Driver
from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

class Locators:
    LOCATOR_GMAIL_LOGIN_AREA = (By.CLASS_NAME,"identifier")
    LOCATOR_GMAIL_LOGIN_BUTTON = (By.CSS_SELECTOR,"button.VfPpkd-LgbsSe")

class Login(BasePage):

    def enter_login(self, login):
        login_area = self.find_element(Locators.LOCATOR_GMAIL_LOGIN_AREA)
        login_area.click()
        login_area.send_keys(login)
        return login_area

    def click_on_the_button(self):
        return self.find_element(Locators.LOCATOR_GMAIL_LOGIN_BUTTON,time=2).click()
    
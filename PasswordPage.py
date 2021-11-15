#from Application.App import Driver
from selenium import webdriver
import time
import os

class PasswordPage:
    def PasswordArea(self):
        self.Driver.find_element_by_name("password")
    def Button(self):
        submit_button = self.Driver.find_element_by_css_selector("button.VfPpkd-LgbsSe")
        submit_button.click()
        
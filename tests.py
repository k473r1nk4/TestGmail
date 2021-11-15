from conftest import Browser
import json
import re
import urllib.parse
from selenium import webdriver
import time
import os
import LogPage

File=open("date.txt","r")
SubjectToMail=File.readline().replace("\n", "")
BodyMail=File.readline().replace("\n", "")
PathFile=File.readline().replace("\n", "")
File = open("log1.txt","r")
LoginFirst=File.readline().replace("\n","")
PasswordFirst=File.readline().replace("\n","")
File = open("log2.txt","r")
LoginSecond=File.readline().replace("\n","")
PasswordSecond=File.readline().replace("\n","")

def Autorisation(login, password):
    LogPage.Login.enter_login(Driver, login)
    LogPage.Login.click_on_the_button()

    PasswordArea= Driver.find_element_by_name("password")
    PasswordArea.send_keys(password)
    #Driver.set_page_load_timeout(30)#time.sleep(2)

    submit_button = Driver.find_element_by_css_selector("button.VfPpkd-LgbsSe")
    submit_button.click()
    #Driver.set_page_load_timeout(30)

    time.sleep(7)

def FillLatterAndSend( to, subject, body, fileIn):
    To = Driver.find_element_by_css_selector(".eV>.oj .vO")
    To.send_keys(to)

    Subject = Driver.find_element_by_css_selector(".aoT")
    Subject.send_keys(subject)

    LetterBody = Driver.find_element_by_css_selector(".aoI .Am.Al")
    LetterBody.send_keys(body)

    FileInput = Driver.find_element_by_css_selector("input[type=file]")
    FileInput.send_keys(fileIn)
    time.sleep(5)

    Send = Driver.find_element_by_css_selector(".btA .aoO")
    Send.click()

    time.sleep(3)
def Out():
    Driver.get("https://accounts.google.com/Logout?hl=ru&continue=https://mail.google.com/mail&service=mail&timeStmp=1614707093&secTok=.AG5fkS-nezExemFRLoLaoCP449zXWWxQrw&ec=GAdAFw")

Driver = webdriver.Chrome()
try:
    #Link= "https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/"
    #time.sleep(2)
    #Driver.get(Link)
    #time.sleep(2)
    Browser.browser(Driver)

    Autorisation(LoginFirst, PasswordFirst)
    Write=Driver.find_element_by_css_selector(".z0 .T-I")
    Write.click()

    FillLatterAndSend(LoginSecond, SubjectToMail, BodyMail, PathFile)
    Out()
    time.sleep(3)
    
    New = Driver.find_element_by_css_selector(".UXurCe")
    New.click()
    time.sleep(2)
    Autorisation(LoginSecond, PasswordSecond)
    time.sleep(7)
    
    mail = Driver.find_element_by_css_selector('td[role=gridcell]')
    mail.click()
    time.sleep(3)
    subject = Driver.find_element_by_css_selector(".ha>.hP").text
    #print(subject)
    if subject == SubjectToMail:
        print("Subject success")
    else:
        print("sad")
    time.sleep(3)
    body = Driver.find_element_by_css_selector('.a3s').text
    #print(body)
    if body == BodyMail:
        print("Body success")
    else:
        print("sad")
    button = Driver.find_element_by_css_selector('.akn')
    button.click()

    path= Driver.find_element_by_css_selector(".aV3").text
    time.sleep(15)
    fileOp="C:\\Users\\Katya\\Downloads\\"+path
    if open(fileOp).read() == open(PathFile).read():
        print("File success")
    else:
        print("sad")

    time.sleep(1)
    os.remove(fileOp)
finally:
    Driver.quit()
    
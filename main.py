from selenium import webdriver
import time
import json
from pprint import pprint

browser = webdriver.Chrome("chromedriver.exe")

with open('info.json', 'r') as f:
    info = json.load(f)
    email = info['email']
    password = info['password']
    url = info['url']
    url2 = info['url2']

def login():
    browser.get(url)
    time.sleep(0.5)
    browser.find_element_by_id('user_login').send_keys(email)
    browser.find_element_by_id('user_pass').send_keys(password)
    browser.find_element_by_id('wp-submit').submit()
    remover()

def remover():
    page = 1
    while page < 96:
        browser.get(url2)
        browser.find_element_by_xpath('//*[@id="duplicate_entry_all_apply"]').click()
        page += 1


login()
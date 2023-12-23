import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_element(By.CLASS_NAME, 'form').send_keys('Text')
    time.sleep(5)
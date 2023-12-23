import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService

with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
    driver.get("https://donrobot.ru")
    time.sleep(5)


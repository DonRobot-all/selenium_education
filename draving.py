
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://sketch.io/sketchpad/")
time.sleep(15)
actions = ActionChains(driver)
actions.move_by_offset(500, 500).perform()
ActionChains(driver).click_and_hold().move_by_offset(100, 100).release().perform()
for i in range(10):
    for a in range(10):
        ActionChains(driver).click_and_hold().move_by_offset(i, a).perform()

time.sleep(10000)

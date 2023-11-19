from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

print("Testing Started")
driver.get("http://127.0.0.1:8000/n/login")
driver.find_element("id", "email").send_keys("malavika")
time.sleep(1)
driver.find_element("id", "password").send_keys("malavika")
time.sleep(1)
driver.find_element("xpath", "/html/body/div/div/form/center/input").click()
time.sleep(1)
search_box = driver.find_element("id", "search-box")
search_box.send_keys("sajo")
search_box.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div/div/div[2]/div/div/div/div/div[1]/center/a/div").click()
time.sleep(1)

if driver.current_url == 'http://127.0.0.1:8000/sajo':
    print("Searching successful")
else:
    print('Searching failed')

print("Search Testing Passed")

driver.quit()
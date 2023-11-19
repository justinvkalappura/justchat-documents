from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

print("Testing Started")
options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("http://127.0.0.1:8000/n/login")
driver.find_element("id", "email").send_keys("malavika")
time.sleep(1)
driver.find_element("id", "password").send_keys("malavika")
time.sleep(1)
driver.find_element("xpath", "/html/body/div/div/form/center/input").click()
time.sleep(1)
driver.find_element("xpath", "/html/body/div[2]/div[3]/div/div[2]/div[2]/div[3]/button").click()
time.sleep(1)
driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[1]/div/ul/li[2]/a/div").click()
time.sleep(1)

if driver.current_url == 'http://127.0.0.1:8000/n/following':
    print('Following option is working')
else:
    print('Following option failed working')

print("Following Testing Passed")

driver.quit()
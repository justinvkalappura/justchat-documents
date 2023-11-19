from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options=webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver, 30)

print("Testing Started")
driver.get("http://127.0.0.1:8000/n/login")
driver.find_element("id", "email").send_keys("sreelakshmi")
time.sleep(1)
driver.find_element("id", "password").send_keys("Sreelakshmi@123")
time.sleep(1)
driver.find_element("xpath", "/html/body/div/div/form/center/input").click()
time.sleep(1)
driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[1]/div/ul/li[4]/a/div").click()
time.sleep(1)
driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div/button").click()
time.sleep(1)

menu_button = driver.find_element("id", "menu")
menu_button.click()
driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div[1]/div[3]/div[1]/div/div/a[2]").click()
time.sleep(1)

current_password = driver.find_element("id", "currentpassword")
current_password.send_keys("Sreelakshmi@123")
time.sleep(1)

new_password = driver.find_element("id", "newpassword")
new_password.send_keys("Sreelakshmi@1234")
time.sleep(1)

confirm_password = driver.find_element("id", "confirmpassword")
confirm_password.send_keys("Sreelakshmi@1234")
time.sleep(1)

driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/div/div/div/div/form/div[4]/div/button").click()
time.sleep(1)

if driver.current_url == 'http://127.0.0.1:8000/n/login':
    print("UpdatePassword successful")
else:
    print('UpdatePassword failed')

print("UpdatePassword Testing Passed")

driver.quit()

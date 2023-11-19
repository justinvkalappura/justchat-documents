from selenium import webdriver
import time
import os
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
driver.find_element("xpath", "/html/body/div[2]/div[1]/div/div[1]/button").click()
time.sleep(1)
driver.execute_script("createpost()")
driver.find_element("id", "post-text").send_keys("This is my test post.")
time.sleep(1)
image_filename = "spoon.JPG"
image_path = os.path.abspath(os.path.join(os.getcwd(), "static", "assets", "images", image_filename))
file_input = driver.find_element("id", "insert-img")
file_input.send_keys(image_path)
time.sleep(1)
submit_button = driver.find_element(By.CLASS_NAME, "submit-btn")
submit_button.click()
time.sleep(1)

if driver.current_url == 'http://127.0.0.1:8000/':
    print("Post created successfully")
else:
    print('Post creation failed')

print("Post Testing Passed")

driver.quit()
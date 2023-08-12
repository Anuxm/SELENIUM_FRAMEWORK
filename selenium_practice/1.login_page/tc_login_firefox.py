import selenium

#import webdriver module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\gecko-firefox-64\geckodriver.exe")
from selenium.webdriver.common.keys import Keys
import time

#firefox
driver = webdriver.Firefox(service=serv_obj)
#pass the url of the applicatiom,lnch the url on the browser
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
# driver.get("https://admin-demo.nopcommerce.com/login")
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(10)

#find the element on the web page
driver.find_element(By.NAME, 'username').clear()
driver.find_element(By.NAME, 'username').send_keys('Admin')
time.sleep(1)

# Find and enter the Password
driver.find_element(By.NAME, 'password').send_keys('admin123')
time.sleep(1)

# Click the Login button
driver.find_element(By.TAG_NAME, "button").click()
time.sleep(1)
actual_tile=driver.title
expected_tile="OrangeHRM"
if expected_tile==actual_tile:
    print("login test passed")
else:
    print("login test failed")
"""if i enter my name and click alert,hello ananya will come
we need to enter information select alert button and make sure ananya is coming in alert text and click ok"""
#browser alerts/javascripts alerts
#switch_to_alert,accept,dismiss,text method we use.

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="ananya"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
#after clciking alert msg will popup but driver willnot have knowledge about this popups
#switch driver mode to alert mode
#alert will only focus on alert it doesnot have browser level
alert=driver.switch_to.alert
#get the text from alert(it will grab the text which is present in the alert)
alertText=alert.text
print(alertText)
assert name in alertText
#i want to click on ok/yes/done button
alert.accept()
#i want to click cancel
# alert.dismiss()
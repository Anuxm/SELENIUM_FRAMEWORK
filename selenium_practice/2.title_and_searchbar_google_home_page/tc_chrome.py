


#import webdriver module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")
import time

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://www.google.com/")
time.sleep(10)
#find search box element
box=driver.find_element(By.NAME, "q").send_keys('selenium')

driver.find_element(By.NAME, "q").send_keys(Keys.RETURN)
driver.implicitly_wait(10)
print("page title",driver.title)
driver.quit()
#perform search


#find the element on the web page
 
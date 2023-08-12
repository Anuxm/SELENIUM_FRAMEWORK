"""
google--chrome option python--visit here you see lot of ex
headless option--less time,less virtual memory faster execution

"""



import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")

#chrome driver
driver=webdriver.Chrome(service=serv_obj,options=chrome_option)
driver.implicitly_wait(5)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
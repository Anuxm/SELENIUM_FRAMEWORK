"""click on cloum header
#collect all veggies names-> BrowserSortedveggieList (A,B,C)--browaer already sorted
#sort this BrowserSortedveggiesList==newSortedList (A,B,C)
Brosersortedlist==newsortedlist
"""

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(5)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browser_sorted=[]
Veggiesweb=driver.find_elements(By.XPATH,"//tr//td[1]")
for ele in Veggiesweb:
    browser_sorted.append(ele.text)

original_browserlist=browser_sorted.copy()
print(original_browserlist)
browser_sorted.sort()#browser list will sorted
print(browser_sorted)

assert browser_sorted==original_browserlist
"""static drop down =inplace u can see drop down option
ex gender male feamle"""
#we need to import select package
#selenium.webdriver.support.select import Select
#SELECT IS CLASS CREATE OBJECT FOR IT U WILL FIND DIFFERENT METHODS FOR IT
#select_by_index()...by default it will be on 0 index u want to select femelate give 1
#select_by_value()..if the value attribute defined for it based upon that also we can select
#select_by_visible_text()...we can select the option based on the visible text whatever visible on screen
#deselect_by_index()
#deselect_by_value()...
# etc

"""whenever u see select tag for any dropdown that dropdown is static and u can use this select class to handle that option in the dropdown"""

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.current_url)
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
# dropdown.select_by_index(1)



"""no select tag is there to handle the options of the dropdown
ex-country type to select
scan all

https://rahulshettyacademy.com/dropdownsPractise/
"""

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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.current_url)
dropdown=driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
for country in countries:
    if country.text=="India":
        country.click()
        break
#or use get attribute method of java script
#when you update value dynamically through scripts how do you extract the text? famous interview qns
#print(driver.find_element(By.ID,"autoSuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autoSuggest").get_attribute("value")=="India"




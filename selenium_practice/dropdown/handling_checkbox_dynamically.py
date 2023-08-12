
"""no select tag is there to handle the options of the dropdown
ex-country type to select
scan all

https://rahulshettyacademy.com/dropdownsPractise/


chexkbox may not come in order --option1 may come first or sec or third
checkbox and location could be a variable

is_selected()=will tell you that check box is selected  true=checkbox selected ortherwise false

find_element(by.name or id,"value").click()
id,name,value not there
xpath= //input[@type="checkbox"]   it will select all 3 checkbox
"(//input[@type='checkbox'][2])" .click ---it will select option 2
but we are not sure that option2 will come in 2 it may come in top or  bottom
that time use below method

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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.current_url)
checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkbox))
"""it scans all the checkboxes wherever value option2 value is that that particular
checkbox it will select(use this if in name is not there)"""
for check in checkbox:
    if check.get_attribute("value")=="option2":
        check.click()
        assert check.is_selected()
        break



#radiobuttons
#radio button wont change here it exactly come in 2nd place (if not use prev one)
# radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
# radiobuttons[2].click
# assert radiobuttons[2].is_selected()
"""if not selected it will fail"""

radiobuttons=driver.find_element(By.XPATH,"//input[@value='radio3']").click()
assert radiobuttons.is_selected()


#load the page it will show when you click on hide it will hide
#is_displayed() ---return true  it is displayed
driver.find_element(By.ID,"displayed-text").is_displayed() 
#after clicking hide it will hide
assert not driver.find_element(By.ID,"displayed-text").is_displayed() # return false
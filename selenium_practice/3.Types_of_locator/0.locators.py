

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.current_url)
#ID,XPATH,NAME,CSSSELECTOR,link-text
driver.find_element(By.NAME,"name").send_keys("ananya")
#driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("ananya")
driver.find_element(By.NAME,"email").send_keys("anu37858@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1239809")
driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()


##both email and name has the same class name so selenium get confuses so ta
# ke attribute which is unique
#using Xpath
#syntax=//tagname(@attribute="value")--"//input[@type=submit]" or Value="Submit"

# driver.find_element(By.XPATH,"//input[@Value='Submit']").click()
#aftrer submitting we get alert msg and u need to grab that msg
#text--will grab the element which is present in that element
# msg=driver.find_element(By.CLASS_NAME,"alert-success").text
# print(msg)

#finding elements of webpage using the css selector (to create custom css)
#[using [],#id,.classname]
#syntax="tagname[attribute="value"]"
# #idvalue and .classname ex= ".alert-success"
# #exampleInputPassword1


     

driver.find_element(By.CSS_SELECTOR,"input[Value='Submit']").click()
msg=driver.find_element(By.CLASS_NAME,"alert-success").text

"""in this msg variable all msg is there 
success key word is present in variable or not
if there pass or therwise fail
assert-will tell pass or fail based upon our validation"""


print(msg)
assert "success" in msg
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("ananya")

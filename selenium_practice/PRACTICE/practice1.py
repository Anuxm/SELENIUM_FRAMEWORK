"""*= (we can give the partial value by using the regular expression)
chapter16

href attribute------
angularpractice/shop
css--a[href="angularpractice"]
css--a[href*="shop"]----partial vale
//a[contains(@href,"shop")]
tagname[contains]--xpaths syntax

$x
and $-- in console """
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(4)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()

"""scan all the card,identify the common css or xpath which identifies the entire products
#find the common xpath which taking all the 4 cards
we can use chaining of web elements
"""
    #list.append(ele.find_element(By.CSS_SELECTOR,"/div/h4/a").text)
ele=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for ele in ele:
    name=ele.find_element(By.XPATH,"div/h4/a").text
    if name=="Blackberry":
        ele.find_element(By.XPATH,"div/button").click()
driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()








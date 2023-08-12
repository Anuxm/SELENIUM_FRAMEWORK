"""https://rahulshettyacademy.com/seleniumPractise/#/
#count the totall prices 

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
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
#driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
total_products=driver.find_elements(By.XPATH,"//div[@class='product']") #it matching all 3 
count=len(total_products)
assert count>0
cart=driver.find_elements(By.XPATH,"//div[@class='product']/div/button")#list it will select all add to cart (dynamically)
for cart in cart:
    cart.click()
    cart.is_selected()
    
cart_count=driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
 #Xpath using text
button=driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# enter_code=driver.find_element(By.CLASS_NAME,"promoCode").send_keys("ananya")
enter_code=driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
# assert "rahulshettyacademy" in enter_code 
apply=driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
discount=driver.find_element(By.CSS_SELECTOR,".discountPerc").text
print(discount)
#--------------------------------------total price---------------------------
"""xpath--tr//td[5]//p
   td[5]
   css==tr td:nth-child(5) p"""

price=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p") # first iteration 48 sec 67
sum=0
for price in price:
    sum=sum+int(price.text)
print(sum)
totalamount=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==totalamount



#perform chaining

# cart1=driver.find_elements(By.XPATH,"//div[@class='product']/div")
# for cart in cart1:
#     cart.find_element(By.XPATH,"div/button").click() #it will continue from /div/div/buttom


driver.quit()
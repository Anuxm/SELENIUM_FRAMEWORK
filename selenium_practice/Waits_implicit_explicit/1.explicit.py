"""https://rahulshettyacademy.com/seleniumPractise/#/
#chaining 

when to use explicit and when to use implicit wait?*** difference between them
why cant i use time.sleep
(wherever the element is not displayed it will wait otherwise it will continue)
#driver.implicitly_wait(5)--it will wait max 5 sec to show up this is the max timeout if it
find object in 2 min it procedd it willl save 3 sec 
we declaring in global it applies to eacha nd every line in your code whever object is not identified it will wait untill that particular time
time.sleep will sleep 5 secc no matter what even if the element is displayed in 1 sec it blindly closes until that timeout is done.

find_elements--implicit wait will not work bec find element immediately return empty list then one by one it fect but wt selenium think it already return list it wont check whether list has elements or not
so u can put time.sleep() before find_elements


expicit--in your application ex apply code may take 10 or 15 sec to 
(one scenario is demanding 15 sec we cant apply that 15 sec globally to each and every line of your script)
impicit---if the application doesnot load in 5sec then there is an issue bug...but we still wasting another 10 sec everytime


here explicity wait comes here ---u can target one specific element and we can set explicityly or exclusilvely to that particular element upto 15 sec it over writes the implicit wait and applies explicit wait for that step
from selenium.webdriver.support.ui import WebdriverWait
from selenium.webdriver.support import expected_conditions
wait=WebdriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,".promoInfo"))

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
wait.until(expected_conditions.presence_of_element_located(By.CSS_SELECTOR,".promoInfo"))
discount=driver.find_element(By.CSS_SELECTOR,".discountPerc").text
print(discount)
#perform chaining

# cart1=driver.find_elements(By.XPATH,"//div[@class='product']/div")
# for cart in cart1:
#     cart.find_element(By.XPATH,"div/button").click() #it will continue from /div/div/buttom


driver.quit()
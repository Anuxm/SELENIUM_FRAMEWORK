"""https://rahulshettyacademy.com/client/
selenium,protractor,cypress

<a _ngcontent-byc-c43="" class="forgot-password-link" href="/client/auth/password-new">Forgot password?</a>
"""


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
driver.get("https://rahulshettyacademy.com/client")
print(driver.current_url)
#link-text--if the html has a anchor a tag then it is a link
#link-list---give full name
#partial link test--give prtial name
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot pa").click()
#Xpath
# driver.find_element(By.XPATH,"//input[@formcontrolname='userEmail']").click()
#using css [],#id,.classname

# driver.find_element(By.CSS_SELECTOR,"input[id='userPassword']").send_keys("1234567")
# driver.find_element(By.CSS_SELECTOR,"#userPassword").send_keys("1234567")


# driver.find_element(By.CSS_SELECTOR,"input[id='userPassword']").send_keys("1234567")
#using parent child traversing using xpath
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("ananya@gmail.com")
# driver.find_element(By.XPATH,"//form/div[2]/input")

#using parent child traversing using css selection replace /with space and give :n-thchild(2)
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("123445")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("123445")
# driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

#xpath using anchor tag value
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()


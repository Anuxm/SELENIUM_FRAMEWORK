"""there are some events we need to perform by using javascript
scroll down scroll up
selenium doesnot provide any method for it but it will support the javascript to execute that

go to console and type windows.scrollto there provide some value to go up,down,middle and use that value in execute method
0,700 go top
0,500 is height 0x 500y
instead if this number we can use document-scrollheight-we get max height (ex2000 at 2k it  vl fall)

window.scroll(0,700)
window.scroll(0,800)#middle
window.scroll(0,1000)#bottom
window.scroll(0,100) #top

head mode--it opens browser you can see all the actions
run the script using headless mode---u cannt see browser invocation test will run in invisible mode back end it will run but front it wont run it is litlle bit fast to run in headless mode

declare chrome option--
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("headless")
driver=webdriver.Chrome(service=serv_obj,options=chrome_option)
pass chrome option here

taking screenshot detail info you see in framework folder
"""
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")
chrome_option=webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("--ignore-certificate-errors")

#chrome driver
driver=webdriver.Chrome(service=serv_obj,options=chrome_option)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")#max down
# Scroll to the top of the page using execute_script
# driver.execute_script("window.scrollTo(0, 0);")
driver.get_screenshot_as_file("screen.png")



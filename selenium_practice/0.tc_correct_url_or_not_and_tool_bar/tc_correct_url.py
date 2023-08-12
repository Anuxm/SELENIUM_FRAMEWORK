import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://www.google.com/")
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()




"""you might be redirected to the some other websites aftr hitting url
to make sure whether we have landed on correct url or not
sometimes it might open different url"""
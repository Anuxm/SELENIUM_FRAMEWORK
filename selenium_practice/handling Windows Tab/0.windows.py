"""i have opened one window  i have clicked on one link it will open another tab in slenium
perspective openong anothertap or window is same
if u want to pweform operation(testing) (in child wndow new window) selenium cant so directly
bec scope of thw selenuim web driver will be innthe same page(parent page)
we have explicity  tell selenium to switch to child window then only scope will be transferred to child window now driver scope only in child window
again if u want to switch back to parent window u have to explity provide command

window_handles==get the windows name of all the windows which has opened(grab all the windows which got opened and it put them in a list)
first opened window will stored in 0th index 
2nd opened window will stored in 1st indwex so on

https://the-internet.herokuapp.com/windows
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
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windows_opened=driver.window_handles
driver.switch_to.window(windows_opened[1])#scope is in child window
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()#child window will close

driver.switch_to.window(windows_opened[0])#parent window
assert "Opening a new window"==driver.find_element(By.TAG_NAME,"h3").text
driver.quit()






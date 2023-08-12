"""sitting on top of the html driver will have access to your local html code only,t dont have access to the embedded frame

how do i know frames are present in my applications? ask developer
do noraml automation if object is not identicable even aftr giving corrdct id
comeback to html code and seee if there is any frame tags--iframe
browser cant have access to the embedded frame

you have to write a steps to switch to the frame"""
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
driver.switch_to.frame(id,or name)

driver.switch_to.frame("mce-0-ifr") #id,or name

driver._switch_to.default_content()# switch back to browser
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
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr") #id,or name
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("im able to write")
# driver._switch_to.default_content()# switch back to browser
# print(driver.find_element(By.CSS_SELECTOR,"h3").text)
driver.quit()





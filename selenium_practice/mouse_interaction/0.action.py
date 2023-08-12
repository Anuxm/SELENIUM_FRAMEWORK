"""hoveron it ...not clicking just hoveron it"""

"""
ActionChain class
action is object
terminate with perform() then only action will get activated or executed

hoveron it
hongpress(click_and_hold)---send element-it will click on that element and just keep holdindg
rightclick-context_click()
double_click()
drag_and_drop() source and dst give
move_to_element()--
https://rahulshettyacademy.com/dropdownsPractise/






The ActionChains class in Selenium is used for automating complex user interactions, such as mouse movements, key presses, and more. It allows you to perform a sequence of actions on a web page, simulating user behavior. Below are some commonly used methods of the ActionChains class in Selenium:

move_to_element(element): Moves the mouse pointer to the middle of the specified element.
move_to_element_with_offset(element, xoffset, yoffset): Moves the mouse pointer to an element with the specified offset.

click(on_element=None): Clicks the current mouse position or an optional element if provided.

click_and_hold(on_element=None): Clicks and holds the mouse button on the current mouse position or an optional element if provided.

release(on_element=None): Releases the mouse button from the current mouse position or an optional element if provided.

double_click(on_element=None): Performs a double-click action on the current mouse position or an optional element if provided.

context_click(on_element=None): Performs a right-click action on the current mouse position or an optional element if provided.

drag_and_drop(source, target): Drags the source element and drops it onto the target element.

drag_and_drop_by_offset(source, xoffset, yoffset): Drags the source element and drops it at the specified offset from its current position.

key_down(value, element=None): Simulates holding down a key (e.g., CTRL, SHIFT) while interacting with an element.

key_up(value, element=None): Simulates releasing a key that was held down while interacting with an element.

send_keys(*keys_to_send): Sends keystrokes to the active element or the specified element.

perform(): Executes the stored sequence of actions.
"""

import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")

#chrome driver
driver=webdriver.Chrome(service=serv_obj)
#maximize the window then hit the url
driver.maximize_window()
#pass the url of the applicatiom,lnch the url on the browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()#hover on it
# action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()#right click
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform() #hoveron it and it moved to reload and click



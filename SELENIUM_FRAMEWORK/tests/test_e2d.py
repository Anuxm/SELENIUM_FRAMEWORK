import pytest
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from Pageobject.home_page import HomePage
from Pageobject.checkout_page import CheckoutPage
#instead of using explicity use baseclass(use inheritence) 

# import sys
# sys.path.append("")

from utlss.baseclass import BaseClass

# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

     def test_e2e(self):
          #this is the class driver(fixture) u want to use (use self)
          # self.driver.implicitly_wait(4)
          #sending actual driver this local class driver
          homePage=HomePage(self.driver)
          homePage.ShopItem().click()
          page=CheckoutPage(self.driver)
          page.getcardTitle()
          # i=-1
          # for card in cards:
          #      i=i+1
          #      cardText=card.text
          #      print(cardText)
          #      if cardText=="Blackberry":
          #           page.getCardFooter()[i].click()

          ele=self.driver.find_elements(By.XPATH,"//div[@class='card h-100']")
          for ele in ele:
            name=ele.find_element(By.XPATH,"div/h4/a").text
          if name=="Blackberry":
               ele.find_element(By.XPATH,"div/button").click()
          self.driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
     
        #  self.verifylinkpresence("india")




                    

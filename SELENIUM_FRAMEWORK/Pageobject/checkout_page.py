from selenium.webdriver.common.by import By

class CheckoutPage:

     def __init__(self,driver):
          self.driver=driver  
          
     cardTile=(By.CSS_SELECTOR,".card-title a")
     cardFooter=(By.CSS_SELECTOR,".card-footer button")
    
     def getcardTitle(self):
          return self.driver.find_elements(*CheckoutPage.cardTile)
     
     def getCardFooter(self):
          return self.driver.find_elements(*CheckoutPage.cardFooter)
     
        

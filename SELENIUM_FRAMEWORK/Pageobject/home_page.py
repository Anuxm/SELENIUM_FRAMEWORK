from selenium.webdriver.common.by import By


class HomePage:
   
    def __init__(self,driver):
        """whoever creates object of class they have to send driver as their argument
         HomePage=HomePage(self.driver)"""
        self.driver=driver
    shop=(By.CSS_SELECTOR,"a[href*='shop']") # tuple
    name=(By.CSS_SELECTOR,"[name=name]")
    email=(By.CSS_SELECTOR,"[name=email]")



    def ShopItem(self):
         #self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
         # * read the particular variable as tuple and deserilalizes it
         return self.driver.find_element(*HomePage.shop) #shop is a class variable clasname.

    def getName(self):
        return self.driver.find_element(*HomePage.name)
    
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
   
 
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""common utility place it here"""

@pytest.mark.usefixtures("setup")
class BaseClass:
     """instead of having this in every tc we can place then here and
     call in required tc"""
     def verifylinkpresence(self,text):
          element=WebDriverWait(self.driver,10).until(
               EC.presence_of_element_located(By.LINK_TEXT,text)
          )
     
     def test_loggingDemo(self):

        logger=logging.getLogger(__name__)
        fileHandler=logging.FileHandler("logfile.log")# where excatly file should printed
        Formatter=logging.Formatter("%(asctime)s :%(levelname) :%(name)s :%(message)") #time.
        fileHandler.setFormatter(Formatter)
        logger.addHandler(fileHandler)
    
        logger.setLevel(logging.INFO)  
        return logger
          
    
    
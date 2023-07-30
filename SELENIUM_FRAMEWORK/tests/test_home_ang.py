from selenium.webdriver.support.select import Select
from utlss.baseclass import BaseClass
from Pageobject.home_page import HomePage
from TestData.excdata import TestEdata
import pytest


class TestHomepge(BaseClass):               

    
    def test_formSubmission(self,getData):
        #page object mechanism
        #define all in pageobejc--Homepage
        #call homepage object.method
        homepage=HomePage(self.driver)
        # homepage.getName().send_keys("ananya")
        # homepage.getEmail().send_keys("anu378@gmail.com")
        # homepage.getName().send_keys(getData[0])
        # homepage.getEmail().send_keys(getData[1])
        #use dict
        # homepage.getName().send_keys(getData["name"])
        # homepage.getEmail().send_keys(getData["email"])
        
        self.driver.refresh()
        #or get method use so that 2nd time it take rakshi raksi@123

    # @pytest.fixture(params=[("ananya","anu37858@gmai.com"),("rakshi","rakshi@123")])
    # def getData(self,request):
    #     return request.param
    
    # @pytest.fixture(params=[{"name":"ananya","email":"anu37858@gmai.com"},{"name":"rakshi","email":"rakshi@123"}])
    # def getData(self,request):
    #     return request.param
    
        
    #used excel to get data
    @pytest.fixture(params=TestEdata.get_exc_data("test3"))
    def getData(self,request):
        return request.param
    

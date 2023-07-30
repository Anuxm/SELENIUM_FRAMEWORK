import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#once a class below will  execute --in class use usefixture


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="inovikg chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\chromedriver_win32\chromedriver.exe")
        #chrome driver
        driver=webdriver.Chrome(service=serv_obj)
    elif browser_name=="edge":
            serv_obj=Service(r"C:\Users\Asus\Desktop\selenium\drivers\edgedriver_win64\msedgedriver.exe")  
            driver=webdriver.Edge(service=serv_obj)        

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    #maximize the window then hit the url
    driver.maximize_window()
    #this is the class driver u want to use (use self)
    request.cls.driver=driver
    yield
    driver.close()

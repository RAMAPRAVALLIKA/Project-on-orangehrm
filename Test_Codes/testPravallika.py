from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Pravallika_Data
from Test_Locators.locators import Pravallika_Locators
from time import sleep
import pytest

class Test_Pravallika:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    def test_TC_Login_01(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Pravallika_Data().B)
        self.driver.find_element(by = By.NAME, value = Pravallika_Locators().A).send_keys(Pravallika_Data().C)
        self.driver.find_element(by = By.NAME, value = Pravallika_Locators().B).send_keys(Pravallika_Data().D)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().C).click()
        assert (self.driver.title == Pravallika_Data().A)
        print("Status = Successful")

    def test_TC_Login_02(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Pravallika_Data().B)
        self.driver.find_element(by = By.NAME, value = Pravallika_Locators().A).send_keys(Pravallika_Data().E)
        self.driver.find_element(by = By.NAME, value = Pravallika_Locators().B).send_keys(Pravallika_Data().F)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().C).click()
        assert (self.driver.title == "OrangeHHRM")
        # print("Status = Successful")

    def test_TC_PIM_01(self, boot):
        self.driver.implicitly_wait(10)
        self.test_TC_Login_01(self)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().D).click()
        self.driver.find_element(by = By.LINK_TEXT, value = Pravallika_Locators().E).click()
        self.driver.find_element(by = By.NAME, value = Pravallika_Locators().F).send_keys(Pravallika_Data().G)
        self.driver.find_element(by = By.NAME, value = Pravallika_Locators().G).send_keys(Pravallika_Data().H)
        self.driver.find_element(by = By.NAME, value = Pravallika_Locators().H).send_keys(Pravallika_Data().I)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().I).click()
        self.driver.find_element(by = By.LINK_TEXT, value = Pravallika_Locators().J).click()
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().K).send_keys(Pravallika_Data().J)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().L).send_keys(Pravallika_Data().K)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().M).send_keys(Pravallika_Data().L)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().N).send_keys(Pravallika_Data().M)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().O).send_keys(Pravallika_Data().N)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().P).send_keys(Pravallika_Data().O)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().Q).send_keys(Pravallika_Data().P)
        self.driver.find_element(by = By.XPATH, value = Pravallika_Locators().R).click()
        self.driver.implicitly_wait(10)
        self.URL = self.driver.current_url
        assert (self.driver.title == Pravallika_Data().A)
        print("Status = Successful")

# pytest -v -s --capture=sys --html=C:\Users\Pravi\Desktop\PROJECT\Reports\test_1.html testPravallika.py

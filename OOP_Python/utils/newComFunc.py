# from selenium.webdriver.common.by import By
from OOP_Python.utils.commonUtils import comUtils

class newCommonfunctions():

    def __init__(self, driver):
        self.driver = driver
        self.cf = comUtils(driver)

    def clickElement(self, locatedBy, locatorValue):
        self.driver.find_element(locatedBy, locatorValue).click()

    def sendText(self, locatedBy, locatorValue, text):
        self.driver.find_element(self.cf.getByType(locatedBy), locatorValue).sendkeys(text)


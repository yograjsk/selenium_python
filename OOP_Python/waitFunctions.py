from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from OOP_Python.utils.commonUtils import comUtils
from selenium.common.exceptions import *


class waitFunctions():
    def __init__(self, driver):
        self.driver = driver
        self.cf = comUtils(driver)

    def explicitWaitForElement(self, locator, locateBy="linktext", timeout=10, pollFreq=1):
        element = None
        try:
            print("waiting for element till it is clickable for maximum " + str(timeout) + " seconds")

            byType = self.cf.getByType(locateBy)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, "Logout")))
            # element.click()

            print("Element found")
        except:
            print("Element is not observed on web page")
        return element


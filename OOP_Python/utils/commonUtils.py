from selenium.webdriver.common.by import By


class comUtils():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locateBy):
        locateBy = locateBy.lower()
        if locateBy == "id":
            return By.ID
        elif locateBy == "name":
            return By.NAME
        elif locateBy == "xpath":
            return By.XPATH
        elif locateBy == "css":
            return By.CSS_SELECTOR
        elif locateBy == "classname":
            return By.CLASS_NAME
        elif locateBy == "linktext":
            return By.LINK_TEXT
        elif locateBy == "partiallinktext":
            return By.PARTIAL_LINK_TEXT
        else:
            print("Invalid locatorBy value " +locateBy)
        return False


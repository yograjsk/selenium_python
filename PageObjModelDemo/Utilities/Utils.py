from selenium import webdriver
from selenium.webdriver.common.by import By

class Utils:

    def propertiesFileReader(self, filePath):
        properties = {}

        with open(filePath, 'r') as f:
            for line in f:
                line = line.rstrip()
                if ("=" not in line or line.startswith("#")): continue
                k, v = line.split("=", 1)
                properties[k] = v
        print(properties)
        return properties

    def getDriver(self, browserName):
        driver = None
        if browserName in ("chrome", "Chrome", "CHROME"):
            driver = webdriver.Chrome(executable_path='../../drivers/chromedriver.exe')
        elif browserName in ("firefox", "FF", "ff"):
            driver = webdriver.Firefox(executable_path='../../drivers/geckodriver.exe')
        elif browserName in ("ie", "internetExplorer", "InternetExplorer", "IE"):
            driver = webdriver.Ie(executable_path='../../drivers/IEDriverServer.exe')
        return driver


    def enterTextToTextField(self, byValue, byLocatorValue, text, driver):
        if byValue is "id":
            driver.find_element(By.ID, byLocatorValue).send_keys(text)
        elif byValue is "class":
            driver.find_element(By.CLASS_NAME, byLocatorValue).send_keys(text)
        elif byValue is "xpath":
            driver.find_element(By.XPATH, byLocatorValue).send_keys(text)
        elif byValue is "name":
            driver.find_element(By.NAME, byLocatorValue).send_keys(text)

    def clickOnElement(self, byValue, byLocatorValue, driver):
        if byValue is "id":
            driver.find_element(By.ID, byLocatorValue).click()
        elif byValue is "class":
            driver.find_element(By.CLASS_NAME, byLocatorValue).click()
        elif byValue is "xpath":
            driver.find_element(By.XPATH, byLocatorValue).click()
        elif byValue is "name":
            driver.find_element(By.NAME, byLocatorValue).click()

    def checkElementPresent(self, byValue, byLocatorValue, driver):
        try:
            if byValue is "id":
                return driver.find_element(By.ID, byLocatorValue).is_displayed()
            elif byValue is "class":
                return driver.find_element(By.CLASS_NAME, byLocatorValue).is_displayed()
            elif byValue is "xpath":
                return driver.find_element(By.XPATH, byLocatorValue).is_displayed()
            elif byValue is "name":
                return driver.find_element(By.NAME, byLocatorValue).is_displayed()
        except:
            return False


    def takeScreenshot(self, screenshotPath, driver):
        driver.save_screenshot(screenshotPath)
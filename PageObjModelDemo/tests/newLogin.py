import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjModelDemo.pages.login_page import Login_page
from PageObjModelDemo.pages.home_page import Home_page
from PageObjModelDemo.ObjectRepository.ObjRepo import OR
from PageObjModelDemo.Utilities.Utils import Utils

class NewLoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.u = Utils()
        cls.config = cls.u.propertiesFileReader("../Configuration/config.properties")
        browser = cls.config["browserName"]
        timeout = cls.config["timeout"]
        cls.driver = cls.u.getDriver(browser)
        # cls.driver = webdriver.Chrome(executable_path="C:/Users/USER/PycharmProjects/sample/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(int(timeout))

    def setUp(self):
        print("runs before every test method")

    def test_validLogin(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        or1 = OR()
        # or1 = OR()
        u = Utils()

        u.enterTextToTextField("id", or1.username_txt, "admin", self.driver)
        u.enterTextToTextField("id", or1.password_txt, "admin123", self.driver)
        u.clickOnElement("id", or1.login_btn, self.driver)
        # u.enterTextToTextField("id", or1.username_txt, "admin", self.driver)
        # u.enterTextToTextField("id", or1.password_txt, "admin123", self.driver)
        # u.clickOnElement("id", or1.login_btn, self.driver)
        checkLoginSuccessful = u.checkElementPresent("id", or1.welcome_link_id, self.driver)
        if checkLoginSuccessful is True:
            u.takeScreenshot("../Screenshots/loginSuccessful.png", self.driver)
        else:
            u.takeScreenshot("../Screenshots/loginFailed.png", self.driver)

        print("Valid Login Test Completed")

    @classmethod
    def tearDownClass(cls):
        print("runs after last test method")


if __name__ == '__main__':
    unittest.main()






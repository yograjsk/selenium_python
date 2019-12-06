from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from SeleniumPOMProject.Pages.login_page import Login_Page
from SeleniumPOMProject.Pages.home_page import HomePage
from SeleniumPOMProject.Utilities.Utils import utils
# from SeleniumPOMProject.ObjectRepository.ObjRepo import OR


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        u = utils()
        cls.config = u.propertiesFileReader("../Configuration/config.properties")
        browser = cls.config["browserName"]
        timeout = cls.config["timeout"]
        cls.driver = u.getDriver(browser)
        # cls.driver = webdriver.Chrome(executable_path="C:/Users/USER/PycharmProjects/sample/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(int(timeout))


    def test_validLogin(self):
        driver = self.driver
        URL = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
        driver.get(URL)

        login = Login_Page(driver)
        # loginPage = Login_Page()
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

        # self.driver.find_element(By.ID, "txtUsername").send_keys("admin")
        # self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        # self.driver.find_element(By.ID, "btnLogin").click()
        # self.driver.find_element(By.ID, "welcome").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Login Test Completed")

if __name__ == '__main__':
    unittest.main()


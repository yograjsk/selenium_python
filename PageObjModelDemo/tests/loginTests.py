from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjModelDemo.pages.login_page import Login_page
from PageObjModelDemo.pages.home_page import Home_page
import unittest


class LoginTests():

    # @classmethod
    # def setUpClass(self):
    #     self.driver = webdriver.Chrome(executable_path='C:/Users/USER/PycharmProjects/sample/drivers/chromedriver.exe')
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(5)

    def test_validLogin(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/USER/PycharmProjects/sample/drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        # driver = self.driver
        login = Login_page(self.driver)
        home = Home_page(self.driver)

        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login.enter_username("admin")
        login.enter_password("admin123")
        login.click_login_button()

        # self.driver.find_element(By.ID, "txtUsername").send_keys("admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element(By.ID, "btnLogin").click()
        # welcomePresent = self.driver.find_element(By.ID, "welcome").is_displayed()
        # if welcomePresent:
        #     print("User Logged in Successfully")
        # else:
        #     print("User Failed to log in")

        home.click_welcomeLink()
        home.click_logoutLink()
        # self.driver.find_element(By.ID, "welcome").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        print("Valid Login Test Completed")

lt = LoginTests()
lt.test_validLogin()





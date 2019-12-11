import unittest
import HtmlTestRunner
from selenium import webdriver
from PageObjModelDemo.pages.home_page import Home_page
from PageObjModelDemo.pages.login_page import Login_page

'''
normal methods - create object, call the method to run - this will work for all the methods

unittest - no need to create the object of the class, and not need to call the methods explicitly
as soon you mention the "test" in prefix the method gets picked up for execution automatically
'''



class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("run only once before the first test method")
        print("Running Login Tests Class tests")
        self.driver = webdriver.Chrome(executable_path='C:/Users/USER/PycharmProjects/sample/drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def setUp(self):
        print("runs before every test method")

    def test1(self):
        print("test1 method")

    def test2(self):
        print("test2 method")

    def test3(self):
        print("test3 method")

    def logintest(self):
        print("This is a login test scenario")

    def test_validLogin(self):
        # self.driver = webdriver.Chrome(executable_path='C:/Users/USER/PycharmProjects/sample/drivers/chromedriver.exe')
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)
        # driver = self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        login = Login_page(self.driver)

        # with separate page objects way
        login.enter_username("admin")
        login.enter_password("admin123")
        login.click_login_button()


        home = Home_page(self.driver)
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

    @classmethod
    def tearDownClass(cls):
        print("runs after last test method")

# lt = LoginTests()
# lt.test_validLogin()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='htmlReport.html'))






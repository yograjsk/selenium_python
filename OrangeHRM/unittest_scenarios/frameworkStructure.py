import unittest
from selenium import webdriver

username = "Admin"
password = "admin123"
url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
location = '../drivers/'


def setUpModule():
    print("setupModule - setup browser and webdriver")


def tearDownModule():
    print("tearDownModule - close browser and quit webdriver")


class FWstructure(unittest.TestCase):
    driver = webdriver.Chrome(executable_path=location + 'chromedriver.exe')

    @classmethod
    def setUp(self):
        print("login to the application")
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()

    @classmethod
    def tearDown(self):
        print("logout of the application")
        self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element(By.ID, "welcome").click()
        # time.sleep(2)
        self.driver.find_element_by_link_text("Logout").click()

    @classmethod
    def setUpClass(cls):
        print("setupClass - Launch the application")

    @classmethod
    def tearDownClass(cls):
        print("teardown Class - logout the application")

    def test_verify_welcome(self):
        print("verifying welcome")
        welcomeText = self.driver.find_element_by_id('welcome').text
        print(welcomeText)
        assert "Welcome "+self.username in welcomeText

    def test_create_user(self):
        print("creating user")

    def test_edit_user(self):
        print("editing user")

    def test_delete_user(self):
        print("deleting user")

if __name__ == "__main__":
    unittest.main()


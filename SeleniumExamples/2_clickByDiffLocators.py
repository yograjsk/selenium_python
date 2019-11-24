import unittest

from selenium import webdriver

class LinkTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

    def setUp(self):
        print("Running setUp Method")
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

    def test_click_link_by_text(self):
        print("Running test_click_link_by_text")
        self.driver.find_element_by_link_text("Forgot your password?").click()

    def test_click_link_by_id(self):
        print("Running test_click_link_by_id")
        self.driver.find_element_by_id("btnLogin").click()

    def test_click_link_by_partial_text(self):
        print("Running test_click_link_by_partial_text")
        self.driver.find_element_by_partial_link_text("Forgot your").click()

    def test_click_link_by_xpath(self):
        print("Running test_click_link_by_xpath")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()

    def tearDown(self):
        print("Teardown method")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        # cls.driver.quit()


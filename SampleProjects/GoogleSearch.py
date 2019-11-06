from selenium import webdriver
import unittest

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        driver.implicitly_wait(10)
        driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("www.google.com")
        self.driver.find_elements_by_name("q").send_keys("Automation with Python")
        self.driver.find_elements_by_name("btnK").click()

    def test_search_yograj(self):
        self.driver.get("www.google.com")
        self.driver.find_elements_by_name("q").send_keys("yograj")
        self.driver.find_elements_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print(("test completed"))






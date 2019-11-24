import unittest
import time
import os

from selenium import webdriver

class LinkTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        print("TearDown")
        # cls.driver.quit()

    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        # self.driver.find_element_by_name('txtUsername').send_keys("admin")
        # self.driver.find_element_by_name('txtPassword').send_keys("admin123")
        # self.driver.find_element_by_name('Submit').click()

    def test1(self):
        self.assertTrue(self.driver.find_element_by_xpath("//input[@id='btnLogin']").is_displayed())
        print(self.driver.find_element_by_xpath("//input[@id='btnLogin']").is_displayed())

    def test2(self):
        # self.driver.find_elements_by_link_text()
        list1 = ['abcd']
        elements1 = self.driver.find_elements_by_link_text("Forgot your password?")
        elements2 = self.driver.find_elements_by_link_text("Forgot your password?")
        elements2.pop(0)
        self.assertEqual(1,len(elements1),"forgot password link is available more than 1 time")
        self.assertCountEqual(elements1, elements2, "The two lists are not equal")

    def test3(self):
        print(self.driver.find_element_by_id("btnLogin").is_displayed())

    def test4(self):
        self.assertFalse(self.driver.find_element_by_id("txtUsername").is_selected(),"The element is not selected")

    def test5(self):
        linkelements = self.driver.find_elements_by_tag_name("a")
        print("link Count:", len(linkelements))
        for link in linkelements:
            print("<",link.text,">")


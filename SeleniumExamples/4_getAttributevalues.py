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
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        self.driver.find_element_by_name('txtUsername').send_keys("admin")
        self.driver.find_element_by_name('txtPassword').send_keys("admin123")
        self.driver.find_element_by_name('Submit').click()

    def test_linkTexts(self):
        links = self.driver.find_elements_by_tag_name("a")
        print('count of links is',len(links))
        for link in links:
            text = link.get_attribute("text")
            href = link.get_attribute("href")
            print("text:",text,"href:",href)

    def test_menuItems(self):
        menus = self.driver.find_elements_by_class_name("firstLevelMenu")
        print('Total first level menu count is',len(menus))
        for menu in menus:
            text = menu.get_attribute("text")
            font = menu.get_attribute("font")
            print("text:",text,"font:",font)

'''
excel file - fetch, and upload (browser), and download
dropdown - loops associated
popup window, alert
Jenkins/Maven
Report HTML
executing javascript



'''
import unittest
import time
from selenium import webdriver

class GoogleTestCase(unittest.TestCase):

    site_url = "https://google.com"

    def start_chrome(self):
        driver =  webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        driver.get(self.site_url)
        time.sleep(1)
        driver.quit()

    def test_start_firefox_and_assert_title(self):
        driver =  webdriver.Firefox(executable_path='drivers/geckodriver.exe')
        driver.get(self.site_url)
        self.assertEqual("Google", driver.title)
        time.sleep(1)
        driver.quit()

    def test_start_ie(self):
        driver =  webdriver.Ie(executable_path='drivers/IEDriverServer.exe')
        driver.get(self.site_url)
        time.sleep(1)
        driver.quit()

# googletestCase = GoogleTestCase()
# googletestCase.test_start_chrome()
# googletestCase.test_start_firefox_and_assert_title()
# googletestCase.test_start_ie()

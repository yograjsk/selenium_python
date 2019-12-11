import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageObjModelDemo.Utilities.Utils import Utils

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("running tests from NewLoginTests class")
        cls.u = Utils()
        cls.config = cls.u.propertiesFileReader("../Configuration/config.properties")
        browser = cls.config["browserName"]
        timeout = cls.config["timeout"]
        cls.driver = cls.u.getDriver(browser)
        # cls.driver = webdriver.Chrome(executable_path="C:/Users/USER/PycharmProjects/sample/drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(int(timeout))


    def test_googleSearch(self):
        gs = GoogleSearch()
        gs.googleSearch("Python Programming")
        # # print("running google search text")
        # driver = self.driver
        # URL = "https://www.google.com/"
        # driver.get(URL)
        # searchText = "python programming"
        # searchField = driver.find_element(By.NAME, "q")
        # searchField.send_keys(searchText + Keys.ENTER)
        #
        # title = driver.title
        # self.assertEqual(searchText + " - Google Search", title)

    def googleSearch(self, searchText):
        # print("running google search text")
        driver = self.driver
        URL = "https://www.google.com/"
        driver.get(URL)
        # searchText = "python programming"
        searchField = driver.find_element(By.NAME, "q")
        searchField.send_keys(searchText + Keys.ENTER)
        self.u.checkElementPresent("id", "hdtb-tls", self.driver)

        title = driver.title
        self.assertEqual(searchText + " - Google Search", title)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Login Test Completed")

if __name__ == '__main__':
    unittest.main()


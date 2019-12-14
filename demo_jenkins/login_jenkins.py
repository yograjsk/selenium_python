from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

baseLocation = "drivers/"
# driver = webdriver.Chrome(executable_path=baseLocation+'chromedriver.exe')
# driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")

class scenario(unittest.TestCase):

    def test_search(self):
        # driver.save_screenshot("sample.png")
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
        driver = self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        # self.driver.get("https://www.google.com/")
        pageTitle = str(driver.title)
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        driver.find_element(By.ID, "btnLogin").click()
        driver.find_element(By.ID, "welcome").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()


if __name__ == '__main__':
    unittest.main()


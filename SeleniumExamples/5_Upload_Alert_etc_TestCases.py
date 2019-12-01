import unittest
import pandas as pd
import time
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Upload_Alert_etc_TC(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chop = Options()
        # chop.add_argument("--disable-infobars")
        chop.add_argument("--disable-extensions")
        chop.add_argument("--disable-notifications")
        chop.add_argument("--disable-gpu")
        # chop.add_argument("--incognito")
        chop.add_argument("--ignore-certificate-errors")
        chop.add_argument("--disable-popup-blocking")

        # chop.add_argument("--window-size=1920,1080")
        chop.add_argument("--start-maximized")
        # chop.add_argument("--headless")
        chop.add_experimental_option("prefs", {
            "download.prompt_for_download": True,
            "safebrowsing_for_trusted_sources_enabled": True,
            "safebrowsing.enabled": True
        })
        chop.add_experimental_option("excludeSwitches", ['enable-automation'])
        cls.driver = webdriver.Chrome(chrome_options=chop, executable_path="drivers/chromedriver.exe")

        cls.driver.implicitly_wait(5)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
        cls.driver.find_element_by_name('txtUsername').send_keys("admin")
        cls.driver.find_element_by_name('txtPassword').send_keys("admin123")
        cls.driver.find_element_by_name('Submit').click()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def _test_upload_dataImport(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
        self.assertTrue(self.driver.find_element(By.ID, 'welcome').is_displayed())
        element = self.driver.find_element(By.ID, 'pimCsvImport_csvFile')
        # element = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        element.send_keys(os.getcwd()+"/importData.csv")
        self.driver.find_element(By.ID, "btnSave").click()

    def test_download_template(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/pimCsvImport")
        element = self.driver.find_element(By.CLASS_NAME, 'download')
        element.click()

    def _test_1readExcel(self):
        data = pd.read_excel("websites.xlsx")
        print(data)
        # list = data.values.tolist()
        # print("\nlist\n",list)
        # name = data['name'].tolist()
        # url = data['url'].tolist()
        # print("\nname\n",name,"\nurl\n",url)

    def _test_handleSimpleAlert(self):
        self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
        element = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
        element.click()
        alert = self.driver.switch_to.alert
        alertMsg = alert.text
        print(alertMsg)
        alert.accept()

    def _test_2handleSimpleAlert(self):
        list = [True, False]
        # accept = True
        for condition in list:

            self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
            element = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
            element.click()
            alert = self.driver.switch_to.alert
            alertMsg = alert.text
            print(alertMsg)
            if condition:
                alert.accept()
                print("Accepted Alert")
            else:
                alert.dismiss()
                print("Cancelled Alert")
            buttonPressInfo = self.driver.find_element(By.ID, "confirm-demo").text
            print(buttonPressInfo)






'''
excel file - fetch, and upload (browser), and download
dropdown - loops associated
popup window, alert
Jenkins/Maven
Report HTML
executing javascript



'''

# profile = webdriver.FirefoxProfile()
# profile.set_preference('browser.download.folderList', 2)
# # profile.set_preference('browser.download.manager.showWhenStarting', False)
# # profile.set_preference('browser.download.dir', '/temp')
# profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
# profile.set_preference('browser.download.useDownload.Dir', True)
#
# cls.driver = webdriver.Firefox(profile, executable_path='drivers/geckodriver.exe')
# cls.driver = webdriver.Firefox(profile)

# cls.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

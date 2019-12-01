import unittest
import pandas as pd
import os
import itertools

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class ExcelReader(unittest.TestCase):

    def _test_1readExcel(self):

        data = pd.read_excel("websites.xlsx")
        print("data frame format\n",data)
        print(type(data))
        list = data.values.tolist()
        listTranspose = data.values.T.tolist()
        print("\nlist\n",list)
        print("\nTransposelist\n",listTranspose)
        name = data['name'].tolist()
        url = data['url'].tolist()
        print("\nname\n",name,"\nurl\n",url)

    def test_2AccessDiffSites(self):
        data = pd.read_excel("websites.xlsx")
        name = data['name'].tolist()
        url = data['url'].tolist()
        print("\nname\n",name,"\nurl\n",url)

        # for a in name:
        #     print(a)
        for (n, u) in zip (name, url):
            print("sitename",n,"url",u)




    # def _test_handleSimpleAlert(self):
    #     self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    #     element = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
    #     element.click()
    #     alert = self.driver.switch_to.alert
    #     alertMsg = alert.text
    #     print(alertMsg)
    #     alert.accept()
    #
    # def _test_2handleSimpleAlert(self):
    #     list = [True, False]
    #     # accept = True
    #     for condition in list:
    #
    #         self.driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
    #         element = self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']")
    #         element.click()
    #         alert = self.driver.switch_to.alert
    #         alertMsg = alert.text
    #         print(alertMsg)
    #         if condition:
    #             alert.accept()
    #             print("Accepted Alert")
    #         else:
    #             alert.dismiss()
    #             print("Cancelled Alert")
    #         buttonPressInfo = self.driver.find_element(By.ID, "confirm-demo").text
    #         print(buttonPressInfo)



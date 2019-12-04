import unittest
import pandas as pd
import os
import itertools

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class ExcelReader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        cls.driver.implicitly_wait(5)

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
        name = data['NAME'].tolist()
        url = data['URL'].tolist()
        print("\nname\n",name,"\nurl\n",url)

        # for a in name:
        #     print(a)
        for (n, u) in zip (name, url):
            print("opening sitename",n,"url",u)
            self.driver.get(u)
            print("title is:",self.driver.title)


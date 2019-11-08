from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

class CheckWelcome:
    '''
    implicite wait = applicatble for all elements
    explicite wait = perticular / desired element
    '''

    def __init__(self):
        self.username = "Admin"
        self.password = "admin123"
        self.url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        self.location = '../drivers/'
        # self.driver = webdriver.Chrome(executable_path=self.location + 'chromedriver.exe')

    def setup(self):
        # url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        # location = '../drivers/'
        self.driver = webdriver.Chrome(executable_path=self.location + 'chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)
        # time.sleep(2)

    def login(self):
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()

    def checkWelcome(self):

        welcomeText = self.driver.find_element_by_id('welcome').text
        print(welcomeText)
        assert "Welcome "+self.username in welcomeText

    def logout(self):
        # time.sleep(2)
        # wait = WebDriverWait(self.driver, 10)
        # # element = wait.until(EC.element_to_be_clickable(self.driver.find_element_by_id("welcome")))
        # # element.click()
        # wait.until(EC.element_to_be_clickable(self.driver.find_element(By.ID, "welcome"))).click()
        self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element(By.ID, "welcome").click()
        # time.sleep(2)
        self.driver.find_element_by_link_text("Logout").click()

check1 = CheckWelcome()
check1.setup()
check1.login()
check1.checkWelcome()

check1.logout()


# checkWelcome()



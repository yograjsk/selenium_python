from selenium import webdriver
from selenium.webdriver.common.by import By
from OOP_Python.waitFunctions import waitFunctions
from traceback import print_stack
import datetime

class ExplicitWait():

    def test_verifyWelcome(self):
        url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        location = '../drivers/'
        driver = webdriver.Chrome(executable_path=location + 'chromedriver.exe')
        # driver2 = webdriver.Firefox(executable_path=location + 'geckodriver.exe')
        wait = waitFunctions(driver)
        driver.get(url)
        driver.find_element(By.NAME, 'txtUsername').send_keys('Admin')
        driver.find_element(By.NAME, 'txtPassword').send_keys('admin123')
        driver.find_element(By.NAME, 'Submit').click()
        welcomeText = driver.find_element_by_id('welcome').text
        print(welcomeText)
        driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()
        element = wait.explicitWaitForElement("Logout")
        element.click()

run = ExplicitWait()
run.test_verifyWelcome()
# checkWelcome()

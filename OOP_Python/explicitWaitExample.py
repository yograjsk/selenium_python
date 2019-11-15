from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from OOP_Python.utils.newComFunc import newCommonfunctions
from traceback import print_stack
import datetime


class ExplicitWait():

    def test_checkWelcome(self):
        try:
            url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
            location = '../drivers/'
            driver = webdriver.Chrome(executable_path=location + 'chromedriver.exe')
            # driver.implicitly_wait(5)

            driver.get(url)
            # driver.find_element_by_name('txtUsername').send_keys('Admin')
            # driver.find_element_by_name('txtPassword').send_keys('admin123')
            # driver.find_element_by_name('Submit').click()

            driver.find_element(By.NAME, 'txtUsername1').send_keys('Admin')
            driver.find_element(By.NAME, 'txtPassword').send_keys('admin123')
            driver.find_element(By.NAME, 'Submit').click()

            # cf.sendText("name", "txtUsername", "Admin")
            # cf.sendText("name", "txtPassword", "admin123")
            # cf.clickElement("name", "Submit")

            welcomeText = driver.find_element_by_id('welcome').text
            print(welcomeText)
            driver.find_element_by_id("welcome").click()
            # driver.find_element_by_link_text("Logout").click()
            wait = WebDriverWait(driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                     ElementNotVisibleException,
                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
            element.click()
        except:
            # driver.save_screenshot("screenshots/failureStep.png")
            # driver.save_screenshot("screenshots/failureStep.png")
            driver.save_screenshot("screenshots/failureStep_%s.png" % (str(datetime.datetime.now()).replace(":", "_")))
            # print("screenshots/failureStep_%s.png" %(str(datetime.datetime.now()).replace(":", "_")))
            # print("my name is %s and I am learning %s" %("anu", "selenium"))
            print_stack()


run = ExplicitWait()
run.test_checkWelcome()
# checkWelcome()

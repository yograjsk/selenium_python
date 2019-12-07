from selenium.webdriver.common.by import By
from PageObjModelDemo.ObjectRepository.ObjRepo import OR


class Login_page():

    def __init__(self, driver):
        self.driver = driver


        self.username_txt = "txtUsername"
        self.password_txt = "txtPassword"
        self.login_btn = "btnLogin"

        self.usernameNew = (By.ID, "txtUsername")
        self.passwordNew = (By.ID, "txtPassword")

        # self.usernameField = self.driver.find_element(By.ID, self.username_txt)
        # self.passwordField = self.driver.find_element(By.ID, self.password_txt)

        # self.usernameField = self.driver.find_element(self.usernameNew)
        # self.passwordField = self.driver.find_element(self.passwordNew)


    def enter_username(self, username):
        # self.usernameField.send_keys(username)
        self.driver.find_element(By.ID, self.username_txt).send_keys(username)

    def enter_password(self, password):
        # self.passwordField.send_keys(password)
        self.driver.find_element(By.ID, self.password_txt).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_btn).click()

'''
one:  methods information/method writing - we dont pass parameters, but we define them

'''

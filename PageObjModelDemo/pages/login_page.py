from selenium.webdriver.common.by import By


class Login_page():

    def __init__(self, driver):
        self.driver = driver

        self.username_txt = "txtUsername"
        self.password_txt = "txtPassword"
        self.login_btn = "btnLogin"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_txt).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_txt).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_btn).click()

'''
one:  methods information/method writing - we dont pass parameters, but we define them

'''

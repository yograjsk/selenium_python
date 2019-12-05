from selenium.webdriver.common.by import By


class Home_page():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_text = "Logout"

    def check_welcomeLinkPresent(self):
        return self.driver.find_element(By.ID, self.welcome_link_id).is_displayed()

    def click_welcomeLink(self):
        self.driver.find_element(By.ID, self.welcome_link_id).click()

    def click_logoutLink(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_text).click()



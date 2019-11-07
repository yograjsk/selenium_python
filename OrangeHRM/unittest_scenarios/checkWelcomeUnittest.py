from selenium import webdriver
import time

class CheckWelcome:


    def __init__(self):
        self.username = "Admin"
        self.password = "admin123"
        self.url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        self.location = '../drivers/'
        # self.driver = webdriver.Chrome(executable_path=self.location + 'chromedriver.exe')

    @classmethod
    def setUpClass(cls):
        print("launch application login page")

    @classmethod
    def tearDownClass(cls):
        print("close the application page")

    @classmethod
    def setUp(self):
        print("logining into the application")

    @classmethod
    def tearDown(self):
        print("logining out of the application")

    def test_checkWelcome(self):
        # print("login")
        print("checking welcome user text")
        # print("logout")



    def setUp(self):
        # url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        # location = '../drivers/'
        self.driver = webdriver.Chrome(executable_path=self.location + 'chromedriver.exe')
        self.driver.get(self.url)
        time.sleep(2)

    def login(self):
        self.driver.find_element_by_name('txtUsername').send_keys('Admin')
        self.driver.find_element_by_name('txtPassword').send_keys('admin123')
        self.driver.find_element_by_name('Submit').click()

    def checkWelcome(self):
        welcomeText = self.driver.find_element_by_id('welcome').text
        print(welcomeText)
        assert "Welcome "+self.username in welcomeText

    def logout(self):
        self.driver.find_element_by_id("welcome").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("Logout").click()

check1 = CheckWelcome()
check1.setup()
check1.login()
check1.checkWelcome()

check1.logout()


# checkWelcome()



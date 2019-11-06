from selenium import webdriver
import time

def checkWelcome():
    url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
    location = '../drivers/'
    driver = webdriver.Chrome(executable_path=location + 'chromedriver.exe')

    driver.get(url)
    time.sleep(2)
    driver.find_element_by_name('txtUsername').send_keys('Admin')
    driver.find_element_by_name('txtPassword').send_keys('admin123')
    driver.find_element_by_name('Submit').click()
    welcomeText = driver.find_element_by_id('welcome').text
    print(welcomeText)
    assert "Welcome" in welcomeText
    driver.find_element_by_id("welcome").click()
    driver.find_element_by_link_text("Logout").click()

# checkWelcome()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

baseLocation = "resources/"
driver = webdriver.Chrome(executable_path=baseLocation+'chromedriver.exe')

def checkTitle_SearchByUsingKeys(searchText):
    flag = False
    driver.maximize_window()
    driver.get("https://www.google.com/")
    googleSearchBar = driver.find_element_by_name("q")
    # action.move_to_element(mikeIcon).perform()
    googleSearchBar.send_keys("Learn Python"+Keys.ENTER)
    title = driver.title
    if title is searchText+" - Google Search":
        flag = True
    return flag


def mouseOverUsingActions():
    action = ActionChains(driver)
    driver.maximize_window()
    driver.get("https://www.google.com/")
    mikeIcon = driver.find_element_by_class_name("JC0tCe")
    action.move_to_element(mikeIcon).perform()


from selenium import webdriver
from selenium.webdriver.common.by import By

baseLocation = "drivers/"
driver = webdriver.Chrome(executable_path=baseLocation+'chromedriver.exe')

def search():

    driver.save_screenshot()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    pageTitle = str(driver.title)
    print(driver.find_elements_by_xpath("count(//a)"))
    # elements = driver.find_elements_by_xpath("count(//a)")
    # count = len(elements)
    # driver.find_element(By.)
    # check = driver.find_element_by_partial_link_text("Learn Python Programming").is_displayed()
    # print ("element is present: " + str(check))
    # return count

print(search())
# driver.find_element_by_id("hplogo")
# driver.find_element_by_class_name("gLFyf.gsfi").send_keys("programming with python")
# driver.find_element_by_xpath("//img[@id='hplogo']")


# driver.quit()


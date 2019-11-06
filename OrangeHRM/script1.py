import time
from filecmp import cmp
'''
xpath:
absolute:/html/body/......
relative://


'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = "https://opensource-demo.orangehrmlive.com/index.php/auth/login"
location = "../drivers/"
driver = webdriver.Chrome(executable_path=location + 'chromedriver.exe')

action = ActionChains(driver)

def verifyWelcomeText(username, password):
    driver.get(url)
    # driver.maxmize_window()
    time.sleep(5)
    driver.find_element_by_name('txtUsername').send_keys(username)
    driver.find_element_by_name('txtPassword').send_keys(password)
    driver.find_element_by_name('Submit').click()
    welcomeText = driver.find_element_by_id('welcome').text
    print(welcomeText)
    if (welcomeText == "Welcome " + username):
        print("PASSED")
    else:
        print("FAILED")

    time.sleep(5)


# verifyWelcomeText("Admin", "admin123")

def CreateNewUser(username, password):
    def menus(menuNavigation):
        menuXpaths = []
        try:
            firstLevel = "//a[@class='firstLevelMenu']/b[text()='" + str(menuNavigation[0]) + "']"
            menuXpaths.append(firstLevel)
            secondLevel = firstLevel + "/../following-sibling::ul//a[text()='" + str(menuNavigation[1]) + "']"
            menuXpaths.append(secondLevel)
            thirdLevel = secondLevel + "/..//a[text()='" + str(menuNavigation[2]) + "']"
            menuXpaths.append(thirdLevel)
        except:
            print(menuXpaths)

        count = 0
        length = len(menuXpaths)
        for i in menuXpaths:
            element = driver.find_element_by_xpath(i)
            # if cmp(length-1,count) == 0:
            if count == length - 1:
                element.click()
            else:
                action.move_to_element(element).perform()
            count += 1

    driver.get(url)
    # driver.maxmize_window()
    time.sleep(2)
    driver.find_element_by_name('txtUsername').send_keys(username)
    driver.find_element_by_name('txtPassword').send_keys(password)
    driver.find_element_by_name('Submit').click()
    # menuItems = ["Admin", "User Management", "Users"]
    # menus(menuItems)
    menus(["PIM", "Add Employee"])
    # menus(["Admin", "User Management", "Users"])
    # action.move_to_element(driver.find_element_by_id("menu_admin_viewAdminModule")).perform()
    # action.move_to_element(driver.find_element_by_id("menu_admin_UserManagement")).perform()
    # action.move_to_element(driver.find_element_by_id("menu_admin_viewAdminModule")).click().perform()
    # driver. find_element_by_id('menu_admin_viewAdminModule').click()
    #
    # driver.find_elements_by_id('menu_admin_UserManagement').click()
    # driver.find_element_by_id('menu_admin_viewSystemUsers').click()
    time.sleep(2)
    driver.find_element_by_name('btnAdd').click()
    driver.find_element_by_id('systemUser_employeeName_empName').send_keys('a')
    driver.find_elements_by_id('systemUser_userName').send_keys('Test5')
    driver.find_element_by_id('systemUser_password').send_keys('Test66')
    driver.find_elements_by_id('systemUser_confirmPassword').send_keys('Test66')
    driver.find_element_by_id('btnSave').submit()
    # driver.find_element_by_id('welcome').click()
    # driver. find_element_by_id('menu_admin_viewAdminModule').click()
    # driver.find_elements_by_id('menu_admin_UserManagement').click()
    # driver.find_element_by_id('menu_admin_viewSystemUsers').click()#menu_admin_viewSystemUsers
    # driver.find_elements_by_id('searchSystemUser_userName').send_keys(username)
    # driver.find_element_by_xpath(".//option[@value='ESS']")

CreateNewUser("Admin", "admin123")





'''
---first level menu xpath
//*[@class='firstLevelMenu']/b[text()='Admin']

--second level menu xpath:
//a[@class='firstLevelMenu']/b[text()='Admin']/../following-sibling::ul//a[text()='User Management']


---third level menu xpath:
//a[@class='firstLevelMenu']/b[text()='Admin']/../following-sibling::ul//a[text()='Job']/..//a[text()='Job Title']
'''
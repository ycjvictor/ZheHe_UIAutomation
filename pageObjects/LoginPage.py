from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
from util.Log import *

class LoginPage:

    #获取loginPage页的所有元素
    def __init__(self, driver):
        self.driver = driver
        self.parseCF = ParseConfigFile()
        self.loginOptions = self.parseCF.getItemsSection('login')


    def userNameObj(self):
        try:
            locateType, locateExpression = self.loginOptions['loginPage.username'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素"+locateExpression)
            return element


    def passwordObj(self):
        try:
            locateType, locateExpression = self.loginOptions['loginPage.password'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element


    def loginButton(self):
        try:
            locateType, locateExpression = self.loginOptions['loginPage.loginButton'.lower()].split('>')
            element = getElement(self.driver, locateType, locateExpression)
        except Exception as e:
            logger.error(e)
        else:
            logger.info("找到元素" + locateExpression)
            return element



if __name__=="__main__":
    from selenium import webdriver
    import time

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)

    browser.get("http://47.96.183.143/#/login")
    browser.maximize_window()
    login = LoginPage(browser)
    browser.implicitly_wait(1)
    login.userNameObj().send_keys("yinchengjie")
    login.passwordObj().send_keys("123456")
    login.loginButton().click()
    time.sleep(1)
    # get the session cookie  
    # cookie = [item["name"]+"="+item["value"] for item in browser.get_cookies()]
    token = browser.execute_script('return sessionStorage.getItem("_token");')
    print(token)
    browser.quit()
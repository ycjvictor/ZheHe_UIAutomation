#coding=utf-8
from pageObjects.LoginPage import LoginPage
from util.Log import *
from selenium import webdriver
import time

class LoginAction:
    def __init__(self):
        logger.info("login..")

    @staticmethod
    def login(username, password, browser, source_url=None):
        '''
        登陆，并返回token且跳转到source_url
        :param username:
        :param password:
        :param browser:
        :param source_url:
        :return:登陆cookie
        '''
        try:

            # browser.get("https://plogin.m.jd.com/user/login.action")
            page = LoginPage(browser)
            page.userNameObj().send_keys(username)
            page.passwordObj().send_keys(password)
            page.loginButton().click()
            browser.implicitly_wait(1)

            while (1):
                # verify_code(browser)
                try:
                    # 这个条件不同情况下调用需要修改
                    browser.implicitly_wait(1)
                    # element = browser.find_element_by_xpath('// *[ @ class = "jcap_refresh"]')
                    element = browser.find_element_by_xpath('//*[@id="app"]//button')
                except Exception as e:
                    logger.info("登录成功！")
                    # get the session cookie  
                    # cookie = [item["name"] + "=" + item["value"] for item in browser.get_cookies()]
                    # print cookie  
                    # cookiestr = ';'.join(cookie)
                    browser.implicitly_wait(1)
                    token = browser.execute_script('return sessionStorage.getItem("_token");')
                    if source_url:
                        browser.get(source_url)
                    return token

        except Exception as e:
            logger.error(e)
            raise e
if __name__=="__main__":

    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=options)
    browser.get("http://47.96.183.143/#/login")
    browser.delete_all_cookies()
    token = LoginAction.login('yinchengjie', '123456', browser, "http://47.96.183.143/#/oa/home")
    # print(cookie)
    # for key, value in cookie.items():
    #     print(key, value)
    print(token)
    browser.quit()
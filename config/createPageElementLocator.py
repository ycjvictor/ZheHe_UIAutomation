# -*- coding: utf-8 -*-
# coding:utf-8
import configparser
import os
from config.getPageElement import getPageElement
from selenium import webdriver

class createPageElementLocator(object):


    def writenInI(self,browser):
        curpath = os.path.dirname(os.path.realpath(__file__))
        cfgpath = os.path.join(curpath, "cfg.ini")
        print(cfgpath)   # cfg.ini的路径

        # 创建管理对象
        conf = configparser.ConfigParser()

        # 添加一个select
        print(getPageElement().getPage(browser)[:-4])
        section = getPageElement().getPage(browser)[:-4]
        page =  getPageElement().getPage(browser)
        conf.add_section(section)
        print(conf.sections())

        # 往select添加key和value
        if(section):
            for one in getPageElement().getElement(browser):
                conf.set(section, page+"."+one[6:], "id>"+one)
                items = conf.items(section)
        print(items)    # list里面对象是元祖
        conf.write(open(cfgpath, "a"))   # 追加模式写入


if __name__ == '__main__':
    browser = webdriver.Chrome()

    browser.implicitly_wait(10)
    url = r'C:\Users\a\PycharmProjects\ZheHe_UIAutomation\数字建筑云平台login.html'
    browser.get(url)
    browser.maximize_window()

    ct = createPageElementLocator()
    ct.writenInI(browser)

    browser.quit()
# -*- coding: utf-8 -*-
# @Time : 2020-07-09 10:59
# @Author : Yinchengjie
# @Email : yinchengjie@zhehekeji.com
# @File: getPageElement.py
# @Project : ZheHe_UIAutomation
# @Software: PyCharm
import re
from selenium import webdriver

class getPageElement(object):

    def __init__(self):
        pass

    def getPage(self, browser):
        js_Page_script = '''
           function getPage(){
               var body = document.getElementsByTagName('body');
               return body[0].id;
               }
           return getPage()
           '''
        page = browser.execute_script(js_Page_script)
        return page

    def getElement(self, browser):
        js_Elemnt_script = '''
        function getElement(){
            var _docc = window.document.all;
            var body = document.getElementsByTagName('body');
            var arrayObj = new Array();
            // 遍历每一个对象
            for (var i=0 ;i<_docc.length;i++){
                if(_docc[i].id){
                arrayObj.push(_docc[i].id)
                }
            }
                return arrayObj
        }
        return getElement()
        '''
        Element_list = browser.execute_script(js_Elemnt_script)
        re_input_list = list(filter(lambda x: re.match('zhehe_input.*', x) != None, Element_list))  # 生成新列表
        input_dict = {}
        for one in re_input_list:
            input_Element = browser.find_element_by_id(one)
            input_dict[one] = input_Element
        return input_dict


if __name__ == '__main__':


    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    url = r'C:\Users\a\PycharmProjects\ZheHe_UIAutomation\数字建筑云平台login.html'
    browser.get(url)
    browser.maximize_window()
    getPageElement = getPageElement()

    print(getPageElement.getElement(browser))
    print(getPageElement.getPage(browser))

    browser.quit()

#coding=utf-8
import os
#获取当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取存放页面元素定位表达式文件的绝对路径
pageElementLocatorPath = parentDirPath+r"/config/PageElementLocator.ini"
#获取数据文件存放的绝对路径
dataFilePath = parentDirPath+r"/testData/测试数据.xlsx"



#测试数据.xlsx中登陆账号tab每列对应的数字序号
acount_username = 2
acount_password = 3
login_isExecute = 4
acount_comment = 5
execute_testResult = 6
execute_time = 7



if __name__=="__main__":
    print(pageElementLocatorPath)
    print(dataFilePath)
    print(parentDirPath)

#!/usr/bin/python2
# coding: utf8
''' CLI Version '''

def main():
    pass


def JWCInterface():
    # firstly login
    if os.path.exists("JWCConf"):
        # getConf()
        print "getconf"
        conf = open("JWCConf","r").readlines()
        StuID = conf[0]
        StuPW = conf[1]
    else :
        # writeConf()
        print("无本地配置！开始登录...")
        StuID = raw_input("输入学号 Input your StudentID ：")
        StuPW = raw_input("输入密码 Input your StudentPW ：")
        conf = open("JWCConf","w+")
        conf.write(StuID + "\n")
        conf.write(StuPW + "\n")
    import JWC_login
    cookie = JWC_login.Login(StuID,StuPW)
    if cookie is False :
        print("错误的账户或密码！")
        os.remove(JWCConf)
    else :
        selectJWCFunctions(cookie)

def selectJWCFunctions(cookie):
    print("选择功能 Select the Function")
    listOfFunctions = '''
        JWC function 列表：
 		1.教务处改密码
 		2.？？？
 		3.？？？
    '''

def URPInterface():
    pass


if __name__ == '__main__':
    import sys
    import os

    platform = raw_input("选择登录平台 [1]教务处 [2]信息门户 \nInput Platform to Login [1]JWC [2]URP \n>>>  ")
    print platform
    if platform is "1" :
        JWCInterface()
    elif platform is "2" :
        URPInterface()
    else :
        print("错误的平台代码！")

    # main()


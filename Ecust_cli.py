#!/usr/bin/python2
# coding: utf8
''' CLI Version , Please DO NOT import this file ! '''

def JWCInterface():
    # firstly login
    import JWC_login as login
    import JWC_functions as function
    if (os.path.exists("JWC.conf")):
        # getConf()
        print "getconf"
        conf = open("JWC.conf","r").readlines()
        StuID = conf[0]
        StuPW = conf[1]
    else :
        # writeConf()
        print("无本地配置！开始登录...")
        StuID = raw_input("输入学号 Input your StudentID ：")
        StuPW = raw_input("输入密码 Input your StudentPW ：")
        conf = open("JWC.conf","w+")
        conf.write(StuID + "\n")
        conf.write(StuPW + "\n")
    cookie = login.Login(StuID,StuPW)
    if cookie is False :
        print("错误的账户或密码！")
        os.remove(JWC.conf)
    else :
        print("登录成功～")
        selectJWCFunctions(cookie)

def selectJWCFunctions(cookie):
    print("登录成功，可选择功能 \nSelect the Function")
    listOfFunctions = '''
        JWC function 列表：
        1.教务处改密码
        2.？？？
        3.？？？
        T.Mini Tools
    '''
    functionID = raw_input(listOfFunctions)
    # print platform
    if functionID is "1" :
        newPW = raw_input("type your NEW password:")
        function.changePW(login_cookie,newPW)
        pass
    elif functionID is "2" :
        pass
    else :
        print("错误的功能代码！")

def URPInterface():
    # firstly login
    import URP_login as login
    import URP_functions as function
    if os.path.exists("URP.conf") :
        # getConf()
        print "getconf"
        conf = open("URP.conf","r").readlines()
        StuID = conf[0]
        StuPW = conf[1]
    else :
        # writeConf()
        print("无本地配置！开始登录...")
        StuID = raw_input("输入学号 Input your StudentID ：")
        StuPW = raw_input("输入密码 Input your StudentPW ：")
        conf = open("URP.conf","w+")
        conf.write(StuID + "\n")
        conf.write(StuPW + "\n")
    cookie = login.Login(StuID,StuPW)
    if cookie is False :
        print("错误的账户或密码！")
        os.remove(URP.conf)
    else :
        print("登录成功～")
        selectURPFunctions(cookie)


def selectURPFunctions(cookie):
    print("登录成功，可选择功能 \nSelect the Function")
    listOfFunctions = '''
        URP function 列表：
        1.教务处改密码
        2.？？？
        3.？？？
        T.Mini Tools
    '''
    pass 

def main():
    import sys
    import os

    platform = raw_input("选择登录平台 [1]教务处 [2]信息门户 \nInput Platform to Login [1]JWC [2]URP \n>>>  ")
    # print platform
    if platform is "1" :
        JWCInterface()
    elif platform is "2" :
        URPInterface()
    else :
        print("错误的平台代码！")


if __name__ == '__main__':
    main()

    # try:
    #   options,args = getopt.getopt(sys.argv[1:],"l:f:i:p:",["login=", "function=", "id=", "password="])
    # except getopt.GetoptError:
    #   sys.exit()
    # for name,value in options:
    #   if name in ("-l","--login"):
    #       platformID = value
    #       if value is '1':
    #           import JWC_login as login
    #           import JWC_functions as function
    #           pass
    #       elif value is '2':
    #           import URP_login as login
    #           import URP_function as function
    #       else :
    #           sys.exit("NO LOGIN!")
    #   if name in ("-f", "--function"):
    #       funcID = value
    #   if name in ("-i", "--id"):
    #       stuID = value
    #   if name in ("-p", "--password"):
    #       stuPW = value
    # main(platformID, funcID, stuID, stuPW)
    # pass

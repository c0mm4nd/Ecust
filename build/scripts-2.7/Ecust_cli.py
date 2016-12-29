#!python
# coding: utf8
""" CLI Version , Please DO NOT import this file ! """


def jwc_interface():
    """ JWC """
    # firstly login
    import jwc_login as login
    import os
    if os.path.exists("JWC.conf"):
        # getConf()
        print "getconf"
        conf = open("JWC.conf", "r").readlines()
        stu_id = conf[0]
        stu_pw = conf[1]
    else:
        # writeConf()
        print("无本地配置！开始登录...")
        stu_id = raw_input("输入学号 Input your StudentID ：")
        stu_pw = raw_input("输入密码 Input your StudentPW ：")
        conf = open("JWC.conf", "w+")
        conf.write(stu_id + "\n")
        conf.write(stu_pw + "\n")
    cookie = login.jwc_login(stu_id, stu_pw)
    if cookie is False:
        print("错误的账户或密码！")
        os.remove("JWC.conf")
    else:
        print("登录成功～")
        select_jwc_functions(cookie)


def select_jwc_functions(cookie):
    import jwc_functions as function
    print("登录成功，可选择功能 \nSelect the Function")
    list_of_functions = '''
        JWC function 列表：
        1.教务处改密码
        2.？？？
        3.？？？
        T.Mini Tools
    '''
    function_id = raw_input(list_of_functions)
    # print platform
    if function_id is "1":
        new_pw = raw_input("type your NEW password:")
        function.change_password(cookie, new_pw)
        pass
    elif function_id is "2":
        pass
    else:
        print("错误的功能代码！")


def urp_interface():
    # firstly login
    import urp_login as login
    import os
    if os.path.exists("URP.conf"):
        # getConf()
        print "getconf"
        conf = open("URP.conf", "r").readlines()
        stu_id = conf[0]
        stu_pw = conf[1]
    else:
        # writeConf()
        print("无本地配置！开始登录...")
        stu_id = raw_input("输入学号 Input your StudentID ：")
        stu_pw = raw_input("输入密码 Input your StudentPW ：")
        conf = open("URP.conf", "w+")
        conf.write(stu_id + "\n")
        conf.write(stu_pw + "\n")
    cookie = login.urp_login(stu_id, stu_pw)
    if cookie is False:
        print("错误的账户或密码！")
        os.remove("URP.conf")
    else:
        print("登录成功～")
        select_urp_functions(cookie)


def select_urp_functions(cookie):
    print("登录成功，可选择功能 \nSelect the Function")
    list_of_functions = '''
        URP function 列表：
        1.教务处改密码
        2.？？？
        3.？？？
        T.Mini Tools
    '''
    pass 


def main():
    import os
    platform = raw_input("选择登录平台 [1]教务处 [2]信息门户 \nInput Platform to urp_login [1]JWC [2]URP \n>>>  ")
    # print platform
    if platform is "1":
        jwc_interface()
    elif platform is "2":
        urp_interface()
    else:
        print("错误的平台代码！")


if __name__ == '__main__':
    main()

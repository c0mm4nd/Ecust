#!/usr/bin/python2
# coding:utf8
"""教务处**综合查询**工具合集"""
import requests
from lxml import etree

import jwc_login


# login_cookie = JWC_login.urp_login(stuID, stuPW)

def change_password(login_cookie, new_pw):
    url = 'http://202.120.108.14/ecustedu/StudentChangePassword.aspx'
    get = requests.get(url, cookies=login_cookie)
    root = etree.HTML(get.text)
    viewstate_tag = root.xpath("//*[@id='__VIEWSTATE']")
    viewstate = viewstate_tag[0].attrib['value']
    eventvalidation_tag = root.xpath("//*[@id='__EVENTVALIDATION']")
    eventvalidation = eventvalidation_tag[0].attrib['value']
    params = {
        '__VIEWSTATE': viewstate,
        'txtNewPwd1': new_pw,
        'txtNewPwd2': new_pw,
        'BtnOK': '提交',
        '__EVENTVALIDATION': eventvalidation,
    }
    requests.post(url, data=params, cookies=login_cookie)
    pass


def get_class_table(login_cookie, term="this"):
    if term is "this":
        term = "下学期"
    elif term is "last":
        term = "本学期"
    else:
        exit()
    url = "http://202.120.108.14/ecustedu/E_SelectCourse/ScInFormation/syllabus.aspx"
    get = requests.get(url, cookies=login_cookie)
    root = etree.HTML(get.text)
    viewstate_tag = root.xpath("//*[@id='__VIEWSTATE']")
    viewstate = viewstate_tag[0].attrib['value']
    eventvalidation_tag = root.xpath("//*[@id='__EVENTVALIDATION']")
    eventvalidation = eventvalidation_tag[0].attrib['value']
    params = {
        '__VIEWSTATE': viewstate,
        'selyeartermflag': term,
        'bttn_search': '查询',
        '__EVENTVALIDATION': eventvalidation,
    }
    result = requests.post(url, data=params, cookies=login_cookie)
    table_root = etree.HTML(result.text)
    time12_classes = table_root.xpath("//table[@id='TblSyllabus']/tr[2]/td")
    # time1 = ['', '', '', '', '', '', '']
    # time2 = time1
    # time3 = time1
    # time4 = time1
    # time5 = time1
    # time6 = time1
    i = 1
    time12 = []
    time34 = []
    time56 = []
    time78 = []
    time910 = []
    time1112 = []

    time12_classes = table_root.xpath("//table[@id='TblSyllabus']/tr[2]/td")
    for the_class in time12_classes:
        time12.append(the_class.text)

    time34_classes = table_root.xpath("//table[@id='TblSyllabus']/tr[4]/td")
    for the_class in time34_classes:
        time34.append(the_class.text)

    time56_classes = table_root.xpath("//table[@id='TblSyllabus']/tr[6]/td")
    for the_class in time56_classes:
        time56.append(the_class.text)

    time78_classes = table_root.xpath("//table[@id='TblSyllabus']/tr[8]/td")
    for the_class in time78_classes:
        time78.append(the_class.text)

    time910_classes = table_root.xpath("//table[@id='TblSyllabus']/tr[10]/td")
    for the_class in time910_classes:
        time910.append(the_class.text)

    time1112_classes = table_root.xpath("//table[@id='TblSyllabus']/tr[12]/td")
    for the_class in time1112_classes:
        time1112.append(the_class.text)

    del time12[0]
    del time34[0]
    del time56[0]
    del time78[0]
    del time910[0]
    del time1112[0]
    table = [time12, time34, time56, time78, time910, time1112]

    return table


if __name__ == '__main__':
    stuID = 10142045
    stuPW = 10142045
    cookie = jwc_login.jwc_login(stuID, stuPW)
    # print
    get_class_table(cookie)

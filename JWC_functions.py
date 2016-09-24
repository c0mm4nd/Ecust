#!/usr/bin/python2
# coding:utf8
import JWC_login
import requests
from lxml import etree
"教务处综合查询工具合集"

# login_cookie = JWC_login.Login(stuID, stuPW)

def changePW(login_cookie, newPW):
	url = 'http://202.120.108.14/ecustedu/StudentChangePassword.aspx'
	get = requests.get(url, cookies=login_cookie)
	root = etree.HTML(get.text)
	viewstate_tag = root.xpath("//*[@id='__VIEWSTATE']")
	viewstate = viewstate_tag[0].attrib['value']
	eventvalidation_tag = root.xpath("//*[@id='__EVENTVALIDATION']")
	eventvalidation = eventvalidation_tag[0].attrib['value']
	params = {
		'__VIEWSTATE':viewstate,
		'txtNewPwd1':newPW,
		'txtNewPwd2':newPW,
		'BtnOK':'提交',
		'__EVENTVALIDATION':eventvalidation,
	}
	requests.post(url, data=params, cookies=login_cookie)
	pass


if __name__ == '__main__':
	stuID=10142045
	stuPW=951120
	cookie = JWC_login.Login(stuID, stuPW)
	changePW(cookie, '10142045')

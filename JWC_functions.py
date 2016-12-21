#!/usr/bin/python2
# coding:utf8
import JWC_login
import requests
from lxml import etree
'''教务处**综合查询**工具合集'''

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

def getClassTable(login_cookie, term="this"):
	if term is "this":
		term = "下学期"
	elif term is "last":
		term = "本学期"
	else :
		exit
	url = "http://202.120.108.14/ecustedu/E_SelectCourse/ScInFormation/syllabus.aspx"
	get = requests.get(url, cookies=login_cookie)
	root = etree.HTML(get.text)
	viewstate_tag = root.xpath("//*[@id='__VIEWSTATE']")
	viewstate = viewstate_tag[0].attrib['value']
	eventvalidation_tag = root.xpath("//*[@id='__EVENTVALIDATION']")
	eventvalidation = eventvalidation_tag[0].attrib['value']
	params = {
		'__VIEWSTATE':viewstate,
		'selyeartermflag':term,
		'bttn_search':'查询',
		'__EVENTVALIDATION':eventvalidation,
	}
	result = requests.post(url, data=params, cookies=login_cookie)
	table_root = etree.HTML(result.text)
	time12Classes = table_root.xpath("//table[@id='TblSyllabus']/tr[2]/td")
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

	time12Classes = table_root.xpath("//table[@id='TblSyllabus']/tr[2]/td")
	for theClass in time12Classes:
		time12.append(theClass.text)

	time34Classes = table_root.xpath("//table[@id='TblSyllabus']/tr[4]/td")
	for theClass in time34Classes:
		time34.append(theClass.text)

	time56Classes = table_root.xpath("//table[@id='TblSyllabus']/tr[6]/td")
	for theClass in time56Classes:
		time56.append(theClass.text)

	time78Classes = table_root.xpath("//table[@id='TblSyllabus']/tr[8]/td")
	for theClass in time78Classes:
		time78.append(theClass.text)

	time910Classes = table_root.xpath("//table[@id='TblSyllabus']/tr[10]/td")
	for theClass in time910Classes:
		time910.append(theClass.text)

	time1112Classes = table_root.xpath("//table[@id='TblSyllabus']/tr[12]/td")
	for theClass in time1112Classes:
		time1112.append(theClass.text)

	del time12[0]
	del time34[0]
	del time56[0]
	del time78[0]
	del time910[0]
	del time1112[0]
	table = [time12, time34, time56, time78, time910, time1112 ]

	return table



if __name__ == '__main__':
	stuID=10142045
	stuPW=10142045
	cookie = JWC_login.Login(stuID, stuPW)
	print getClassTable(cookie)

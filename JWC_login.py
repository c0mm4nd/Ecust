# coding:utf8
import requests
import mechanize
from lxml import etree
import cookielib

# stuID = 10142045
# stuPW = 10142045
def Login(stuID, stuPW):
	# 第一种方法
	x = primaryMethod(stuID, stuPW)
	if x:
		return x  
		pass
	else : 
		x = standbyMethod(stuID, stuPW)
		return x
		pass
	pass

def primaryMethod(stuID, stuPW):
	get_url = "http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentQueryLogin.aspx"
	get = requests.get(get_url)
	root = etree.HTML(get.text)
	viewstate_tag = root.xpath("//*[@id='__VIEWSTATE']")
	viewstate = viewstate_tag[0].attrib['value']
	eventvalidation_tag = root.xpath("//*[@id='__EVENTVALIDATION']")
	eventvalidation = eventvalidation_tag[0].attrib['value']

	url_ggcx_login = "http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentQueryLogin.aspx"
	payload = {
		'TxtStudentId': stuID,
		'TxtPassword': stuPW,
		'__EVENTVALIDATION': eventvalidation,
		'__VIEWSTATE': viewstate,
		'BtnLogin':'登录'}
	r = requests.post(url_ggcx_login, data=payload)
	text = r.text.encode("utf8")
	if validateLogin(text) :
		return r.cookies
	else :
		return False
	pass

def standbyMethod(stuID, stuPW):
	br = mechanize.Browser()
	cookiejar = cookielib.CookieJar()
	br.set_cookiejar(cookiejar)  
	br.set_handle_equiv(True)  
	br.set_handle_redirect(True)  
	br.set_handle_referer(True)  
	br.set_handle_robots(False)  
	br.open("http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentQueryLogin.aspx")
	br.select_form(name="Form1")
	br["TxtStudentId"] = '10142045'
	br["TxtPassword"] = '10142045'
	response = br.submit()
	text = response.read()
	if validateLogin(text) :
		return cookiejar
	else :
		return False
	pass

def validateLogin(x):
	signal = "您好"
	if x.find(signal) >0 :
		# print 'login success'
		# for i in cookiejar
		# 	print i
		return True
	else :
		# print 'login failed'
		return False
	pass

# jar = requests.cookies.RequestsCookieJar()
# print vars(r.cookies)


# a = Login(stuID, stuPW)
# print vars(a)

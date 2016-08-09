# coding:utf8
import requests
import mechanize
# import lxml
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
	url_ggcx_login = "http://202.120.108.14/ecustedu/K_StudentQuery/K_StudentQueryLogin.aspx"
	payload = {'TxtStudentId': stuID, 'TxtPassword': stuPW, '__EVENTVALIDATION': '/wEWBALplYnsCgK/ycb4AQLVqbaRCwLi44eGDNL1/UVfta6zTJ9DMRXMNe6Ao6Wm', '__VIEWSTATE': '/wEPDwUJMTg2MzE1NTYyD2QWAgIBD2QWAgIGDw8WAh4EVGV4dAVQ5a2m55Sf5Yid5aeL5a+G56CB5Li66Lqr5Lu96K+B5Y+35ZCO5YWt5L2N44CC5a+G56CB6ZW/5bqm5LiN6LaF6L+HMTDkuKrlrZfnrKbjgIJkZGTItFe6UDnNqdE2sz592HXKwZ7Fhw==', 'BtnLogin':'登录'}
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

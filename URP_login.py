#!/usr/bin/python2
# coding:utf8

''' 信息门户登录 '''
''' http://urp.ecust.edu.cn '''
import requests
# from lxml import etree

# print "test"
# req = requests.Session()
# url = "http://urp.ecust.edu.cn/"
# r = req.get(url,  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'})
# print r.text.encode('utf8')
# rt = etree.HTML(r.text)
# xpath = rt.xpath("//img[@id='captchaImg']")
# 吐槽：妈的又是个当摆设的验证码设计……
def Login(stuID, stuPW):
	url = "http://urp.ecust.edu.cn/userPasswordValidate.portal"
	params = {
		"Login.Token1":stuID,
		"Login.Token2":stuPW,
		"goto":"http://urp.ecust.edu.cn/loginSuccess.portal",
		"gotoOnFail":"http://urp.ecust.edu.cn/loginFailure.portal",
	}
	req = requests.Session()
	req.post(url, data=params)

	r = req.get("http://urp.ecust.edu.cn/index.portal")
	text = r.text.encode('utf8')
	if validateLogin(text) :
		return r.cookies
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

# coding:utf8
import requests
import mechanize
import lxml
import cookielib

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
x = response.read()
signal = "您好"
if x.find(signal) >0 :
	print 'login success'
	# for i in cookiejar:
	# 	print i
else :
	print 'login failed'
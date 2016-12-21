#!/usr/bin/python2
# coding: utf8

import sys
import getopt

def main(platformID, funcID, stuID, stuPW):
	'''
	Run in CLI Version:
	python Ecust.py [args]

	'''
	login_cookie = login.Login(stuID, stuPW)
	print vars(login_cookie)
	functionRunner(platformID, funcID, login_cookie)


def functionRunner(platformID, funcID, login_cookie):
	'''
	platformID = 1:
		JWC Function Lists:
		1.Change the password of the URL of jwc.ecust.edu.cn
		2.???
		3.???
	platformID = 2: 
		URP Function Lists:
		1.???
		2.???
	'''
	if platformID is 1 :
		if funcID is 1:
			newPW = raw_input("type your NEW password:")
			function.changePW(login_cookie,newPW)
			pass
		else :
			sys.exit()
	if platformID is 2 :
		pass

class Ecust(object):
	"""import ME"""
	def __init__(self, arg):
		super(Ecust, self).__init__()
		self.arg = arg

	def Ecust(platformID, stuID, stuPW):
		'''
		Login Module for the import action 
		Args:
			platformID :
				1 : JWC
				2 : URP
			stuID : Your Student ID 
			stuPW : Your Student Password of the Student ID
		Return :
			a cookie if it succeed , or False.
		'''
		if platformID is '1':
			import JWC_login as login
			import JWC_functions as function
			pass
		elif platformID is '2':
			import URP_login as login
			import URP_function as function
		else :
			sys.exit("NO LOGIN!")
		login_cookie = login.Login(stuID, stuPW)
		# print vars(login_cookie)
		return login_cookie

	

if __name__ == '__main__':
	try:
		options,args = getopt.getopt(sys.argv[1:],"l:f:i:p:",["login=", "function=", "id=", "password="])
	except getopt.GetoptError:
		sys.exit()
	for name,value in options:
		if name in ("-l","--login"):
			platformID = value
			if value is '1':
				import JWC_login as login
				import JWC_functions as function
				pass
			elif value is '2':
				import URP_login as login
				import URP_function as function
			else :
				sys.exit("NO LOGIN!")
		if name in ("-f", "--function"):
			funcID = value
		if name in ("-i", "--id"):
			stuID = value
		if name in ("-p", "--password"):
			stuPW = value
	main(platformID, funcID, stuID, stuPW)
	pass

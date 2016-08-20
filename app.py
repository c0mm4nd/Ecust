# coding: utf8
''' CLI Version '''
import sys
import getopt

def main(loginID, funcID, stuID, stuPW):
	login_cookie = login.Login(stuID, stuPW)
	print vars(login_cookie)
	functionSelector(loginID, funcID, login_cookie)


def functionRunner(loginID, funcID, login_cookie):
	if loginID is 1 :
		'''
		JWC function 列表：
		1.教务处改密码
		2.？？？
		3.？？？

		'''
		if funcID is 1:
			newPW = raw_input("type your NEW password:")
			function.changePW(login_cookie,newPW)
			pass
		else :
			sys.exit()

	if loginID is 2 :
		'''
		URP function 列表：
		1.？？？
		2.？？？

		'''
		pass

if __name__ == '__main__':
	try:
		options,args = getopt.getopt(sys.argv[1:],"l:f:i:p:",["login=", "function=", "id=", "password="])
	except getopt.GetoptError:
		sys.exit()

	for name,value in options:
		if name in ("-l","--login"):
			loginID = value
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
	main(loginID, funcID, stuID, stuPW)	
	pass


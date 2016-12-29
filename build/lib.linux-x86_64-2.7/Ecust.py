# coding: utf8

class Ecust(object):
	"""import ME """
	# def __init__(self, platformID = ):
	# 	super(Ecust, self).__init__()
	# 	self.platformID = platformID

	def __init__(self, platformID, stuID, stuPW):
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


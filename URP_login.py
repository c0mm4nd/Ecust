# coding:utf8
# from PIL import Image as Img
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

url = "http://urp.ecust.edu.cn/userPasswordValidate.portal"
params = {
	"Login.Token1":10142045,
	"Login.Token2":951120,
	"goto":"http://urp.ecust.edu.cn/loginSuccess.portal",
	"gotoOnFail":"http://urp.ecust.edu.cn/loginFailure.portal",
}
req = requests.Session()
req.post(url, data=params)

r = req.get("http://urp.ecust.edu.cn/index.portal")
print r.text.encode("utf8")

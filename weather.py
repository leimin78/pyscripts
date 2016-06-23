# -*- coding:utf-8 -*-

import requests
from lxml import etree
import sys

reload(sys)
sys.setdefaultencoding('utf-8') 

#Global Value

head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
url = 'http://www.weather.com.cn/textFC/hn.shtml'

def GetProvinceUrl(Province):
	obj = etree.HTML(requests.get(url,headers= head).content)
	provincename = '//*[@class="lqcontentBoxheader"]//ul//li//a/text()'
	provinceurl = '//*[@class="lqcontentBoxheader"]//ul//li/a/@href'
	
	pdict = dict(zip(obj.xpath(provincename),obj.xpath(provinceurl)))

	'''for name in obj.xpath(provincename):
		print name

	for purl in obj.xpath(provinceurl):
		print purl'''
	base_url = "http://www.weather.com.cn"
	province_url = base_url + pdict[Province]
	return province_url

def GetCityUrl(province_url):
	obj = etree.HTML(requests.get(province_url,headers=head).content)
	cityname = '//*[@class="hanml"]//tr/td/a/text()'
	city_url = {}
	for name in set(obj.xpath(cityname)):
		cityurl='//*[@class="hanml"]//tr/td/a[text()='+"'"+name+"'"+']/@href'
		if name == u'详情':
			continue
		#print cityurl
		else:
			for url in set(obj.xpath(cityurl)):
				city_url[name] = url
	return city_url

def GetWeather(name,cityurl):
	obj=etree.HTML(requests.get(cityurl,headers=head).content)
	cityname = name
	weatherule='//*[@class="c7d"]/input[1]/@value'
	cityweather=''.join(obj.xpath(weatherule))
	print "城市: %s : %s" %(name,cityweather)



if __name__ == '__main__':
	Province = raw_input(u'请输入省份:').decode(sys.stdin.encoding)
	province_url =  GetProvinceUrl(Province)
	Cityname=raw_input(u'请输入城市名:').decode(sys.stdin.encoding)
	Cityurl = GetCityUrl(province_url)[Cityname]
	GetWeather(Cityname,Cityurl)

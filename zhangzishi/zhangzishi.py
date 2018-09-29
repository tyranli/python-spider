import requests
from bs4 import BeautifulSoup
import os,time

URL = 'http://www.zhangzishi.cc/category/welfare/page/'
RECORD = '='*20 + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '='*20 + '\n'

def getlist(page):
	global RECORD

	req = requests.get(URL + str(page))
	soup = BeautifulSoup(req.text , 'html.parser')
	pagelist = soup.select('.excerpt h2 a')
	pagetime = soup.select('footer time')
	# print(pagelist,pagetime)

	for i in range(0,len(pagelist)):
		pageurl = pagelist[i]['href']
		title = pagelist[i].text.split('\u200b')[0].strip()
		time = pagetime[i].text
		filepath = 'media/'+time+'.'+title
		try:
			os.mkdir(filepath)
			print(page,time+title+'>>>获取中：')
			RECORD += time+title+pageurl+'\n' 
			getpic(pageurl,filepath)
		except Exception : 
			print(time+title+'>>>已存在,跳过')
			RECORD += time+title+'>>>已存在,跳过\n'

def getpic(pageurl,filepath):
	global RECORD

	soup = BeautifulSoup(requests.get(pageurl).text , 'html.parser')
	picurl = soup.select('.article-content img')
	for i in range(0,len(picurl)-1):
		onepic = picurl[i]['src']
		#有些链接带了‘http’，没有就加上
		if onepic.find('http') != -1 :	pass
		else : onepic = 'http:'+onepic
		print(onepic)
		#判断图片扩展名，并保存
		pictype = onepic[onepic.rindex('.'):]
		savepath = filepath + '/pic_' + str(i) + pictype
		try:
			with open(savepath, 'wb') as file :
				file.write(requests.get(onepic).content)
			file.close()
			print(savepath + '>>>保存成功')
			RECORD += '>>>pic_' + str(i) + '@' + onepic + '>>>成功\n'
		except Exception as e:
			print(savepath + '>>>保存失败')
			RECORD += '>>>pic_' + str(i) + '@' + onepic + '>>>失败\n' + str(e)+'\n'
# =========test==========
# testurl = 'http://www.zhangzishi.cc/20180821jj.html'
# getlist(0)
# filepath = '2018-08-21.气质小姐姐'
# os.mkdir(filepath)
# getpic(testurl,filepath)

# =========main==========
for i in range(6,11):
	getlist(i)

with open('RECORD.txt','a') as file:
	file.write(RECORD)
file.close()
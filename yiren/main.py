import os,sys
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

URL = 'http://www.yiren21.com/se/yazhousetu/'	#亚洲
headers = {
'User-Agent' : 'mozilla/5.0 (linux; u; android 4.1.2; zh-cn; mi-one plus build/jzo54k) applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534.30 micromessenger/5.0.1.352'
}

def getlist(page):
	if page==0 : res = requests.get(URL)
	else : res = requests.get(URL+'index_'+str(page+1)+'.html')
	soup = BeautifulSoup(res.text.encode('raw_unicode_escape'),'html.parser')
	# 以utf8编码的字符串被当成unicode编码的字符串放进unicode对象里去了,用.encode('raw_unicode_escape')解开得到utf8编码。
	url_list = soup.select('.textList li a')
	date_list = soup.select('.textList li a span')
	for i in range(1,len(url_list)):
		date = date_list[i].text
		title = (url_list[i]['title'])
		url = (URL + url_list[i]['href'][15:])
		getpic(date,title,url)
		# print(date,title,url)

# 获取每一页图片
def getpic(date,title,url):
	piclink = BeautifulSoup(requests.get(url).text,'html.parser').select('.t_f img')

	# 创建文件夹，如果已存在则跳过
	try: os.mkdir('media/' + date)
	except Exception as e: pass
	try: os.mkdir('media/' + date +'/'+title)
	except Exception as e: pass

	for i in range(1,len(piclink)):
		picurl = piclink[i]['src']
		print(picurl)

	# # 设置图片存放路径，下载图片，如果存在则跳过。网络问题无法下载
	# 	picpath = 'media/' + date + '/' + title + '/' + str(i) + '.jpg'
	# 	if os.path.exists(picpath) : print(str(i),'.jpg已存在')
	# 	else:
	# 		with open(picpath, 'wb') as file:
	# 			file.write(requests.get(picurl,headers=headers).content)
	# 			file.close()

# 主程序开始
# for i in range(3,len(title)):
# 	url_single = []
# 	getpic(title[i],url[i],'')


# 异步处理主程序
# if __name__ == '__main__':
# 	pool = Pool(processes=2)
# 	for i in range(0,3) :
# 		pool.apply_async(getpic,args=(title[i],url[i],'',))
# 	pool.close()
# 	pool.join()

# getlist(50)

getpic('2018-08-29','卢埃巴【20P】','http://www.yiren21.com/se/yazhousetu/621659.html')
import requests
from bs4 import BeautifulSoup
import os,time

headers = {
	'Referer': 'http://www.jder.net/cosplay/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

def arti_list(page):
	URL = 'http://www.jder.net/cosplay-cat/page/' + str(page)
	soup = BeautifulSoup(requests.get(URL).text,'html.parser')
	arti = soup.select('.picture-box h2 a')
	arti_url = []
	for i in arti : arti_url.append(i['href'])
	# print(arti_url,len(arti_url))
	for i in range(0,len(arti_url)) : 
		# 因为1篇文章有可能分2页，所以先获取所有图片列表，再调用下载程序
		piclist = []
		(title ,piclink) = pic_list(arti_url[i],1,piclist)
		# print(title,piclink)
		print(page, i, title, '开始下载')
		pic_down(title+str(i),piclink)

		time.sleep(5)

def pic_list(arti_url,i,piclist):
	soup = BeautifulSoup(requests.get(arti_url+'/'+str(i)).text,'html.parser')
	title = soup.select('header h1')[0].text.replace(' ','-').replace(':','：').replace('/','·')
	picurl = soup.select('.single-content img')
	# print(picurl)
	for picurl in picurl : 
		try:
			link = picurl['src']
			if link.find('http') == -1 : link = 'http:'+link
			piclist.append(link)
		except Exception : pass
	# 判断是否有下一页，嵌套执行，最终返回所有图片连接列表
	nextpage = soup.select('.page-links i')
	if str(nextpage).find('right') != -1 : pic_list(arti_url,i+1,piclist)

	return title,piclist

def pic_down(pictitle,piclink):
	# 创建文件夹，如果已存在则跳过
	dirpath = 'media/' + pictitle
	try : os.mkdir(dirpath)
	except Exception : pass
	
	# 根据传入的图片链接开始下载
	for i in range(0,len(piclink)):
		# 设置图片存放路径，下载图片，如果存在则跳过
		picsave = dirpath + '/' + str(i+1) + '.jpg'
		# print(piclink[i],picsave)
		if os.path.exists(picsave) : print(picsave,'已存在')
		else:
			try:
				img = requests.get(piclink[i],headers=headers)
				# print(img)
				with open(picsave, 'wb') as file:
					file.write(img.content)
				file.close()
			except Exception : pass


# =========test==========
# page = [21,42,42]
# num  = [14, 7,12]
# for i in range(0,len(page)):
# 	arti_list(page[i],num[i])

# =========main==========
for i in range(0,1):
	arti_list(i)
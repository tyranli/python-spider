import requests,os,time
from bs4 import BeautifulSoup
# from multiprocessing import Pool

headers = {
	# 'Host':'www.mmjpg.com',
	# 'Connection':'keep-alive',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	# 'Accept':'*/*',
	'Referer':'http://www.mmjpg.com/mm/',  # 'Referer'是关键，告诉服务器我是从哪个页面链接过来，才会得到正确的respond
	# 'Accept-Encoding':'gzip, deflate',
	# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}

def getlist(artical_num):
	# 获取基础信息
	URL = 'http://www.mmjpg.com/mm/' + str(artical_num)
	soup = BeautifulSoup(requests.get(URL).text.encode('raw_unicode_escape'),'html.parser')
	title = soup.select('.article h2')[0].text	#.replace('?',',')
	year = soup.select('.info i')[0].text[5:][:4]
	# print(title)
	if artical_num<1256 :
	# 1255之前图片链接形式为：http://fm.shiyunjj.com/2018/1255/[1,2,3].jpg
		picnum = soup.select('.page a')[6].text
		piclink = []
		for i in range(1,int(picnum)+1):
			piclink.append('http://fm.shiyunjj.com/'+year+'/'+str(artical_num)+'/'+str(i)+'.jpg')
		# print(piclink)
	else :
	# 1255之后，图片为XHR加载，图片地址加了随机编码
		URL = 'http://www.mmjpg.com/data.php?id='+ str(artical_num) +'&page=8999'
		req = requests.get(URL,headers=headers)
		code = req.text.split(',')
		piclink = []
		for i in range(0,len(code)):
		# 地址为：http://fm.shiyunjj.com/2018/1256/[1,2,3]+i+随机编码.jpg
			piclink.append('http://fm.shiyunjj.com/'+year+'/'+str(artical_num)+'/'+str(i+1)+'i'+code[i]+'.jpg')
		# print(piclink)

	# 执行下载图片
	print(artical_num,title,'开始下载')
	picdown(str(artical_num)+'.'+title,piclink)

def picdown(pictitle,piclink):
	# 创建文件夹，如果已存在则跳过
	try: os.mkdir('media/' + pictitle)
	except Exception: pass
	# 根据传入的图片链接开始下载
	for i in range(0,len(piclink)):
		# 设置图片存放路径，下载图片，如果存在则跳过
		picsave = 'media/' + pictitle + '/' + str(i+1) + '.jpg'
		# print(piclink[i],picsave)
		if os.path.exists(picsave) : print(picsave,'已存在')
		else:
			img = requests.get(piclink[i],headers=headers)
			with open(picsave, 'wb') as file:
				file.write(img.content)
			file.close()
			# time.sleep(1)

# =============main=============
for i in range(1257,1486) :
	getlist(i)
	time.sleep(10)


# 异步处理主程序
# if __name__ == '__main__':
# 	pool = Pool(processes=3)
# 	for i in range(6,100) :
# 		pool.apply_async(getlist,args=(i,))
# 	pool.close()
# 	pool.join()

# 加入休眠时间，反爬措施限制了
import os
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

URL = 'http://manhua.fzdm.com/39/'
res = requests.get(URL)
soup = BeautifulSoup(res.text,'html.parser')
url_list = soup.select('#content li a')
title = []
url = []
for i in range(0,len(url_list)):
	title.append(url_list[i]['title'])
	url.append(URL + url_list[i]['href'])
# print(title)

# 获取每一话图片
def getpic(title_1,url_base,url_next):
	onesoup = BeautifulSoup(requests.get(url_base + url_next).text,'html.parser')
# 获取当页图片地址，并记录
	piclink = 'http://p2.xiaoshidi.net/' + str(onesoup.select('script')[8]).split('mhurl="')[-1].split('";')[0]
	# url_list.append(piclink)	#异步处理时记录列表会出错，不明原因
	# 获取页面序号
	pagenum = str(onesoup.select('head title')).split('(')[-1].split(')')[0]
	if pagenum.find('页') == -1 : pagenum = '第1页'
# 创建文件夹，如果已存在则跳过
	try: os.mkdir('media/' + title_1)
	except Exception: pass
# 设置图片存放路径，下载图片，如果存在则跳过
	picpath = 'media/' + title_1 + '/' + pagenum + '.jpg'
	img = requests.get(piclink)
	if os.path.exists(picpath) : print(pagenum,'已存在')
	else:
		with open(picpath, 'wb') as file:
			file.write(img.content)
			file.close()
# 判断是否为最后一页，如果是则保存列表退出，否则嵌套执行下一页
	nextpic = onesoup.select('head link')[3]['href']
	if nextpic.find('.html') == -1 :
		print('已是最后一页,'+title_1+'完成')
		#记录图片地址清单。异步处理时记录列表会出错，不明原因
		# with open('media/' + title_1 + '/' + 'list.txt','a') as file2:
		# 	file2.write('============'+title_1+'============\n')
		# 	file2.write(str(url_single))
		# 	file2.close()
	else :
		print(pagenum,'完成，前往下一页')
		getpic(title_1,url_base,nextpic)

# 主程序开始
# for i in range(3,len(title)):
# 	url_single = []
getpic(title[39],url[39],'')

# 异步处理主程序
# if __name__ == '__main__':
# 	pool = Pool(processes=2)
# 	for i in range(40,41) :
# 		pool.apply_async(getpic,args=(title[i],url[i],'',))
# 	pool.close()
# 	pool.join()
import requests

headers = {
	# 'Host':'www.mmjpg.com',
	# 'Connection':'keep-alive',
	# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
	# 'Accept':'*/*',
# 'Referer'是关键，告诉服务器我是从哪个页面链接过来，才会得到正确的respond
	'Referer':'http://www.mmjpg.com/mm/',
	# 'Accept-Encoding':'gzip, deflate',
	# 'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}


# 1255之前图片链接形式为：http://fm.shiyunjj.com/2018/1255/[1,2,3].jpg

# 1255之后，图片为XHR加载，得到图片编码
# for i in range(1256,1257):
# 	URL = 'http://www.mmjpg.com/data.php?id='+ str(i) +'&page=8999'
# 	req = requests.get(URL,headers=headers)

# # 地址为：http://fm.shiyunjj.com/2018/1256/[1,2,3]+i+随机编码.jpg
# 	print(req.text.split(','))


URL = 'http://fm.shiyunjj.com/2018/1255/3.jpg'
req = requests.get(URL)
print(req.content)
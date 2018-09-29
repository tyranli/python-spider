import requests
from bs4 import BeautifulSoup
import json
#======================configure==========================
MID = '92ca11dcba564952b82b0a0a8b5f7431'	#订阅号ID
SIZE = '1'
#=========================================================

#获取文章列表
def get_index_page(MID,SIZE):
	url = 'http://napi.uc.cn/3/classes/article/categories/wemedia/lists/'+MID+'?_app_id=cbd10b7b69994dca92e04fe00c05b8c2&_fetch=1&_size='+SIZE+'&_select=xss_item_id%2Ctitle%2Ccontent'
	res = requests.get(url)
	data = json.loads(res.text)
#	soup = BeautifulSoup(res.text,'html.parser')
#	title = soup.select('article-title').text

	print(data)

get_index_page(MID,SIZE)
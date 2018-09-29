import requests
from bs4 import BeautifulSoup

# with open('22.txt','r') as file :
# 	soup = BeautifulSoup(file,'html.parser')
# 	gif_list = soup.select('.f24 img')
# 	# print(soup.prettify())
# 	with open('list.txt','a') as listfile:
# 		for i in range(0,len(gif_list)):
# 			listfile.write(gif_list[i]['src']+'\n')
# 	listfile.close()
# file.close()
with open('list.txt') as file :
	urllist = list(file)
file.close()

# RECORD = ''
# with open('list2.txt','a') as file:
	# for i in range(0,len(urllist)):
		# url = urllist[i].strip('\n')
		# savepath = 'media/' + str(i) + '.gif'
		# try:
		# 	with open(savepath, 'wb') as file :
		# 		file.write(requests.get(url).content)
		# 	file.close()
		# 	print(savepath + '>>>保存成功')
		# 	# RECORD += '>>>pic_' + str(i) + '@' + url + '>>>成功\n'
		# except Exception as e:
		# 	print(savepath + '>>>保存失败',e)
			# RECORD += url+'\n'
	# file.write(RECORD)
# file.close()
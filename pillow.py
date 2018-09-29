import os
from PIL import Image
# 用pillow生成缩小图
root = os.getcwd()
for i in os.listdir(root):
	im = Image.open(i)
	w, h = im.size
	if w*h >= 4000000:
		print(i,'缩放')
		im.thumbnail((w*0.5, h*0.5))	# 缩放到50%:
		im.save(i,'JPEG')

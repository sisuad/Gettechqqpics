a = input("index1with1:") #获取图片第一级目录，1位
b = input("index2with2:") #获取图片第二级目录，2位
c = input("index3with1:") #获取图片第三级目录，3位
initial_pic = input("initial_pic:") #获取初始图片编号，3位
initial_pic -= 1
final_pic = input("final_pic:") #获取末尾图片编号，3位
px_with = input("px_with:") #获取图片宽度
px_len = input("px_len:") #获取图片调试
key_words = raw_input("key_words:") #获取图片关键词
B = str(a) + str(b)
C = str(a) + str(b) + str(c) 
pic_last_num = 0

#输出图片地址编号
while initial_pic < final_pic: 
	initial_pic += 1
	#如果图片目录小于10
	if initial_pic < 10:
		print "![" + str(key_words) + "](http://img1.gtimg.com/" + str(a) + "/" \
			+ str(B) + "/" + str(C) + str(pic_last_num) + "/" + str(C) + "00" + str(initial_pic) \
			+ "_" + str(px_with) + "x" + str(px_len) + "_0.jpg)"
	#如果图片目录大于等于10小于100
	elif 10 <= initial_pic < 100:
		print "![" + str(key_words) + "](http://img1.gtimg.com/" + str(a) + "/" \
			+ str(B) + "/" + str(C) + str(pic_last_num) + "/" + str(C) + "0" + str(initial_pic) \
			+ "_" + str(px_with) + "x" + str(px_len) + "_0.jpg)"
	#如果图片目录大于等于100
	elif initial_pic >= 100:
		pic_last_num = initial_pic // 100
		print "![" + str(key_words) + "](http://img1.gtimg.com/" + str(a) + "/" \
			+ str(B) + "/" + str(C) + str(pic_last_num) + "/" + str(C) + str(initial_pic) \
			+ "_" + str(px_with) + "x" + str(px_len) + "_0.jpg)"


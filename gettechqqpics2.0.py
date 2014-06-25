#_*_ coding=utf-8 _*_
#以下是示例地址
#http://img1.gtimg.com/9/955/95531/9553121_1200x1000_0.jpg
#http://img1.gtimg.com/9/955/95532/9553285_1200x1000_0.jpg
print "示例图片地址"
print "初始图片：http://img1.gtimg.com/9/955/95531/9553121_1200x1000_0.jpg"
print "末尾图片：http://img1.gtimg.com/9/955/95532/9553285_1200x1000_0.jpg"

#获取变量
a = input("输入图片第一级目录（1位，示例【9】）:") #获取图片第一级目录，1位
b = input("输入图片第二级目录（2位，示例【55】）:") #获取图片第二级目录，2位
c = input("输入图片第三级目录（1位，示例【3】）") #获取图片第三级目录，3位
initial_pic = input("输入首位图片编号（后3位，示例【121】）:") #获取初始图片编号，3位
initial_pic -= 1
final_pic = input("输入末尾图片编号（后3位，示例【285】）:") #获取末尾图片编号，3位
px_with = input("输入图片宽度，示例【1200】:") #获取图片宽度
px_len = input("输入图片高度，示例【1000】:") #获取图片调试
key_words = raw_input("输入图片关键词，示例【互联网女皇】:") #获取图片关键词
B = str(a) + str(b)
C = str(a) + str(b) + str(c) 
pic_last_num = 0

#输出图片Markdown地址
f = open ("name.txt", "w" )
while initial_pic < final_pic: 
	initial_pic += 1

	#如果图片目录小于10
	if initial_pic < 10:
		results1 = "![" + str(key_words) + "](http://img1.gtimg.com/" + str(a) + "/" \
			+ str(B) + "/" + str(C) + str(pic_last_num) + "/" + str(C) + "00" + str(initial_pic) \
			+ "_" + str(px_with) + "x" + str(px_len) + "_0.jpg)"
		f.write(results1 + '\n')
		print results1

	#如果图片目录大于等于10小于100
	elif 10 <= initial_pic < 100:
		results2 = "![" + str(key_words) + "](http://img1.gtimg.com/" + str(a) + "/" \
			+ str(B) + "/" + str(C) + str(pic_last_num) + "/" + str(C) + "0" + str(initial_pic) \
			+ "_" + str(px_with) + "x" + str(px_len) + "_0.jpg)"
		f.write(results2 + '\n')
		print results2

	#如果图片目录大于等于100
	elif initial_pic >= 100:
		pic_last_num = initial_pic // 100
		results3 = "![" + str(key_words) + "](http://img1.gtimg.com/" + str(a) + "/" \
			+ str(B) + "/" + str(C) + str(pic_last_num) + "/" + str(C) + str(initial_pic) \
			+ "_" + str(px_with) + "x" + str(px_len) + "_0.jpg)"
		f.write(results3 + "\n")
		print results3

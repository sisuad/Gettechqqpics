#_*_ coding=utf-8 _*_
#以下是示例地址
#http://img1.gtimg.com/9/955/95531/9553121_1200x1000_0.jpg
#http://img1.gtimg.com/9/955/95532/9553285_1200x1000_0.jpg
print "示例图片地址"
print "初始图片：http://img1.gtimg.com/9/955/95531/9553121_1200x1000_0.jpg"
print "末尾图片：http://img1.gtimg.com/9/955/95532/9553285_1200x1000_0.jpg"
initial_pic = 0
final_pic = 0
px_with = 0
px_len = 0
pic_blong = 0
a = 0
b = 0
pic_last_num = 0

#定义开始函数
def new_loop():
    global initial_pic, final_pic, px_with, px_len, a, b, A, B
    initial_pic = input("输入图库初始数值，示例【9553121】:") #获取图库初始数值
    final_pic = input("输入图库末尾数值，示例【9553285】:") #获取图库末尾数值
    px_with = input("输入图片宽度，示例【1200】:") #获取图片宽度
    px_len = input("输入图片高度，示例【1000】:") #获取图片高度
    pic_blong = input("输入图片.jpg前的数值，示例【0】，因为有些图库为【960】")#获取图片.jpg前的数值
    a = initial_pic // 10 ** 6 #图库初级目录
    b = initial_pic // 10 ** 4 #图库二级目录
    A = str(initial_pic)[-3] #初始图片序号倒数第三个数
    B = str(final_pic)[-3] #末尾图片序号倒数第三个数
    initial_pic -= 1
    return get_img()

#定义生成图片地址函数
def get_img():
    global initial_pic, final_pic, px_len, px_with, a, b, A, B
    #开始规则循环生成图片
    while initial_pic < final_pic:
        initial_pic += 1

        #如果图库倒数第三个数值相等，即百位没有变化
        if A == B:
            c = initial_pic // 10 ** 2 #确定图库第三级目录
            library = str(a) + "/" + str(b) + "/" + str(c) #图库目录绝对路径

        #如果图库倒数第三个数值不相等，即百位有进位
        else:
            #根据循环确定倒数第三个数的具体值
            pic_last_num = initial_pic % 10 ** 3 // 100
            c = str(initial_pic //10 ** 3 % 10) + str(pic_last_num) #确定图库第三级目录
            library = str(a) + "/" + str(b) + "/" + str(b) + str(c) #图库目录绝对路径

    #输出图片Markdown地址
        print "![](http://img1.gtimg.com" + "/" + str(library) + "/" + str(initial_pic) + \
            "_" + str(px_with) + "x" + str(px_len) + "_" + str(pic_blong) + ".jpg)"
    
    #重新开始获取图库地址
    return new_loop()

new_loop()

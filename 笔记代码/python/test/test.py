#!/usr/bin/env python
#coding:utf -8
# l = [1,2,3,4,5,6,7,2,3,4]
# t = {"a":4, "b":2,"c":5,"e":3,"d":2}
# n = sorted(t.items(),key=lambda x:x[1],reverse=True)#1代表value的值由小到大,reverse代表倒转
# m = sorted(t.items(),key=lambda x:x[0])#0代表key的“a”到“e”
# print l[2:]
# print l[2:5]
# print l[2:5:2]
# print l[2:5:3]
# print n
# print n[0:3]#将字典内的出现频率最高三个列出
# print m
# print 'hello'
# print 'hello\n\n'
# print r'hello\n\n'
# n = 'abc'
# print n.join("1")
# print n.join("11")
# print n.join('111')

# def changename(a,b):
# 	print a 
# 	return a
# changename(1,2)

# l = ['a','a','a','b','b','c']
# print l
# t = {"a":4, "b":2,"c":5,"e":3,"d":2}
# print t.get("g")
# t = {}
# for i in l:
# 	print

# def a(b,**c):
# 	print b
# 	print c
# 	print '-'*20
# 	return 1,2,3,4
# t=a(1,x=2,y=3,z=4)
# print t
# from time import ctime,sleep
# from time import
# def timefun_arg(pre="hello"):
# 	def timefun(func):#定义装饰器
# 		def warppedfunc():#定义一个内部函数  
# 			print "%s called at %s" %(func.__name__,ctime())#先执行函数的内容 
# 			return func()#再执行另一个函数的内容（这里传入的是foo函数）
# 		return warppedfunc#这个让foo(1,2)执行不报错,它的意义可能是执行上一行的代码
# 	return timefun
# @timefun_arg("wind")#在foo执行之前，先利用foo调用装饰器函数，进入到这个函数然后再timefun（foo）
# def foo():
# 	print "-"*30
# 	return "haha"

# @timefun_arg("kid")
# def too():
# 	print "-"*30
# 	return "wawa"	
# foo()
# sleep(2)
# print foo()

# too()
# sleep(2)
# print too()

# from time import time,sleep
# def logged(when):
# 	def log(f,*args,**kargs):
# 		print "fun:%s args:%r kargs:%r" %(f,args,kargs)
# 		#%r字符串的同时，显示原有对象类型
# 	def pre_logged(f):#先声明，否则最下面的try语句中的pre_logged会不存在
# 		def warpper(*args,**kargs):
# 			log(f,*args,**kargs)     #先执行log(fun,"wind",x=1,y=2)
# 			return f(*args,**kargs)  #后执行fun函数内容
# 		return warpper
# 	def post_logged(f):#同理
# 		def warpper(*args,**kargs):
# 			now=time()
# 			try:
# 				return f(*args,**kargs) #先执行too函数内容
# 			finally:#finally表示执行玩try语句后，一定最后再执行其内容
# 				log(f,*args,**kargs)    #后执行log(too,"kid")
# 				sleep(2)
# 				print "time delta: %s"%(time()-now)
# 		return warpper
# 	try:#先执行函数的内容（第一步）
# 		#若when等于pre返回pre_logged,即执行上面的pre_logged函数	
# 		return {"pre":pre_logged,"post":post_logged}[when]
# 	except KeyError ,e:
# 		raise ValueError(e),'must be "pre" or "post"'
# @logged("pre")
# def fun(name,x,y):
# 	print "hello,",name
# fun("wind",x=1,y=2)
# print "-"*30
# @logged("post")
# def too(name):
# 	print "hi,",name
# too("kid")
# import json
# class Employee:
# 	a="123"
# 	def __init__(self,name,pay):
# 		self.name=name
# 		self.pay=pay
# 	def hello(self):
# 		print self.name
# 		print "hello"

# worker=Employee("wind",100)
# worker.hello()
# print getattr(worker,'a')
# print hasattr(worker,'a')
# setattr(worker,'name',"kid")
# worker.hello()
# print "-"*30
# print Employee.__name__
# print "-"*30
# print Employee.__dict__
# print "-"*30
# print Employee.__doc__
# print "-"*30
# print Employee.__module__
# print "-"*30
# print Employee.__bases__

# class Parent:
# 	a = 100
# 	def __init__(self):
# 		print "调用父类构造函数"
# 	def parentMethod(self):
# 		print "调用父类方法"
# 	def setAttr(self,attr):
# 		Parent.a = attr
# 	def getAttr(self):
# 		print "父类属性 :",Parent.a
# 	def sayhello(self):
# 		print "i am Parent"
# class child(Parent):
# 	def __init__(self):#子类不会主动调用父类构造方法
# 		print "调用子类构造方法"
# 	def childMethod(self):
# 		print "调用子类方法"
# 	def sayhello(self):#与父类的函数重名，会覆盖父类的内容
# 		print "i am child"

# c = child()
# c.childMethod()
# c.parentMethod()
# c.sayhello()
# c.getAttr()
# print "-"*30
# c.setAttr(200)
# c.getAttr()
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
# def run_twice(animal):
#     animal.run()
#     animal.run()
# run_twice(Dog())

# class Parent:
# 	__a = 100
# 	b = 20
# 	def print_a(self):
# 		print self.__a
# 	@parentmethod
# 	def changeB(cls,newB):
# 		cls.b = newB
# p = Parent()
# p.print_a()
# print p._Parent__a

# sum =100 

# def fun():
# 	s1=200
# 	res=locals() #返回这个函数中的获取到的局部变量
# 	print res 
# 	res1 = globals()#返回全局的变量
# 	print res1 
# fun()

# f = open("hello.txt","r+")
# #r 只读  
# #w 只写，文件存在，则覆盖内容，文件不存，则新建（最好不要用w）
# #a 追加写
# #r+ 读写方式打开文件
# #w+ 可读可写文件，文件存在，则覆盖内容，文件不存，则新建
# #a+ 追加打开文件，可读可写，如果文件不存在，则创建
 
# print f.mode 
# print f.name
# print f.closed#判断文件是否关闭了
# print '-'*30
# f.close()
# print f.closed

# myPath    = "./"
# fontPath  = "./"
# inputFile = "test.JPG"
# outputFil = "output.jpg"

# from PIL import Image,ImageFont,ImageDraw
# im = Image.open(myPath + inputFile)#打开图片
# draw = ImageDraw.Draw(im)#画出图片
# fontsize = min(im.size)/4
# print im
# print im.size
# print im.size[0]
# print fontsize
# font = ImageFont.truetype(fontPath + "GasinamuNew.ttf", fontsize)#.ttf是字体库的东西，需要另外找的
# draw.text((im.size[0]-fontsize,0), '8',font = font ,fill = (256,256,0))#8代表显示的数字，fill颜色，第一个参数是位置
# im.save(myPath + outputFil,"jpeg")

# import string, random

# filed = string.letters + string.digits#字母加数字

# def getRandom():#获得四组字母和数字的随机组合
# 	return "".join(random.sample(filed,3))

# def concatenate(group):#生成的每个激活码中有几组
# 	return "-".join([getRandom() for i in range(group)])

# def generate(n):#生成n组激活码
# 	return [concatenate(4) for i in range(n)]

# if __name__ == '__main__':#单独执行才会运行print，否则不会运行
# 	print generate(5)

# import re,os
# from collections import Counter
# # FileSource = "./music.txt"
# File_Path = "./again"

# def getCounter(articlefilesource):
# 	pattern = r'''[A-Za-z]+|\$?\d+%?$'''#字母格式，
# 	with open(articlefilesource) as f:
# 		r = re.findall(pattern,f.read())
# 		return Counter(r)
# #过滤词
# stop_word = ['the','in','of','and','to','has','that','s','is','are','a','with','as','an']

# def run(File_Path):
# 	os.chdir(File_Path)#切换到目标文件所在目录
# 	total_counter = Counter()#遍历该目录下的txt文件
# 	for i in os.listdir(os.getcwd()):
# 		print os.path.splitext(i)
# 		if os.path.splitext(i)[1] == '.txt':
# 			total_counter += getCounter(i)
# 	#排除stopword的影响
# 	for i in stop_word:
# 		total_counter[i]=0
# 	print total_counter.most_common()
# 	print total_counter.most_common()[0:3]
# if __name__ == '__main__':
# 	run(File_Path)

# import os
# from PIL import Image

# myPath = "./"

# outPath= "./photo/"

# def processImage(filesource,destsource,name,imgtype):
# 	imgtype = 'jpeg' if imgtype == ".jpg" else 'png'
# 	im = Image.open(filesource + name)
# 	rate = max(im.size[0]/640 if im.size[0] > 640 else 0,im.size[1]/1130 if im.size[1] > 1130 else 0)
# 	print rate#缩放比例
# 	if rate:
# 		im.thumbnail((im.size[0]/rate,im.size[1]/rate))
# 	im.save(destsource + name,imgtype)

# def run():
# 	os.chdir(myPath)
# 	for i in os.listdir(os.getcwd()):
# 		postfix = os.path.splitext(i)[1]#检查后缀
# 		if postfix == '.jpg' or postfix == '.png':
# 			processImage(myPath,outPath,i,postfix)
# if __name__ == '__main__':
# 	run()
# import os,re

# File_Path = "./"

# def analyze_code(codefilesource):
# 	total_line = 0
# 	comment_line = 0
# 	blank_line = 0
# 	with open(codefilesource) as f: #相当于f = open(codefilesource)
# 		lines = f.readlines()
# 		total_line = len(lines)
# 		line_index = 0
# 		while line_index < total_line:#遍历每一行
# 			line = lines[line_index]
# 			if line.startswith("#"):#注释行数
# 				comment_line += 1
# 			elif re.match("\s*'''",line) is not None:
# 				comment_line += 1
# 				while re.match(".*'$'''",line) is None:
# 					line = lines[line_index]
# 					comment_line += 1
# 					line_index += 1

# 			elif line == "\n":#空行
# 				blank_line +=1
# 			line_index +=1
# 	print "在%s中:"%codefilesource
# 	print "代码行数:",total_line
# 	print "注释行数:",comment_line,"占%0.2f%%"%(comment_line*100.0/total_line)
# 	print "空行数:",blank_line,"占%0.2f%%"%(blank_line*100.0/total_line)
# 	return [total_line,comment_line,blank_line]

# def run(File_Path):
# 	os.chdir(File_Path)
# 	total_lines = 0
# 	total_comment_lines = 0
# 	total_blank_lines = 0
# 	for i in os.listdir(os.getcwd()):
# 		if os.path.splitext(i)[1] == '.py':
# 			line = analyze_code(i)
# 			total_lines,total_comment_lines,total_blank_lines = total_lines + line[0],total_comment_lines+line[1],total_blank_lines+line[2]
# 	print "总代码行数:",total_lines
# 	print "总注释数:",total_comment_lines,"占%0.2f%%"%(total_comment_lines*100.0/total_lines)
# 	print "总空行数:",total_blank_lines,"占%0.2f%%"%(total_blank_lines*100.0/total_lines)

# if __name__ == '__main__':
# 	run(File_Path)

from goose import Goose
from goose.text import StopWordsChinese
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

url ='https://linux.cn/article-6717-1.html'

def extract(url):
	g= Goose({'stopwords_class':StopWordsChinese})
	article = g.extract(url=url)
	return article.cleaned_text
if __name__ == '__main__':
	print extract(url)

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import string,random

fontPath = "./"

def getRandomChar():#获得随机四个字母+数字
	return [random.choice(string.letters + string.digits) for _ in range(4)]

def getRandomColor():#获得颜色
	return (random.randint(30,100),random.randint(30,100),random.randint(30,100))

def getCodePicture():#获取验证码图片
	width = 240
	height= 60
	#创建画布
	image = Image.new('RGB',(width,height),(180,180,180))
	font = ImageFont.truetype(fontPath + "GasinamuNew.ttf",40)
	draw = ImageDraw.Draw(image)
	#创建验证码对象
	code = getRandomChar()
	for t in range(4):
		draw.text((60*t +10,0),code[t],font=font,fill=getRandomColor())
	#填充噪点
	for _ in range(random.randint(1500,3000)):
		draw.point((random.randint(0,width),random.randint(0,height)),fill=getRandomColor())
	#模糊处理
	image = image.filter(ImageFilter.BLUR)
	#保存文件
	image.save("./photo/"+"".join(code)+'.jpg','jpeg')

if __name__ == '__main__':
	getCodePicture()

import requests
import re
url = r'http://www.renren.com/ajaxLogin/login'
user = {'email':'username','password':'passwd'}#注册一个账号，才会有数据显示
s = requests.Session()
r = s.post(url,data=user)
html = r.text
visit = []
first = re.compile(r'</span><span class="time-tip first-tip"><span class="tip-content">(.*?)</span>')
second = re.compile(r'</span><span class="time-tip"><span class="tip-content">(.*?)</span>')
third = re.compile(r'</span><span class="time-tip last-second-tip"><span class="tip-content">(.*?)</span>')
last = re.compile(r'</span><span class="time-tip last-tip"><span class="tip-content">(.*?)</span>')
visit.extend(first.findall(html))
visit.extend(second.findall(html))
visit.extend(third.findall(html))
visit.extend(last.findall(html))
for i in visit:
	print i

print "以下是更多的最近采访"
vm = s.get('http://www.renren.com/myfoot/whoSeenMe')
fm = re.compile(r'"name":"(.*?)"')
visitmore = fm.findall(vm.text)
for i in visitmore:
	print i







# files = {'file':open('1.jpg','rb')}#rb二进制
# r = requests.post("http://httpbin.org/post",files = files)
# print r.url
# print r.text
# import json
# mydata = {'name':'wind','age':'24'}
# r = requests.post("http://httpbin.org/post",data = json.dumps(mydata))
# print r.url
# print r.text
# {
# 	"args":{},
# 	"data":"{\"name\":\"wind\",\"age\":\"24\"}",
# 	"files":{},#上传文件
# 	"from":{},
# 	"headers":{
# 		"Accept":"*/*",
# 		"Accept-Encoding":"gzip,deflate,compress",
# 		"Content-Length":"30",
# 		"Content-Type":"application/x-www-form-urlencoded",
# 		"Host":"httpbin.org",
# 		"User-Agent":"python-requests/2.2.1 CPython/2.7.6 Linux/3.16.0-30-generic" #使用的命令
# 	},
# 	"json":{
# 		"name":"wind",
# 		"age":"24"
# 		},
# 	"origin":"61.148.201.2",
# 	"url":"http://httpbin.org/post"
# }
# myparams= {"name":"wind"}
# r = requests.get('https://www.baidu.com',params=myparams)#前面那个应该是网址头
# print r.url
# print r.content
# r = requests.get('http://httpbin.org/get')
# r = requests.get('http://c.itcast.cn')
# print r.text#发出去的内容
# print r.content #收到的内容
# print r.url


# {
# 	"args":{},
# 	"headers":{
# 		"Accept":"*/*",
# 		"Accept-Encoding":"gzip,deflate,compress",
# 		"Host":"httpbin.org",
# 		"User-Agent":"python-requests/2.2.1 CPython/2.7.6 Linux/3.16.0-30-generic" #使用的命令
# 	},
# 	"origin":"61.148.201.2",
# 	"url":"http://httpbin.org/get"
# }
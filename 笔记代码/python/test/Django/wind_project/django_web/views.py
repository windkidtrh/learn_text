#coding:utf-8
from django.shortcuts import render
from django_web.models import Test1
# Create your views here.
from django.core.paginator import Paginator
def index(request):
	limit = 2
	test1 =  Test1.objects.all()
	paginator = Paginator(test1,limit)#分页
	page = request.GET.get('page',1)#获取第一页
	loaded = paginator.page(page)#当前那一页
	# print (request)
	# print (request.GET)
	context ={
		'Test1':loaded,
	}
	return render(request,'index.html',context)
# def index(request):
# 	test1 =  Test(name = 'w',age = 24,sex = 1)
# 	iter = "123456"
# 	paginator = Paginator(iter,2)
# 	page1 = paginator.page(1)
# 	# test2 = Test.objects.all()[:1]
# 	# print test2
# 	try:
# 		test1.save()
# 	except:
# 		pass

# 	context ={
# 		'Test':loaded,
# 	}
# 	return render(request,'index.html',context)
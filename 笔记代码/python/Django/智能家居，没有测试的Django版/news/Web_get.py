# -*- coding: utf-8 -*-

from django.http import HttpResponse#网页响应
from django.shortcuts import render_to_response#网页跳转
import json
import socket
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
Current_time = time.strftime(TIMEFORMAT,time.localtime())
import sys   
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')
host = ""
port = ""
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 表单
def search_form(request):
    return render_to_response('search_form.html')

# 接收请求数据
def search(request):  
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

	
# from django.http import HttpResponse
 
# def hello(request):
#     return HttpResponse("Hello world wind! ")

# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
import MySQLdb
from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['wind'] = 'Hello World! wind'
    return render(request, 'hello.html', context)
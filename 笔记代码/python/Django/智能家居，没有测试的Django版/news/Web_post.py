# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf
import sys   
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')  
# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)

def Product_isExist_inNum4(First_type,Second_type,Product_num,User_id):
    try:
        return ProductBelongTo.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num,user_id=User_id)

    except:
        print "Product_isExist_inNum4 Error"
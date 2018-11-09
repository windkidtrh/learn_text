# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from TestModel.models import SaveTmpValue,Log,ProductBelongTo,ProductCurrentState
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
# import SocketServer
# import socket
# HOST = "10.10.20.43"
# PORT = 12001
# from SocketServer import handle
# class MyUDPHandler(SocketServer.BaseRequestHandler):
#     print "cccc"
#     def handle(self):
#         data = self.request[0].strip()
#         socket = self.request[1]
#         print data,socket
# from django.db import connection
# def Product_isExist_inNum4(First_type,Second_type,Product_num,User_id):
#     try:
#         x = ProductBelongTo.objects.all()
#         # return x
#         # x=ProductBelongTo.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num,user_id=User_id)
#         return x
#         # conn=mysql.connect_mysql()
#         # cur = conn.cursor()
#         # sql1="select * from product_belong_to where (first_type,second_type,product_num,user_id) in (('%s','%s','%s','%s'))"%(First_type,Second_type,Product_num,User_id)
#         # cur.execute(sql1)
#         # result = cur.fetchone()
#         # conn.commit()
#         # cur.close()
#         # return result

#     except:
#         print "Product_isExist_inNum4 Error"
def Product_isExist_inNum2():
    # print First_type,Second_type,Product_num
    try:
        x = ProductCurrentState.objects.all()
        # return x
        # x=ProductBelongTo.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num,user_id=User_id)
        return x
        # haha=''
        # return ProductCurrentState.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num)
        # tt=ProductCurrentState.objects.all()
        # haha=tt.first_type
        # return haha

    except:
        print "Product_isExist_inNum2 Error"
def Mac_is_not_in():
    try:
        result = ProductCurrentState.objects.all()
        if len(result) == 0:
            pass
        else:
            for i in result:
                ProductCurrentState.objects.filter(belong_id = i.belong_id).update(online_value= i.online_value-1)
            ProductCurrentState.objects.filter(online_value=0).delete()

    except:
        print "Mac_is_not_in Error"
def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    # Current_time = time.strftime(TIMEFORMAT,time.localtime())
    # Log(user_id=1,the_time=Current_time,info="a").save()
    # test1.name = 'haha'
    # user_id = request.GET["user_id"]
    # first_type = request.GET["first_type"]
    # second_type = request.GET["second_type"]
    # product_num = request.GET["product_num"]
    # callback=request.REQUEST.get("callback","")
    Num4_message = Mac_is_not_in()
    # haha=request.GET["haha"]
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    # print "haga"

    # print Num4_message.first_type,Num4_message.user_id
    # print "haha"
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse(Num4_message)

# if __name__ == "__main__":
#     server = SocketServer.UDPServer((HOST, int(PORT)), MyUDPHandler)
#     server.serve_forever()

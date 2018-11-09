# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test,Register
# import Mysql.mysql
# import web
# import MySQLdb
# 数据库操作
# def testdb(request):
#     # 初始化
#     response = ""
#     response1 = ""
    
    
#     # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
#     list = Test.objects.all()
        
#     # filter相当于SQL中的WHERE，可设置条件过滤结果
#     # response2 = Test.objects.filter(id=1) 
    
#     # 获取单个对象
#     # response3 = Test.objects.get(id=1) 
    
#     # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
#     # Test.objects.order_by('name')[0:2]
    
#     #数据排序
#     # Test.objects.order_by("id")
    
#     # 上面的方法可以连锁使用
#     # Test.objects.filter(name="wind").order_by("id")
    
#     # 输出所有数据
#     for var in list:
#         response1 += var.name + " "
#     response = response1
#     return HttpResponse("<p>" + response + "</p>")
# def test:
#     return "hah1"
#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql="update testmodel_test set name='wind' where id='1' "
#         cur.execute(sql)
#         conn.commit()
#         cur.close()

#         return "success"

#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Register(name='wind',passwd='123456')
    # test1.name = 'haha'
    test1.save()
    
    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')
    
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    
    return HttpResponse("<p>"+"input成功"+"</p>")

# def testdb:
#     # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
#     test1 = Register(name='wind',passwd='123456')
#     # test1.name = 'haha'
#     test1.save()
    
#     # 另外一种方式
#     #Test.objects.filter(id=1).update(name='Google')
    
#     # 修改所有的列
#     # Test.objects.all().update(name='Google')
    
#     return "<p>"+"input成功"+"</p>"
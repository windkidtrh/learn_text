#-*-coding:utf-8-*- 
import mongo
# from pymongo import MongoClient
# conn = MongoClient('192.168.1.101', 27017)
# db = conn.wind  
# my_test = db.wind
# def Register(Password,Username):
#     # return "hah1"
#     try:
#         # print "haha1"
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql1="insert into register(password,username) values ('%s','%s')"%(Password,Username)
#         cur.execute(sql1)
#         conn.commit()
#         cur.close()

#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])


def Register(Username):
    # return "hah1"
    try:
        result=""
        print "1"
        conn_mongo=mongo.connect_mysql()
        # conn.my_test
        # print my_test
        x = conn_mongo.find()
        for i in x:
            result=result+str(i)
        # print "haha1"
        # conn=mysql.connect_mysql()
        # cur = conn.cursor()
        # sql1="select * from register where username='%s'"%(Username)
        # cur.execute(sql1)
        # result = cur.fetchall()
        # conn.commit()
        # cur.close()
        print result 
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
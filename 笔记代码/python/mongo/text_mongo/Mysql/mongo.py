#-*-coding:utf-8-*-
# import MySQLdb
# import socket
#import time
#TIMEFORMAT= "%Y-%m-%d %H:%M:%S"
#import traceback


# HOSTNAME = socket.gethostname()
# PASSWD = ''
# if HOSTNAME=='iZ94zoeilgyZ':
#     PASSWD = '4c1fadc64b' #4c1fadc64b
# elif HOSTNAME== 'iZ28quomnknZ':
#     PASSWD = 'aa123123'

# sql_socket ="/run/mysqld/mysqld.sock"   #"/tmp/mysql.sock"

# def connect_mysql():
    
#     try:
#         conn=MySQLdb.connect(
#              host='localhost',
#              port=3306,
#              user='root',
#              passwd=PASSWD,
#              #db='study',
#              charset="utf8",
#              unix_socket = sql_socket
#              )
#         conn.select_db("test")
#         return conn
    
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
from pymongo import MongoClient
def connect_mysql():
    conn = MongoClient('192.168.1.101', 27017)
    db = conn.wind  
    my_test = db.wind
    return my_test

if __name__ == '__main__':
    con = connect_mysql()
    print con

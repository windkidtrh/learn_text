#-*-coding:utf-8-*- 
import mysql
import MySQLdb

def Register(Password,Username):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into register(password,username) values ('%s','%s')"%(Password,Username)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Username_isExist(username):

    if get_by_username(username) == None:
        return False
    else:
        return True

def get_by_username(username):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from register where username='%s'"%username
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Check_number(Check_number):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select * from number where check_number='%s'"%Check_number
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Delete_number(Check_number):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="delete from number where check_number='%s'"%Check_number
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Input_number(Check_number):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into number(check_number) values ('%s')"%Check_number
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])        
if __name__== "__main__":
    print get_by_username('wind')
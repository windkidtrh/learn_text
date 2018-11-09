#-*-coding:utf-8-*- 
import mysql
import MySQLdb

def Register(Password,Username,Nickname,Head_photo):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into user(password,username,nickname,head_photo) values ('%s','%s','%s','%s')"%(Password,Username,Nickname,Head_photo)
        cur.execute(sql1)
        conn.commit()
        cur.close()

        cur=conn.cursor()
        sql2= "select user_id from user where username='%s'"%Username
        cur.execute(sql2)
        result=cur.fetchone()
        conn.commit()
        cur.close()

        cur=conn.cursor()
        sql3="insert into balance(user_id) values ('%s')"%result
        cur.execute(sql3)
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
        sql = "select * from user where username='%s'"%username
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__== "__main__":
    print get_by_username('wind')
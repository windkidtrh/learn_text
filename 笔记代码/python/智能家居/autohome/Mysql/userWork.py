#-*-coding:utf-8-*- 
import mysql
import MySQLdb

def Update_user(Mac_number,Mac_isWork,Id_name):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="update mac_message set mac_isWork='%s',controler='%s' where mac_number='%s'"%(Mac_isWork,Id_name,Mac_number)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Relation(Mac_number,Id_name):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into relation(mac_number,id_name) values ('%s','%s')"%(Mac_number,Id_name)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Check_relation(Mac_number,Id_name):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select * from relation  where (mac_number,id_name) in (('%s','%s'))"%(Mac_number,Id_name)
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Return_mac(Id_name):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select mac_number from relation  where id_name='%s'"%Id_name
        cur.execute(sql1)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Return_mac_current_status(Mac_number):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select current_status from mac_status where mac_number='%s'"%Mac_number
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
#-*-coding:utf-8-*- 
import mysql
import MySQLdb

def Mac_number_isExist(Mac_number):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select * from mac_status where mac_number='%s'"%Mac_number
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Register_mac(Mac_number,Current_status,Mac_ip,Mac_port):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into mac_status(mac_number,current_status,action_name,mac_ip,mac_port) values ('%s','%s','%s','%s','%s')"%(Mac_number,Current_status,Current_status,Mac_ip,Mac_port)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_mac(Mac_number,Current_status):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="update mac_status set current_status='%s' where mac_number='%s'"%(Current_status,Mac_number)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_user_answer(Mac_number,Action_name):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="update mac_status set action_name='%s' where mac_number='%s'"%(Action_name,Mac_number)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
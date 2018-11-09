#-*-coding:utf-8-*- 
import mysql
import MySQLdb

def Register(Password,Username,Id_name):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into register(password,username,id_name) values ('%s','%s','%s')"%(Password,Username,Id_name)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_by_id_name(id_name):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from register where id_name='%s'"%id_name
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
        sql1="select * from mac_message where check_number='%s'"%Check_number
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Delete_number(Check_number):
#    # return "hah1"
#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql1="delete from mac_message where check_number='%s'"%Check_number
#         cur.execute(sql1)
#         conn.commit()
#         cur.close()

#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Input_number(Check_number):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into mac_message(check_number) values ('%s')"%Check_number
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])        

def Input_action(Action_name,Action_show):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into action(action_name,action_show) values ('%s','%s')"%(Action_name,Action_show)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_action(Action_id,Action_name,Action_show):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        if Action_name != '':
            cur = conn.cursor()
            sql1="update action set action_name='%s' where action_id='%s'"%(Action_name,Action_id)
            cur.execute(sql1)
            conn.commit()
            cur.close()

        if Action_show != '':
            cur = conn.cursor()
            sql2="update action set action_show='%s' where action_id='%s'"%(Action_show,Action_id)
            cur.execute(sql2)
            conn.commit()
            cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1]) 

def Show_action():
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select * from action"
        cur.execute(sql1)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])  

def Show_current_action(Action_id):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select * from action where action_id='%s'"%(Action_id)
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Delete_action(Action_id):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="delete from action where action_id='%s'"%(Action_id)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
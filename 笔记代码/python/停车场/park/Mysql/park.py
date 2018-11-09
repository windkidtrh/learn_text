#-*-coding:utf-8-*- 
import mysql
import MySQLdb
TIMEFORMAT= "%Y.%m.%d.%H.%M.%S"
import time

def Register_park(Park_name,Addr,Gps_x,Gps_y,Price,Wifi_name,Wifi_password):
   # return "hah1"
    conn=mysql.connect_mysql()
    try:
        cur = conn.cursor()
        sql1="insert into park_message(park_name,addr,gps_x,gps_y,price,wifi_name,wifi_password) values ('%s','%s','%s','%s','%s','%s','%s')"%(Park_name,Addr,Gps_x,Gps_y,Price,Wifi_name,Wifi_password)
        cur.execute(sql1)
        conn.commit()
        cur.close()

        cur=conn.cursor()
        sql2= "select park_id from park_message where park_name='%s'"%Park_name
        cur.execute(sql2)
        result=cur.fetchone()
        conn.commit()
        cur.close()
        
        cur=conn.cursor()
        sql3="insert into park_stall(park_id) values ('%s')"%(result)
        cur.execute(sql3)
        conn.commit()
        cur.close()

        cur=conn.cursor()
        sql4="insert into indoor_map(park_id) values ('%s')"%(result)
        cur.execute(sql4)
        conn.commit()
        cur.close()          

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Show_park():
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from park_message"
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Park_name_isExist(park_name):

    if get_by_park_name(park_name) == None:
        return False
    else:
        return True

def get_by_park_name(park_name):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from park_message where park_name='%s'"%park_name
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_by_park_id(Park_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from park_message where park_id='%s'"%Park_id
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_park_stall(Park_id,Park_surplus,Park_all,Park_show):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "update park_stall set park_surplus='%s',park_all='%s' where park_id='%s' "%(Park_surplus,Park_all,Park_id)
        cur.execute(sql)
        conn.commit()
        cur.close()

        if Park_show!='':
            cur = conn.cursor()
            sql3=" update park_stall set park_show='%s' where park_id='%s' "%(Park_show,Park_id)
            cur.execute(sql3)
            conn.commit()
            cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Show_park_stall(Park_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from park_stall where park_id='%s'"%Park_id
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_indoor_map(Park_id,Length,Width):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "update indoor_map set length='%s',width='%s' where park_id='%s' "%(Length,Width,Park_id)
        cur.execute(sql)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Show_indoor_map(Park_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from indoor_map where park_id='%s'"%Park_id
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Input_wall(Park_id,Start,End):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "insert into indoor_map_wall(park_id,start,end) values ('%s','%s','%s')"%(Park_id,Start,End)
        cur.execute(sql)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Show_indoor_map_wall(Park_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from indoor_map_wall where park_id='%s'"%Park_id
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Input_position(Park_id,Start,End):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "insert into indoor_map_position(park_id,start,end) values ('%s','%s','%s')"%(Park_id,Start,End)
        cur.execute(sql)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Show_indoor_map_position(Park_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from indoor_map_position where park_id='%s'"%Park_id
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_news_for_comer(Park_id,User_id):
    try:
        Gettime1=time.strftime(TIMEFORMAT,time.localtime())
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql =  "update park_message set door_come='%s'where park_id='%s' "%(1,Park_id)
        cur.execute(sql)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql2 =  "insert into user_come(park_id,comer,come_time) values ('%s','%s','%s')"%(Park_id,User_id,Gettime1)
        cur.execute(sql2)
        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_news_for_outer(Park_id,User_id):
    try:
        Gettime=time.strftime(TIMEFORMAT,time.localtime())
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql =  "update park_message set door_out='%s'where park_id='%s' "%(1,Park_id)
        cur.execute(sql)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql2 =  "insert into user_out(park_id,outer_user,out_time) values ('%s','%s','%s')"%(Park_id,User_id,Gettime)
        cur.execute(sql2)
        conn.commit()
        cur.close()
        conn.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
if __name__== "__main__":
    print get_by_username('wind')
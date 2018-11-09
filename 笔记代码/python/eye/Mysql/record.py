#-*-coding:utf-8-*- 
import mysql
import MySQLdb
TIMEFORMAT= "%Y"
TIMEFORMAT1= "%m.%d"
import time

def Record_eye(Record_id,Left_eye,Right_eye):
    try:
        Gettime1=time.strftime(TIMEFORMAT,time.localtime())#获取年
        Gettime2=time.strftime(TIMEFORMAT1,time.localtime())#获取月日
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into record(record_id,left_eye,right_eye,time_year,time_month) values ('%s','%s','%s','%s','%s')"%(Record_id,Left_eye,Right_eye,Gettime1,Gettime2)
        cur.execute(sql1)
        conn.commit()
        cur.close()
        # return "success"

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_by_record_id(Record_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from register where id='%s'"%Record_id
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Get_record_eye(Record_id):
    try:
        result1=[]
        result2=[]
        result3=[]
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select distinct time_month from record where record_id='%s'"%Record_id#月日唯一查询
        ii=cur.execute(sql1)
        result=cur.fetchmany(ii)
        conn.commit()
        cur.close()
        for haha1 in result:
            result3.append(haha1[0])
        for i,message in enumerate(result3):#for月日循环
            if i != len(result):
                haha = Get_record_left_eye(Record_id,message)#调用左眼求平均
                result1.append('%.1f'%haha)
                gaga = Get_record_right_eye(Record_id,message)#调用右眼求平均
                result2.append('%.1f'%gaga)
        return result3,result1,result2

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Get_record_left_eye(Record_id,Time_month):#左眼求平均
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select AVG(left_eye) from record where (record_id,time_month) in (('%s','%s'))"%(Record_id,Time_month)
        cur.execute(sql1)
        result= cur.fetchone()
        conn.commit()
        cur.close()
        return result[0]#提取数据不带中括号

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Get_record_right_eye(Record_id,Time_month):#右眼求平均
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select AVG(right_eye) from record where (record_id,time_month) in (('%s','%s'))"%(Record_id,Time_month)
        cur.execute(sql1)
        result= cur.fetchone()
        conn.commit()
        cur.close()
        return result[0]#提取数据不带中括号

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_by_health_day(Time_year,Time_month):
    # return Time_year,Time_month
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from health where (time_month,time_year) in (('%s','%s'))"%(Time_month,Time_year)
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Record_health(Record_id,Health_status):
    try:
        Gettime1=time.strftime(TIMEFORMAT,time.localtime())#获取年
        Gettime2=time.strftime(TIMEFORMAT1,time.localtime())#获取月日
        conn=mysql.connect_mysql()
        if get_by_health_day(Time_year=Gettime1,Time_month=Gettime2) == None:
            cur = conn.cursor()
            sql1="insert into health(record_id,health_status,time_year,time_month) values ('%s','%s','%s','%s')"%(Record_id,Health_status,Gettime1,Gettime2)
            cur.execute(sql1)
            conn.commit()
            cur.close() 

        else:
            cur = conn.cursor()
            sql2= "update health set health_status='%s' where (record_id,time_year,time_month) in (('%s','%s','%s'))"%(Health_status,Record_id,Gettime1,Gettime2)
            cur.execute(sql2)
            conn.commit()
            cur.close() 
        cur.close()            

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Get_record_health(Record_id):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select time_month,health_status from health where record_id='%s'"%Record_id
        cur.execute(sql1)
        result=cur.fetchall()
        conn.commit()
        cur.close()  
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__== "__main__":
    print get_by_username('wind')
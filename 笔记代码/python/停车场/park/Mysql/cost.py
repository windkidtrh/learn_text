#-*-coding:utf-8-*- 
import mysql
import MySQLdb
TIMEFORMAT= "%Y.%m.%d %H.%M.%S"
import time 
import datetime

def get_by_user_id(User_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from user where user_id='%s'"%User_id
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_by_user_id_from_balance(User_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from balance where user_id='%s'"%User_id
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Balance(User_id,User_balance,Password):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1 = "update balance set user_balance='%s',password='%s' where user_id='%s' "%(User_balance,Password,User_id)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Show_balance(User_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select user_balance from balance where user_id='%s'"%(User_id)
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Start_indent(User_id,Park_id,Park_name,Payment_status,Power):
    try:
        Gettime10=time.strftime(TIMEFORMAT,time.localtime())
        Gettime20=datetime.datetime.now()
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into indent(user_id,park_id,park_name,payment_status,start_time,time_date,power) values ('%s','%s','%s','%s','%s','%s','%s')"%(User_id,Park_id,Park_name,Payment_status,Gettime10,Gettime20,Power)
        cur.execute(sql1)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql2="select indent_id from indent where (user_id,park_id,payment_status) in (('%s','%s','%s'))"%(User_id,Park_id,Payment_status)
        cur.execute(sql2)
        result = cur.fetchone()#暂时默认订单次数为1次
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql6="select park_surplus from park_stall where park_id='%s'"%(Park_id)
        cur.execute(sql6)
        result3 = cur.fetchone()
        conn.commit()
        cur.close()   

        message_list=[]
        for int_word in result3:
            message_list.append(int_word)
        new_surplus=message_list[0]-1

        cur = conn.cursor()
        sql7= "update park_stall set park_surplus='%s'where park_id='%s' "%(new_surplus,Park_id)
        cur.execute(sql7)
        conn.commit()
        cur.close()  

        cur = conn.cursor()
        sql3="select park_book from park_stall where park_id='%s'"%(Park_id)
        cur.execute(sql3)
        result4 = cur.fetchone()
        conn.commit()
        cur.close()  

        new_book=result4[0]+1

        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql4 = "update park_stall set park_book='%s' where park_id='%s' "%(new_book,Park_id)
        cur.execute(sql4)
        conn.commit()
        cur.close()    
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_by_indent_id(Indent_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from indent where indent_id='%s'"%Indent_id
        cur.execute(sql)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_by_indent(Park_id,User_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select payment_status from indent where (user_id,park_id) in (('%s','%s'))"%(User_id,Park_id)
        cur.execute(sql)
        result1 = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        result=[]
        for message in result1:
            result.append(message[0])
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
def Finish_indent(Indent_id,User_id,Park_id,Payment_status,Power):
    try:
        Gettime1=time.strftime(TIMEFORMAT,time.localtime())
        Gettime2=datetime.datetime.now()
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1 = "update indent set payment_time='%s',payment_status='%s',power='%s' where indent_id='%s' "%(Gettime1,Payment_status,Power,Indent_id)
        cur.execute(sql1)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql2="select time_date from indent where indent_id='%s'"%(Indent_id)
        cur.execute(sql2)
        result = cur.fetchone()
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql3="select user_balance from balance where user_id='%s'"%(User_id)
        cur.execute(sql3)
        result1 = cur.fetchone()
        conn.commit()
        cur.close()
        result1_list=[]
        for result1_word in result1:
            result1_list.append(result1_word)
        # return result[0],Gettime2
        cur = conn.cursor()
        sql4="select price from park_message where park_id='%s'"%(Park_id)
        cur.execute(sql4)
        result2 = cur.fetchone()
        conn.commit()
        cur.close()
        result2_list=[]
        for result2_word in result2:
            result2_list.append(result2_word)

        get1=(Gettime2-result[0]).seconds#用时
        if get1<=3600 :
            get2=1
        elif get1>3600:
            get2=(get1/3600)+1
        cost1=get2*result2_list[0]

        least_balance=result1_list[0]-cost1

        cur = conn.cursor()
        sql5= "update balance set user_balance='%s' where user_id='%s' "%(least_balance,User_id)
        cur.execute(sql5)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql6="select park_surplus,park_used,park_all from park_stall where park_id='%s'"%(Park_id)
        cur.execute(sql6)
        result3 = cur.fetchone()
        conn.commit()
        cur.close()   

        new_surplus=result3[0]+1
        new_used=result3[1]-1 

        cur = conn.cursor()
        sql7= "update park_stall set park_surplus='%s',park_used='%s' where park_id='%s' "%(new_surplus,new_used,Park_id)
        cur.execute(sql7)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql8= "update indent set cost_price='%s' where indent_id='%s' "%(cost1,Indent_id)
        cur.execute(sql8)
        conn.commit()
        cur.close()
        # return get1,get2,cost1,least_balance,new_surplus

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Show_indent(User_id):
    try:
        conn = mysql.connect_mysql()
        cur = conn.cursor()
        sql = "select * from indent where user_id='%s'"%User_id
        cur.execute(sql)
        result = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_news_for_comer_car(Indent_id):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="update indent set power='%s'where indent_id='%s' "%(0,Indent_id)
        cur.execute(sql1)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql2="select park_id from indent where indent_id='%s'"%(Indent_id)
        cur.execute(sql2)
        result = cur.fetchone()
        conn.commit()
        cur.close() 

        cur = conn.cursor()
        sql3="select park_book,park_used from park_stall where park_id='%s'"%(result)
        cur.execute(sql3)
        result4 = cur.fetchone()
        conn.commit()
        cur.close()  

        new_book=result4[0]-1
        new_used=result4[1]+1

        cur = conn.cursor()
        sql4 = "update park_stall set park_book='%s',park_used='%s' where park_id='%s' "%(new_book,new_used,result[0])
        cur.execute(sql4)
        conn.commit()
        cur.close()    

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Update_news_for_outer_car(Indent_id):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="update indent set power='%s'where indent_id='%s' "%(0,Indent_id)
        cur.execute(sql1)
        conn.commit()
        cur.close()   

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__== "__main__":
    print get_by_username('wind')
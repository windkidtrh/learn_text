#-*-coding:utf-8-*- 
import mysql
import MySQLdb
import random
def Get_last_value():
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select last_value from save_tmp_value"
        cur.execute(sql1)
        result=cur.fetchone()
        conn.commit()
        cur.close()

        if result[0]==99999999:
            renew=1
            cur = conn.cursor()
            sql2="update save_tmp_value set last_value='%s'"%(renew)
            cur.execute(sql2)
            conn.commit()
            cur.close()        
            return renew
        else:
            cur = conn.cursor()
            sql3="update save_tmp_value set last_value='%s'"%(result[0]+1)
            cur.execute(sql3)
            conn.commit()
            cur.close()        
            return result[0]+1

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Get_message_inNum12(First_type,Second_type,Product_num,Life):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql="update manage_request set life='%s' where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(int(Life)-1,First_type,Second_type,Product_num)
        cur.execute(sql)
        conn.commit()
        cur.close()

        cur = conn.cursor()
        sql1="select * from manage_request where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(First_type,Second_type,Product_num)
        cur.execute(sql1)
        result=cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Delete_message_inNum12(First_type,Second_type,Product_num):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="delete from manage_request where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(First_type,Second_type,Product_num)
        cur.execute(sql1)
        result=cur.fetchone()
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])    

def Update_Num12(First_type,Second_type,Product_num,Request_value,State):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="update manage_request set life='%s',request_value='%s',state='%s' where(first_type,second_type,product_num) in (('%s','%s','%s'))"%(6,Request_value,State,First_type,Second_type,Product_num)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Insert_Num12(First_type,Second_type,Product_num,Request_value,State):
   # return "hah1"
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into manage_request(first_type,second_type,product_num,life,request_value,state) values ('%s','%s','%s','%s','%s','%s')"%(First_type,Second_type,Product_num,6,Request_value,State)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Product_Exist_inNum2(First_type,Second_type,Product_num):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select * from product_current_state where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(First_type,Second_type,Product_num)
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def Product_Exist_inNum12(First_type,Second_type,Product_num):
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="select * from manage_request where (first_type,second_type,product_num) in (('%s','%s','%s'))"%(First_type,Second_type,Product_num)
        cur.execute(sql1)
        result = cur.fetchone()
        conn.commit()
        cur.close()
        return result

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def test_insert():
    test_a=''
    test_b=''
    list_random="0123456789"
    slice_r=random.sample(list_random,5)
    slice_c=random.sample(list_random,5)
    test_a=test_a.join(slice_r)
    test_b=test_b.join(slice_c)
    print test_a,test_b
    try:
        conn=mysql.connect_mysql()
        cur = conn.cursor()
        sql1="insert into test(test1,test2) values ('%s','%s')"%(test_a,test_b)
        cur.execute(sql1)
        conn.commit()
        cur.close()

    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

#-*-coding:utf-8-*- 
from TestModel.models import SaveTmpValue,Log,ManageRequest,LogSwitch,LogDrive#,SetTimer,LogTimer,RoomSetTemp,RoomProduct
import time
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
def Get_last_value(value_id=1):
    try:
        result = SaveTmpValue.objects.get(id=value_id)
        if result.last_value == 99999999:
            renew = 1
            SaveTmpValue.objects.filter(id=value_id).update(last_value = renew)     
            return renew
        else:
            SaveTmpValue.objects.filter(id=value_id).update(last_value = result.last_value+1)      
            return result.last_value+1

    except:
        print "Get_last_value Error"

def Get_message_inNum12(First_type,Second_type,Product_num,Life):
    try:
        ManageRequest.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num).update(life = int(Life)-1)
        return ManageRequest.objects.get(first_type=First_type,second_type=Second_type,product_num=Product_num)

    except:
        print "Get_message_inNum12 Error"

def Delete_message_inNum12(First_type,Second_type,Product_num):
    try:
        ManageRequest.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num).delete()

    except:
        print "Delete_message_inNum12 Error"

def Update_Num12(First_type,Second_type,Product_num,Request_value,State):
    try:
        ManageRequest.objects.filter(first_type=First_type,second_type=Second_type,product_num=Product_num).update(life = 6,request_value = Request_value,state= State)

    except:
        print "Update_Num12 Error"

def Insert_Num12(First_type,Second_type,Product_num,Request_value,State):
    try:
        ManageRequest.objects.create(first_type=First_type,second_type=Second_type,product_num=Product_num,life=6,request_value=Request_value,return_value=0,state=State)

    except:
        print "Insert_Num12 Error"

def Insert_log(User_id,Info):

    try:
        Current_time=time.strftime(TIMEFORMAT,time.localtime())
        Log.objects.create(user_id=User_id,the_time=Current_time,info=Info)

    except:
        print "Insert_log Error"

def Insert_log_switch(First_type,Second_type,Product_num,Info):
    try:
        Current_time=time.strftime(TIMEFORMAT,time.localtime())
        LogSwitch.objects.create(first_type=First_type,second_type=Second_type,product_num=Product_num,the_time=Current_time,info=Info)
        # # Current_time=time.ctime()
        # # return Current_time
        # conn=mysql.connect_mysql()
        # cur = conn.cursor()
        # sql1="insert into log_switch(first_type,second_type,product_num,the_time,info) values ('%s','%s','%s','%s','%s')"%(First_type,Second_type,Product_num,str(Current_time),Info)
        # # return sql1
        # cur.execute(sql1)
        # conn.commit()
        # cur.close()

    except:
        print "Insert_log_switch Error"

def Insert_log_drive(First_type,Second_type,Device_nums,Current_status,Info):
   # return "hah1"
    try:
        Current_time=time.strftime(TIMEFORMAT,time.localtime())
        LogSwitch.objects.create(first_type=First_type,second_type=Second_type,device_nums=Device_nums,the_time=Current_time,current_status=Current_status,info=Info)
        # # Current_time=time.ctime()
        # # return Current_time
        # conn=mysql.connect_mysql()
        # cur = conn.cursor()
        # sql1="insert into log_drive(first_type,second_type,device_nums,the_time,current_status,info) values ('%s','%s','%s','%s','%s','%s')"%(First_type,Second_type,Device_nums,str(Current_time),Current_status,Info)
        # # return sql1
        # cur.execute(sql1)
        # conn.commit()
        # cur.close()

    except:
        print "Insert_log_drive Error"

# def Insert_timer(User_id,First_type,Second_type,Product_num,State,Set_time,Set_day):
#    # return "hah1"
#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql1="insert into set_timer(user_id,first_type,second_type,product_num,state,set_time,set_day) values ('%s','%s','%s','%s','%s','%s','%s')"%(User_id,First_type,Second_type,Product_num,State,Set_time,Set_day)
#         cur.execute(sql1)
#         conn.commit()
#         cur.close()

#         cur = conn.cursor()
#         sql2="select * from set_timer where (user_id,first_type,second_type,product_num,state,set_time) in (('%s','%s','%s','%s','%s','%s'))"%(User_id,First_type,Second_type,Product_num,State,Set_time)
#         cur.execute(sql2)
#         result=cur.fetchone()
#         conn.commit()
#         cur.close()
#         return result[0]
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Timer_isExist(User_id,First_type,Second_type,Product_num,State,Set_time):
#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql2="select * from set_timer where (user_id,first_type,second_type,product_num,state,set_time) in (('%s','%s','%s','%s','%s','%s'))"%(User_id,First_type,Second_type,Product_num,State,Set_time)
#         cur.execute(sql2)
#         result=cur.fetchone()
#         conn.commit()
#         cur.close()
#         return result
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Update_timer(Timer_id,State,Set_time,Set_day):
#    # return "hah1"
#     try:
#         conn=mysql.connect_mysql()
#         if State!='':
#             cur = conn.cursor()
#             sql1="update set_timer set state='%s' where timer_id='%s'"%(State,Timer_id)
#             cur.execute(sql1)
#             conn.commit()
#             cur.close()
#         if Set_time!='':
#             cur = conn.cursor()
#             sql="update set_timer set set_time='%s' where timer_id='%s'"%(Set_time,Timer_id)
#             cur.execute(sql)
#             conn.commit()
#             cur.close()
#         if Set_day!='':
#             if Set_day=="7":
#                 cur = conn.cursor()
#                 sql="update set_timer set set_day='%s' where timer_id='%s'"%(Set_day,Timer_id)
#                 cur.execute(sql)
#                 conn.commit()
#                 cur.close()
#             else:
#                 cur = conn.cursor()#感觉这里多余
#                 sql="update set_timer set set_day='%s' where timer_id='%s'"%(Set_day,Timer_id)
#                 cur.execute(sql)
#                 conn.commit()
#                 cur.close()               

#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Timer_id_isExist(Timer_id):

#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql2="select * from set_timer where timer_id='%s'"%Timer_id
#         cur.execute(sql2)
#         result=cur.fetchone()
#         conn.commit()
#         cur.close()
#         return result
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Delete_timer(Timer_id):

#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql2="delete from set_timer where timer_id='%s'"%Timer_id
#         cur.execute(sql2)
#         conn.commit()
#         cur.close()

#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Show_timer():

#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql="select * from set_timer"
#         cur.execute(sql)
#         result = cur.fetchone()
#         conn.commit()
#         cur.close()

#         cur = conn.cursor()
#         sql1="select * from set_timer"
#         cur.execute(sql1)
#         result1 = cur.fetchall()
#         conn.commit()
#         cur.close()
#         if result==None:
#             return result
#         else:
#             return result1
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Log_timer(User_id,Timer_id,First_type,Second_type,Product_num,State,Set_time,Gettime1):
#    # return "hah1"
#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql1="insert into log_timer(user_id,timer_id,first_type,second_type,product_num,state,set_time,answer_time) values ('%s','%s','%s','%s','%s','%s','%s','%s')"%(User_id,Timer_id,First_type,Second_type,Product_num,State,Set_time,Gettime1)
#         cur.execute(sql1)
#         conn.commit()
#         cur.close()

#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Show_temp():

#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql="select * from room_set_temp"
#         cur.execute(sql)
#         result = cur.fetchone()
#         conn.commit()
#         cur.close()

#         cur = conn.cursor()
#         sql1="select * from room_set_temp"
#         cur.execute(sql1)
#         result1 = cur.fetchall()
#         conn.commit()
#         cur.close()
#         if result==None:
#             return result
#         else:
#             return result1
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

# def Show_Product_message(room_id):

#     try:
#         conn=mysql.connect_mysql()
#         cur = conn.cursor()
#         sql="select * from room_product where room_id='%s'"%room_id
#         cur.execute(sql)
#         result = cur.fetchone()
#         conn.commit()
#         cur.close()

#         cur = conn.cursor()
#         sql1="select * from room_product where room_id='%s'"%room_id
#         cur.execute(sql1)
#         result1 = cur.fetchall()
#         conn.commit()
#         cur.close()
#         if result==None:
#             return result
#         else:
#             return result1
#     except MySQLdb.Error,e:
#         print "Mysql Error %d: %s" % (e.args[0], e.args[1])
# -*- coding: utf-8 -*-

from django.http import HttpResponse#网页响应
from django.shortcuts import render_to_response#网页跳转
import Mysql.userWork
import Mysql.macWork
import json
import socket
import time
import logging_set.log_message
import Return_mess.return_mess
TIMEFORMAT = "%Y-%m-%d %H:%M:%S"
Current_time = time.strftime(TIMEFORMAT,time.localtime())
import sys   
reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
sys.setdefaultencoding('utf-8')
Host = "10.10.20.43"
Port = 12000
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 表单
def search_form(request):
    return render_to_response('search_form.html')

# 接收请求数据
def Online(request):  
    
    mess_get = ''

    try:
        mycallback = request.GET.get("callback","")
        is_manager = request.GET.get("is_manager","")
        mess_get = Return_mess.return_mess.return_message(a = 1,c = "hello world",callback = mycallback)

    except:
        mess_get = Return_mess.return_mess.return_message(b = 101,c = "hello world",d = "enter data is wrong",is_manager = is_manager,callback = mycallback)

    finally:
            return HttpResponse(mess_get)

def Control_mac(request):
    timer_stop = "false"
    mess_get = ''
    news_data = ''

    try:
        mycallback = request.GET.get("callback","")
        is_manager = request.GET.get("is_manager","")
        user_id = request.GET["user_id"]
        first_type = request.GET["first_type"]
        second_type = request.GET["second_type"]
        product_num = request.GET["product_num"]
        state = request.GET["state"]
        info = request.GET["info"]

    except:
        mess_get = Return_mess.return_mess.return_message(b = 101,d = "enter data is wrong",is_manager = is_manager,callback = mycallback)

    try:
        Mysql.userWork.Insert_log(user_id,info)
        Num4_message = Mysql.macWork.Product_isExist_inNum4(first_type,second_type,product_num,user_id)
        Num2_message = Mysql.macWork.Product_isExist_inNum2(first_type,second_type,product_num)#获取id，port，6,7
        if Num4_message != None:
            if Num2_message == None:
                mess_get = Return_mess.return_mess.return_message(b = 105,d = "data not in form_2,so the send_order hava not ip and port",is_manager = is_manager,callback = mycallback)

            else:
                pass

            Num12_message = Mysql.macWork.Product_isExist_inNum12(first_type,second_type,product_num)
            Request = Mysql.userWork.Get_last_value()
            Order_request = Return_mess.return_mess.Request_mess(Request)
            Order_send = "#" + state + "$" + Order_request + "@"
            try:
                if Num12_message != None :#存在的话更新
                    Mysql.userWork.Update_Num12(first_type,second_type,product_num,Request,state)
                else:
                    Mysql.userWork.Insert_Num12(first_type,second_type,product_num,Request,state)
            except:
                logging_set.log_message.logging.warning('error_code:105_mac')
                mess_get = Return_mess.return_mess.return_message(b = 109,d = "Num12_message have wrong",is_manager = is_manager,callback = mycallback)

            news_data = Return_mess.return_mess.return_message_datas(Order_send,Num2_message.ip_address,json.dumps(Num2_message.net_port))
            sock.sendto(json.dumps(news_data),(Host,int(Port)))

            try:
                while timer_stop == "false":#方便后面暂停
                    Num12_message_for_life = Mysql.macWork.Product_isExist_inNum12(first_type,second_type,product_num)
                    if Num12_message_for_life == None:
                        logging_set.log_message.logging.warning('error_code:in12_life_have_no_data_mac')
                        timer_stop = "true"#停止定时器

                    else:                          
                        stop_value = int(Num12_message_for_life.life)
                        time.sleep(1)#1s定时器
                        Timer_message_inNum12 = Mysql.userWork.Get_message_inNum12(first_type,second_type,product_num,Num12_message_for_life.life)
                        try:
                            if Timer_message_inNum12 == None:
                                logging_set.log_message.logging.warning('error_code:in12_have_no_data_mac')
                                timer_stop = "true"#停止定时器
                            else:
                                if str(Timer_message_inNum12.request_value) == str(Timer_message_inNum12.return_value):#请求值是否等于返回值
                                    Mysql.userWork.Delete_message_inNum12(first_type,second_type,product_num)
                                    mess_get = Return_mess.return_mess.return_message(a = 1,callback = mycallback)
                                    timer_stop = "true"#停止定时器

                                else:
                                    if stop_value == 0:#生存值是否为0
                                        Mysql.userWork.Delete_message_inNum12(first_type,second_type,product_num)
                                        mess_get = Return_mess.return_mess.return_message(b = 103,d = "product_num"+"_"+str(product_num)+"_send failed"+" and life=0",is_manager = is_manager,callback = mycallback)
                                        timer_stop = "true"#停止定时器

                                    else:
                                        if stop_value%2 == 1:
                                            pass

                                        else:
                                            Num12_message_for_request = Mysql.macWork.Product_isExist_inNum12(first_type,second_type,product_num)
                                            if Num12_message_for_request == None:
                                                logging_set.log_message.logging.warning('error_code:in12_request_have_no_data_mac')
                                                timer_stop = "true"#停止定时器 

                                            else:                       
                                                if Num12_message_for_request.request_value == Request:#判断当前请求值是否等于数据库的请求值
                                                    sock.sendto(json.dumps(news_data),(Host,int(Port)))

                                                else:
                                                    timer_stop = "true"#停止定时器,因为有新的命令
                                                    mess_get = Return_mess.return_mess.return_message(b = 113,d = "there have new order_mac",is_manager = is_manager,callback = mycallback)

                        except:
                            logging_set.log_message.logging.warning('error_code:222_mac_12_timer')
                            mess_get = Return_mess.return_mess.return_message(b = 222,d = "timer_12_mac have wrong",is_manager = is_manager,callback = mycallback)
               
            except:
                logging_set.log_message.logging.warning('error_code:104_mac')
                mess_get = Return_mess.return_mess.return_message(b = 104,d = "timer have wrong",is_manager = is_manager,callback = mycallback)

        else:
            logging_set.log_message.logging.warning('error_code:110_mac')
            mess_get = Return_mess.return_mess.return_message(b = 110,d = "data not in form_4",is_manager = is_manager,callback = mycallback)                

    except:
        logging_set.log_message.logging.warning('error_code:102_mac')
        mess_get = Return_mess.return_mess.return_message(b = 102,d = "code have wrong",is_manager = is_manager,callback = mycallback)

    finally:
        return HttpResponse(mess_get)

def Control_switch(request):
    timer_stop = "false"
    mess_get = ''
    news_data = ''

    try:
        mycallback = request.GET.get("callback","")
        is_manager = request.GET.get("is_manager","")
        first_type = request.GET["first_type"]
        second_type = request.GET["second_type"]
        product_num = request.GET["product_num"]
        state = request.GET["state"]

    except:
        mess_get = Return_mess.return_mess.return_message(b = 101,d = "enter data is wrong",is_manager = is_manager,callback = mycallback)

    try:
        Num11_message = Mysql.macWork.Product_isExist_inNum11(first_type,second_type,product_num)
        if Num11_message == None :#判断是否在表11
            mess_get = Return_mess.return_mess.return_message(b = 106,d = "data not in form_11",is_manager = is_manager,callback = mycallback)

        else:
            Request = Mysql.userWork.Get_last_value(2) #当前的请求值
            Ip_list = []
            Port_list = []
            First_type_list = []
            Second_type_list = []
            Product_num_list = []
            for target_message in Num11_message:
                Num2_message = Mysql.macWork.Product_isExist_inNum2(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num)#获取id，port，6,7
                Num12_message = Mysql.macWork.Product_isExist_inNum12(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num)

                try:
                    if Num2_message == None:
                        pass

                    else:
                        Ip_list.append(Num2_message.ip_address)
                        Port_list.append(Num2_message.net_port)
                        First_type_list.append(target_message.target_first_type)
                        Second_type_list.append(target_message.target_second_type)
                        Product_num_list.append(target_message.target_product_num)

                        try:
                            if Num12_message != None:
                                Mysql.userWork.Update_Num12(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num,Request,state)

                            else :
                                Mysql.userWork.Insert_Num12(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num,Request,state)

                        except:
                            logging_set.log_message.logging.warning('error_code:108_switch')
                            mess_get = Return_mess.return_mess.return_message(b = 108,d = "check form_12 hava wrong",is_manager = is_manager,callback = mycallback)

                except:
                    logging_set.log_message.logging.warning('error_code:107_switch')
                    mess_get = Return_mess.return_mess.return_message(b = 107,d = "check form_2 hava wrong",is_manager = is_manager,callback = mycallback)

            Order_request = Return_mess.return_mess.Request_mess(Request)
            Order_send = "#" + state + "$" + Order_request + "@"#生成指令，格式如：#00_00_00$00000001@                    

            if len(Ip_list)==0:
                mess_get = Return_mess.return_mess.return_message(b = 105,d = "data not in form_2,so the send_order hava not ip and port",is_manager = is_manager,callback = mycallback)
                pass

            else:
                i = 0
                while i < len(Ip_list):
                    news_data = Return_mess.return_mess.return_message_datas(Order_send,Ip_list[i],json.dumps(Port_list[i]))
                    sock.sendto(json.dumps(news_data),(Host,int(Port)))
                    i = i + 1

                try:    
                    while timer_stop == "false":#方便后面暂停
                        def remove_list(num_list):
                            Ip_list.remove(Ip_list[num_list])
                            Port_list.remove(Port_list[num_list])
                            First_type_list.remove(First_type_list[num_list])
                            Second_type_list.remove(Second_type_list[num_list])
                            Product_num_list.remove(Product_num_list[num_list])

                        Num12_message_for_life = Mysql.macWork.Product_isExist_inNum12(First_type_list[0],Second_type_list[0],Product_num_list[0])
                        if Num12_message_for_life == None:
                            logging_set.log_message.logging.warning('error_code:in12_life_have_no_data_switch')
                            timer_stop = "true"#停止定时器
                        else:                               
                            stop_value = Num12_message_for_life.life
                            time.sleep(1)#1s定时器
                            Device_num = 0
                            while Device_num < len(Ip_list):
                                Timer_message_inNum12 = Mysql.userWork.Get_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],Product_num_list[int(Device_num)],Num12_message_for_life.life)
                                try:
                                    if Timer_message_inNum12 == None:
                                        logging_set.log_message.logging.warning('error_code:in12_have_no_data_switch')
                                        timer_stop = "true"#停止定时器

                                    else:
                                        def Delete_12(Device_num):
                                                Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],Product_num_list[int(Device_num)])        
                                        if str(Timer_message_inNum12.request_value) == str(Timer_message_inNum12.return_value):#请求值是否等于返回值
                                            if len(Ip_list) == 1:
                                                Delete_12(Device_num)
                                                Device_num = int(Device_num) + 1
                                                mess_get = Return_mess.return_mess.return_message(a = 1,callback = mycallback)
                                                timer_stop = "true"#停止定时器

                                            else:
                                                Delete_12(Device_num)
                                                remove_list(Device_num)

                                        else:
                                            if stop_value == 0:#生存值是否为0
                                                if len(Ip_list) == 1:
                                                    Delete_12(Device_num)
                                                    remove_list(Device_num)
                                                    mess_get = Return_mess.return_mess.return_message(b = 103,d="send failed and life = 0",is_manager = is_manager,callback = mycallback)
                                                    timer_stop = "true"#停止定时器


                                                else:
                                                    Delete_12(Device_num)
                                                    remove_list(Device_num)

                                            else:
                                                if stop_value%2 == 1:
                                                    Device_num = int(Device_num) + 1
                                                    pass 
                                                else:
                                                    Num12_message_for_request = Mysql.macWork.Product_isExist_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],Product_num_list[int(Device_num)])
                                                    if Num12_message_for_request == None:
                                                        logging_set.log_message.logging.warning('error_code:in12_request_have_no_data_switch')
                                                        timer_stop="true"#停止定时器
                                                    else:
                                                        if Num12_message_for_request.request_value == Request:#判断当前请求值是否等于数据库的请求值                                   
                                                            news_data = Return_mess.return_mess.return_message_datas(Order_send,Ip_list[int(Device_num)],json.dumps(Port_list[int(Device_num)]))
                                                            sock.sendto(json.dumps(news_data),(Host,int(Port)))
                                                            Device_num = int(Device_num) + 1  

                                                        else:
                                                            if len(Ip_list) == 1:
                                                                Device_num = int(Device_num) + 1 
                                                                timer_stop = "true"#停止定时器,因为有新的命令
                                                                mess_get = Return_mess.return_mess.return_message(b = 111,d = "there have new order_switch,Ip_list=1",is_manager = is_manager,callback = mycallback)

                                                            else:
                                                                Device_num = int(Device_num) + 1
                                                                if Device_num == len(Ip_list):
                                                                    timer_stop = "true"#停止定时器,因为有新的命令
                                                                    mess_get = Return_mess.return_mess.return_message(b = 112,d = "there have new order_switch",is_manager = is_manager,callback = mycallback)

                                except:
                                    logging_set.log_message.logging.warning('error_code:223_switch_timer_12')
                                    mess_get = Return_mess.return_mess.return_message(b = 223,d = "timer_12_switch have wrong",is_manager = is_manager,callback = mycallback)
              
                except:
                    logging_set.log_message.logging.warning('error_code:104_switch_timer')
                    mess_get = Return_mess.return_mess.return_message(b = 104,d = "timer have wrong",is_manager = is_manager,callback = mycallback)

    except:
        logging_set.log_message.logging.warning('error_code:102_switch')
        mess_get = Return_mess.return_mess.return_message(b = 107,d = "code have wrong",is_manager = is_manager,callback = mycallback)

    finally:
        return HttpResponse(mess_get)

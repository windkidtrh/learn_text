#-*-coding:utf-8-*-
import SocketServer
import socket
import threading
import traceback
import json
import demjson
import time
import sys
import thread
reload(sys) 
sys.setdefaultencoding('utf8')
import logging_set.log_message
import Return_mess.return_mess
# HOST = "192.168.1.102" #localhost
# HOST="47.92.49.44"
# HOST="172.26.55.190"
HOST = "10.10.20.43"
PORT = 12000
# def cut_online_value():
#     print "gaga"
#     thread.start_new_thread(Mysql.macWork.Mac_is_not_in,())
#     timer=threading.Timer(5,cut_online_value)
#     timer.start()
# timer=threading.Timer(5,cut_online_value)
# timer.start()

class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print data,socket
#         thread.start_new_thread(handle_message, (data, self.client_address, socket )) 

# def handle_message(data, addr, socket):
#     if "state" in data and "ip_message" in data and "port_message" in data:
#         try:
#             datas = demjson.decode(data)
#             state = datas["state"]
#             ip_message = datas["ip_message"]
#             port_message = datas["port_message"]
#             try:
#                 socket.sendto(state,(ip_message,int(port_message)))

#             except:
#                 logging_set.log_message.logging.warning('error_code:104_udp_first_control_send')
 
#         except:
#             logging_set.log_message.logging.warning('error_code:102_udp_first')
      
#     if "first_type" in data and "second_type" in data and "device_number" in data and "current_status" in data and "request" in data :
#         try:
#             datas = demjson.decode(data)
#             First_type = datas["first_type"]
#             Second_type = datas["second_type"]
#             Device_nums = datas["device_number"]
#             Current_status = datas["current_status"]
#             Request = datas["request"]
#             Mysql.userWork.Insert_log_drive(First_type,Second_type,Device_nums,Current_status,Request)
#             Num1_message = Mysql.macWork.Product_isExist_inNum1(First_type,Second_type,Device_nums)
#             Num2_message = Mysql.macWork.Product_isExist_inNum2(First_type,Second_type,Device_nums)
#             Num12_message = Mysql.macWork.Product_isExist_inNum12(First_type,Second_type,Device_nums)
       
#             if Num1_message != None:
#                 if Num2_message == None:
#                     Mysql.macWork.Register_mac(First_type,Second_type,Device_nums,Current_status,addr[0],addr[1])
#                 else:
#                     Mysql.macWork.Update_mac(First_type,Second_type,Device_nums,Current_status,addr[0],addr[1])
#                     if Num12_message != None:
#                         if Num12_message.return_value == Request: 
#                             pass
#                         else:
#                             Mysql.macWork.Update_Return_value(First_type,Second_type,Device_nums,int(Request))

#                     else:
#                         pass
#             else:
#                 logging_set.log_message.logging.warning('error_code:not in form_1_udp_second')
#                 pass
#         except:
#             logging_set.log_message.logging.warning('error_code:103_udp_second')

#     if "first_type" in data and "second_type" in data and "product_num" in data and "state" in data :
#         timer_stop = "false"

#         try:
#             datas = demjson.decode(data)
#             first_type = datas["first_type"]
#             second_type = datas["second_type"]
#             product_num = datas["product_num"]
#             State = datas["state"]
#             info = State["current_status"]
#             Mysql.userWork.Insert_log_switch(first_type,second_type,product_num,info)

#         except:
#             logging_set.log_message.logging.warning('error_code:103_udp_third')

#         if info == "online":
#             pass
#         else:    
#             try:
#                 Num11_message = Mysql.macWork.Product_isExist_inNum11(first_type,second_type,product_num)
#                 if Num11_message == None :#判断是否在表11
#                     logging_set.log_message.logging.warning('error_code:106_udp_third_not_in_11')

#                 else:
#                     Request = Mysql.userWork.Get_last_value() #当前的请求值
#                     Ip_list = []
#                     Port_list = []
#                     First_type_list = []
#                     Second_type_list = []
#                     Product_num_list = []
#                     for target_message in Num11_message:
#                         Num2_message = Mysql.macWork.Product_isExist_inNum2(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num)#获取id，port，6,7
#                         Num12_message = Mysql.macWork.Product_isExist_inNum12(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num)

#                         try:
#                             if Num2_message == None:
#                                 pass

#                             else:
#                                 Ip_list.append(Num2_message.ip_address)
#                                 Port_list.append(Num2_message.net_port)
#                                 First_type_list.append(target_message.target_first_type)
#                                 Second_type_list.append(target_message.target_second_type)
#                                 Product_num_list.append(target_message.target_product_num)
#                                 try:
#                                     if Num12_message != None:
#                                         Mysql.userWork.Update_Num12(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num,Request,json.dumps(State))

#                                     else :
#                                         Mysql.userWork.Insert_Num12(target_message.target_first_type,target_message.target_second_type,target_message.target_product_num,Request,json.dumps(State))

#                                 except:
#                                     logging_set.log_message.logging.warning('error_code:108_udp_third')

#                         except:
#                             logging_set.log_message.logging.warning('error_code:107_udp_third')

#                     Order_request = Return_mess.return_mess.Request_mess(Request)
#                     a = State["current_status"]#字符串变成json
#                     Order_send = "#" + str(a) + "$" + Order_request + "@"#生成指令，格式如：00_00_00_00000001                                    

#                     if len(Ip_list) == 0:
#                         logging_set.log_message.logging.warning('error_code:105_udp_third_not_in_2')
#                         pass
#                     else:                
#                         i = 0
#                         while i < len(Ip_list):
#                             socket.sendto(Order_send,(Ip_list[i],Port_list[i]))
#                             i = i + 1
#                         try:   
#                             while timer_stop == "false":#方便后面暂停
#                                 def remove_list(num_list):
#                                     Ip_list.remove(Ip_list[num_list])
#                                     Port_list.remove(Port_list[num_list])
#                                     First_type_list.remove(First_type_list[num_list])
#                                     Second_type_list.remove(Second_type_list[num_list])
#                                     Product_num_list.remove(Product_num_list[num_list])  
#                                 Num12_message_for_life = Mysql.macWork.Product_isExist_inNum12(First_type_list[0],Second_type_list[0],Product_num_list[0])
#                                 if Num12_message_for_life == None:
#                                     logging_set.log_message.logging.warning('error_code:in12_life_have_no_data_udp')
#                                     timer_stop = "true"#停止定时器

#                                 else:
#                                     stop_value = Num12_message_for_life.life
#                                     time.sleep(1)#1s定时器
#                                     Device_num = 0

#                                     while Device_num < len(Ip_list):
#                                         Timer_message_inNum12 = Mysql.userWork.Get_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],Product_num_list[int(Device_num)],Num12_message_for_life.life)

#                                         try:
#                                             if Timer_message_inNum12 == None:
#                                                 logging_set.log_message.logging.warning('error_code:in12_have_no_data_udp')
#                                                 timer_stop = "true"#停止定时器

#                                             else:
#                                                 def Delete_12(Device_num):
#                                                     Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],Product_num_list[int(Device_num)])

#                                                 if str(Timer_message_inNum12.request_value) == str(Timer_message_inNum12.return_value):#请求值是否等于返回值
#                                                     if len(Ip_list) == 1:
#                                                         Delete_12(Device_num)
#                                                         Device_num = int(Device_num) + 1 
#                                                         timer_stop = "true"#停止定时器

#                                                     else:
#                                                         Delete_12(Device_num)
#                                                         remove_list(Device_num)

#                                                 else:
#                                                     if stop_value == 0:#生存值是否为0
#                                                         if len(Ip_list) == 1:
#                                                             Delete_12(Device_num)
#                                                             remove_list(Device_num)
#                                                             logging_set.log_message.logging.warning('error_code:109_udp_third_life==0,delete,Ip_list=1') 
#                                                             timer_stop = "true"#停止定时器

#                                                         else:
#                                                             Delete_12(Device_num)
#                                                             remove_list(Device_num)           

#                                                     else:
#                                                         if stop_value%2 == 1:
#                                                             Device_num = int(Device_num) + 1
#                                                             pass 
#                                                         else:
#                                                             Num12_message_for_request = Mysql.macWork.Product_isExist_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],Product_num_list[int(Device_num)])
#                                                             if Num12_message_for_request == None:
#                                                                 logging_set.log_message.logging.warning('error_code:in12_request_have_no_data_udp')
#                                                                 timer_stop = "true"#停止定时器
#                                                             else: 
#                                                                 if Num12_message_for_request.return_value == Request:#判断当前请求值是否等于数据库的请求值
#                                                                     socket.sendto(Order_send,(Ip_list[int(Device_num)],Port_list[int(Device_num)]))
#                                                                     Device_num = int(Device_num) + 1  

#                                                                 else:
#                                                                     if len(Ip_list) == 1:
#                                                                         Device_num = int(Device_num) + 1 
#                                                                         timer_stop = "true"#停止定时器,因为有新的命令

#                                                                     else:

#                                                                         Device_num = int(Device_num) + 1
#                                                                         if Device_num == len(Ip_list):
#                                                                             timer_stop = "true"#停止定时器,因为有新的命令

#                                         except:
#                                             logging_set.log_message.logging.warning('error_code:222_udp_third')

#                         except:
#                             logging_set.log_message.logging.warning('error_code:104_udp_third')

#             except:
#                 logging_set.log_message.logging.warning('error_code:102_udp_third')

def startservice():#启动udp
    server = SocketServer.UDPServer((HOST, int(PORT)), MyUDPHandler)
    server.serve_forever()
# if __name__ == "__main__":
#     server = SocketServer.UDPServer((HOST, int(PORT)), MyUDPHandler)
#     server.serve_forever()
    # startservice().start()
    # try:
    #     threading.Thread(target=udpserver.startservice).start()   
    # except:
    #     logging_set.log_message.logging.warning('fail to create threads')

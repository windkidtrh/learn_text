#-*-coding:utf-8-*-
import SocketServer
import socket
import Mysql.mysql
import threading
import traceback
import json
import demjson
import time
import Mysql.macWork
import Mysql.userWork
import sys
import thread
import threading
reload(sys) 
sys.setdefaultencoding('utf8')
# HOST = "10.10.33.37" #localhost
HOST="120.27.95.22"
PORT = 12000
def cut_online_value():#定时器，每5分钟将数据库中的值减1
    thread.start_new_thread(Mysql.macWork.Mac_is_not_in,())
    print "udp_timer is ok"
    timer=threading.Timer(150,cut_online_value)
    timer.start()
timer=threading.Timer(150,cut_online_value)
timer.start()

class MyUDPHandler(SocketServer.BaseRequestHandler):#处理UDP数据
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        thread.start_new_thread(handle_message, (data, self.client_address, socket ))  
        # print data
def handle_message(data, addr, socket):
    if "state" in data and "ip_message" in data and "port_message" in data:#接收接口的信息，并发回到对方udp
        try:
            datas=demjson.decode(data)
            state=datas["state"]
            ip_message=datas["ip_message"]
            port_message=datas["port_message"]
            print ip_message,port_message,state
            try:
                socket.sendto(state,(ip_message,int(port_message)))
                print "ssss"
            except:
                f=open("log.txt",'a')
                f.write("error_code:104_udp_first_control_send\n")  
                traceback.print_exc(file=f)  
                f.flush()  
                f.close() 
                error_msg = '''error_code:104;'''
                print error_msg
                # socket.sendto(error_msg, addr)   
        except:
            f=open("log.txt",'a') 
            f.write("error_code:102_udp_first\n") 
            traceback.print_exc(file=f)  
            f.flush()  
            f.close() 
            error_msg = '''error_code:102;'''
            print error_msg
            # socket.sendto(error_msg, addr)        
    if "first_type" in data and "second_type" in data and "device_number" in data and "current_status" in data and "request" in data :#处理设备udp信息
        # socket.sendto("success_connect", addr)
        try:
            datas=demjson.decode(data)
            First_type=datas["first_type"]
            Second_type=datas["second_type"]
            Device_nums=datas["device_number"]
            Current_status=datas["current_status"]
            Request=datas["request"]
            Mysql.userWork.Insert_log_drive(First_type,Second_type,Device_nums,Current_status,Request)
            print First_type,Second_type,Device_nums,Current_status,Request
            # socket.sendto(First_type,Second_type,Device_nums,Current_status,Request, addr)
            Num1_message=Mysql.macWork.Product_isExist_inNum1(First_type,Second_type,int(Device_nums))
            Num2_message=Mysql.macWork.Product_isExist_inNum2(First_type,Second_type,int(Device_nums))
            Num12_message=Mysql.macWork.Product_isExist_inNum12(First_type,Second_type,int(Device_nums))           
            print Num2_message,Num12_message,Num1_message
            if Num1_message!=None:
                if Num2_message==None:
                    Mysql.macWork.Register_mac(First_type,Second_type,int(Device_nums),Current_status,addr[0],addr[1])
                    print "register_mac"
                else:
                    Mysql.macWork.Update_mac(First_type,Second_type,int(Device_nums),Current_status,addr[0],addr[1])
                    print "Update_mac"
                    # socket.sendto("update_mac",addr)
                    if Num12_message!=None:
                        # print "data is exist",int(Num12_message[5]),int(Request),int(Num12_message[5])==int(Request)
                        # socket.sendto("data is exist",addr)
                        if Num12_message[5]==Request:
                            print "equal"
                            # socket.sendto("request == request in form_12", addr) 
                            pass
                        else:
                            Mysql.macWork.Update_Return_value(First_type,Second_type,int(Device_nums),int(Request))
                            print "Update_Return_value"
                            # socket.sendto("Update_Return_value success", addr)
                    else:
                        pass
            else:
                f=open("log.txt",'a')
                f.write("error_code:not in form_1_udp_second\n")  
                traceback.print_exc(file=f)  
                f.flush()  
                f.close() 
                print "not in form_1"
                pass
        except:
            f=open("log.txt",'a')
            f.write("error_code:103_udp_second\n")  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close() 
            error_msg = '''error_code:103_in_request;'''
            print error_msg

    if "first_type" in data and "second_type" in data and "product_num" in data and "state" in data :#处理开关udp信息
        timer_stop="false"
        # socket.sendto("success_connect2", addr)
        try:
            datas=demjson.decode(data)
            first_type=datas["first_type"]
            second_type=datas["second_type"]
            product_num=datas["product_num"]
            State=datas["state"]
            # info=json.loads("state")["current_status"]
            info=State["current_status"]
            Mysql.userWork.Insert_log_switch(first_type,second_type,product_num,info)
            print data
            # print first_type,second_type,product_num,State,info
            # gg=str(state)
        except:
            f=open("log.txt",'a')
            f.write("error_code:103_udp_third\n")  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close() 
            error_msg = '''error_code:103_in_state;'''
            print error_msg
            # socket.sendto(error_msg, addr)
        if info=="online":#判断是否在线
            pass
        else:    
            try:
                Num11_message=Mysql.macWork.Product_isExist_inNum11(first_type,second_type,int(product_num))
                if Num11_message == None :#判断是否在表11
                    f=open("log.txt",'a')
                    f.write("error_code:106_udp_third_not_in_11\n")   
                    traceback.print_exc(file=f)  
                    f.flush()  
                    f.close() 
                    error_msg = '''error_code:106;not in 11'''
                    print error_msg
                    # socket.sendto(error_msg, addr)
                else:
                    Request=Mysql.userWork.Get_last_value() #当前的请求值
                    Ip_list=[]
                    Port_list=[]
                    First_type_list=[]
                    Second_type_list=[]
                    Product_num_list=[]
                    for target_message in Num11_message:
                        Num2_message=Mysql.macWork.Product_isExist_inNum2(target_message[3],target_message[4],int(target_message[5]))#获取id，port，6,7
                        Num12_message=Mysql.macWork.Product_isExist_inNum12(target_message[3],target_message[4],int(target_message[5]))
                        print Num2_message,Num12_message
                        # return First_type_list,Second_type_list,Product_num_list
                        try:
                            if Num2_message==None:
                                pass
                                # socket.sendto(error_msg, addr)
                            else:
                                Ip_list.append(Num2_message[5])
                                Port_list.append(Num2_message[6])
                                First_type_list.append(target_message[3])
                                Second_type_list.append(target_message[4])
                                Product_num_list.append(target_message[5])
                                try:
                                    if Num12_message != None:
                                        Mysql.userWork.Update_Num12(target_message[3],target_message[4],int(target_message[5]),Request,json.dumps(State))
                                        print "i am in update"
                                    else :
                                        Mysql.userWork.Insert_Num12(target_message[3],target_message[4],int(target_message[5]),Request,json.dumps(State))
                                        # print haha
                                        print "i am in Insert"
                                except:
                                    f=open("log.txt",'a')
                                    f.write("error_code:108_udp_third\n")   
                                    traceback.print_exc(file=f)  
                                    f.flush()  
                                    f.close() 
                                    error_msg = '''error_code:108;'''
                                    print error_msg
                                # return Ip_list,Port_list
                        except:
                            f=open("log.txt",'a')
                            f.write("error_code:107_udp_third\n")   
                            traceback.print_exc(file=f)  
                            f.flush()  
                            f.close() 
                            error_msg = '''error_code:107;'''
                            print error_msg
                            # socket.sendto(error_msg, addr)
                        print target_message[3],target_message[4],int(target_message[5])
                            # socket.sendto(error_msg, addr)
                    # return Ip_list[0],Port_list[0],First_type_list[0],Second_type_list[0],Product_num_list[0]
                    print Ip_list,Port_list,First_type_list,Second_type_list,Product_num_list                                                       
                    if len(str(Request))==1:
                        Order_request="0000000"+str(Request)
                    elif len(str(Request))==2:
                        Order_request="000000"+str(Request)
                    elif len(str(Request))==3:
                        Order_request="00000"+str(Request)
                    elif len(str(Request))==4:
                        Order_request="0000"+str(Request)
                    elif len(str(Request))==5:
                        Order_request="000"+str(Request)
                    elif len(str(Request))==6:
                        Order_request="00"+str(Request)
                    elif len(str(Request))==7:
                        Order_request="0"+str(Request)
                    elif len(str(Request))==8:
                        Order_request=str(Request)#生成指令结尾格式
                    # return Order_request
                    a=State["current_status"]#字符串变成json
                    Order_send="#"+str(a)+"$"+Order_request+"@"#生成指令，格式如：00_00_00_00000001                    
                    print a,Order_send
                    if len(Ip_list)==0:
                        f=open("log.txt",'a')
                        f.write("error_code:105_udp_third_not_in_2\n")   
                        traceback.print_exc(file=f)  
                        f.flush()  
                        f.close() 
                        error_msg = '''error_code:105;not in 2'''
                        print error_msg
                        pass
                    else:                
                        i=0
                        # return Ip_list[int(send_number)],Port_list[int(send_number)]
                        while i <len(Ip_list):
                            socket.sendto(Order_send,(Ip_list[i],Port_list[i]))
                            print Ip_list[i],Port_list[i]
                            i=i+1
                        try:   
                            while timer_stop=="false":#方便后面暂停
                                print "i am in timer"
                                # print First_type_list[0],Second_type_list[0],int(Product_num_list[0])
                                Num12_message_for_life=Mysql.macWork.Product_isExist_inNum12(First_type_list[0],Second_type_list[0],int(Product_num_list[0]))
                                print Num12_message_for_life
                                if Num12_message_for_life==None:
                                    f=open("log.txt",'a')
                                    f.write("error_code:in12_life_have_no_data_udp\n")   
                                    traceback.print_exc(file=f)  
                                    f.flush()  
                                    f.close()
                                    timer_stop="true"#停止定时器
                                    # pass
                                else:
                                    stop_value=Num12_message_for_life[3]
                                    print stop_value
                                    time.sleep(1)#1s定时器
                                    Device_num=0
                                    # print "iiii"
                                    while Device_num<len(Ip_list):
                                        # print Device_num
                                        Timer_message_inNum12=Mysql.userWork.Get_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]),Num12_message_for_life[3])
                                        # return Timer_message_inNum12
                                        try:
                                            if Timer_message_inNum12 ==None:
                                                f=open("log.txt",'a')
                                                f.write("error_code:in12_have_no_data_udp\n")   
                                                traceback.print_exc(file=f)  
                                                f.flush()  
                                                f.close()
                                                print "in12_have_no_data_udp"
                                                timer_stop="true"#停止定时器
                                                # pass
                                            else:
                                                if str(Timer_message_inNum12[4])==str(Timer_message_inNum12[5]):#请求值是否等于返回值
                                                    if len(Ip_list)==1:
                                                        Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]))
                                                        Device_num=int(Device_num)+1 
                                                        # return_data["success"]=1
                                                        # return_more_data["success"]=1
                                                        timer_stop="true"#停止定时器
                                                        print "request == return,Ip_list=1"
                                                    else:
                                                        Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)])) 
                                                        Ip_list.remove(Ip_list[Device_num])
                                                        Port_list.remove(Port_list[Device_num])
                                                        First_type_list.remove(First_type_list[Device_num])
                                                        Second_type_list.remove(Second_type_list[Device_num])
                                                        Product_num_list.remove(Product_num_list[Device_num])
                                                        print Ip_list,Port_list,First_type_list,Second_type_list,Product_num_list

                                                else:
                                                    if stop_value==0:#生存值是否为0
                                                        if len(Ip_list)==1:
                                                            # return_more_data["error_intr"]="_"+return_more_data["error_intr"]+"_product_num"+"_"+str(Product_num_list[Device_num])+"_send failed"+" and life=0"
                                                            Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]))
                                                            Ip_list.remove(Ip_list[Device_num])
                                                            Port_list.remove(Port_list[Device_num])
                                                            First_type_list.remove(First_type_list[Device_num])
                                                            Second_type_list.remove(Second_type_list[Device_num])
                                                            Product_num_list.remove(Product_num_list[Device_num])
                                                            print Ip_list,Port_list,First_type_list,Second_type_list,Product_num_list
                                                            # Device_num=int(Device_num)+1 
                                                            f=open("log.txt",'a')
                                                            f.write("error_code:109_udp_third_life==0,delete,Ip_list=1\n")   
                                                            traceback.print_exc(file=f)  
                                                            f.flush()  
                                                            f.close() 
                                                            error_msg = '''error_code:109;'''
                                                            print error_msg
                                                            # socket.sendto(error_msg, addr)
                                                            timer_stop="true"#停止定时器
                                                            print "life==0,delete,Ip_list=1"
                                                        else:
                                                            # return_more_data["error_intr"]="_"+return_more_data["error_intr"]+"_product_num"+"_"+str(Product_num_list[Device_num])+"_send failed "
                                                            Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]))
                                                            Ip_list.remove(Ip_list[Device_num])
                                                            Port_list.remove(Port_list[Device_num])
                                                            First_type_list.remove(First_type_list[Device_num])
                                                            Second_type_list.remove(Second_type_list[Device_num])
                                                            Product_num_list.remove(Product_num_list[Device_num])
                                                            print Ip_list,Port_list,First_type_list,Second_type_list,Product_num_list             

                                                    else:
                                                        if stop_value%2==1:
                                                            Device_num=int(Device_num)+1
                                                            pass 
                                                        else:
                                                            Num12_message_for_request=Mysql.macWork.Product_isExist_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]))
                                                            if Num12_message_for_request==None:
                                                                f=open("log.txt",'a')
                                                                f.write("error_code:in12_request_have_no_data_udp\n")   
                                                                traceback.print_exc(file=f)  
                                                                f.flush()  
                                                                f.close()
                                                                timer_stop="true"#停止定时器
                                                            else: 
                                                                if Num12_message_for_request[4]== Request:#判断当前请求值是否等于数据库的请求值                                   
                                                                    socket.sendto(Order_send,(Ip_list[int(Device_num)],Port_list[int(Device_num)]))
                                                                    # print  Ip_list[int(Device_num)],Port_list[int(Device_num)]
                                                                    Device_num=int(Device_num)+1  
                                                                    # return Device_num 
                                                                    print "send_again"#"重新发送刚刚的指令"
                                                                else:
                                                                    if len(Ip_list)==1:
                                                                        Device_num=int(Device_num)+1 
                                                                        timer_stop="true"#停止定时器,因为有新的命令
                                                                        print "there have new order,Ip_list=1"
                                                                    else:
                                                                        # print Device_num
                                                                        Device_num=int(Device_num)+1
                                                                        if Device_num==len(Ip_list):
                                                                            timer_stop="true"#停止定时器,因为有新的命令
                                                                            print "there have new order,Ip_list>1" 
                                        except:
                                            f=open("log.txt",'a')
                                            f.write("error_code:222_udp_third\n") 
                                            traceback.print_exc(file=f)  
                                            f.flush()  
                                            f.close() 
                                            error_msg = '''error_code:222_mac;'''
                                            print error_msg                     
                        except:
                            f=open("log.txt",'a')
                            f.write("error_code:104_udp_third\n")   
                            traceback.print_exc(file=f)  
                            f.flush()  
                            f.close() 
                            error_msg = '''error_code:104_mac;'''
                            print error_msg
                            # socket.sendto(error_msg, addr)
            except:
                f=open("log.txt",'a')
                f.write("error_code:102_udp_third\n")   
                traceback.print_exc(file=f)  
                f.flush()  
                f.close() 
                error_msg = '''error_code:102_mac;'''
                print error_msg
            # socket.sendto(error_msg, addr)      
def startservice():#启动udp
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
if __name__ == "__main__":
    startservice()

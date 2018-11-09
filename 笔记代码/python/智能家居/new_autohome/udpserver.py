#-*-coding:utf-8-*-
import SocketServer
import socket
import Mysql.mysql
import threading
import traceback
import json
import time
import Mysql.macWork
import Mysql.userWork
import sys
import threading
reload(sys) 
sys.setdefaultencoding('utf8')
HOST = "172.22.225.5" #localhost
# HOST="120.27.95.22"
PORT = 11999

def cut_online_value():
    Mysql.macWork.Mac_is_not_in()
    print "udp_timer is ok"
    timer=threading.Timer(150,cut_online_value)
    timer.start()
timer=threading.Timer(150,cut_online_value)
timer.start()

class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        # return socket
        # socket.sendto(data,(HOST,10101))
        # if "request" in data:
        #     socket.sendto("success_connect", self.client_address)
        #     file=open("back.txt",'w')
        #     file.write("{} wrote:\n".format(self.client_address[0]))  
        #     file.write(data)
        #     file.flush()
        #     file.close()  
        handle_message(data, self.client_address, socket)    
        # print socket    

def handle_message(data, addr, socket):
    if " state " in data and " ip_message " in data and " port_message " in data:
        try:
            new_data=json.loads(data)
            state=new_data[" state "]
            ip_message=new_data[" ip_message "]
            port_message=new_data[" port_message "]
            print ip_message.strip(),port_message
            try:
                socket.sendto(state.strip(),(ip_message.strip(),port_message))
            except:
                f=open("log.txt",'a')  
                traceback.print_exc(file=f)  
                f.flush()  
                f.close() 
                error_msg = '''error_code:104444;'''
                socket.sendto(error_msg, addr)   
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close() 
            error_msg = '''error_code:102;'''
            socket.sendto(error_msg, addr)        
    if "first_type" in data and "second_type" in data and "device_num" in data and "current_status" in data and "request" in data :
        socket.sendto("success_connect", addr)
        try:
            socket.sendto(data, addr)
            # First_type=data.split("first_type")[1].split(",")[0].split(":")[1].split('"')[1]
            # Second_type=data.split("second_type")[1].split(",")[0].split(":")[1].split('"')[1]
            # Device_num=data.split("device_number")[1].split(",")[0].split(":")[1].split('"')[1]
            # Current_status=data.split("current_status")[1].split(",")[0].split(":")[1].split('"')[1]
            # Request=data.split("request")[1].split(":")[1].split("}")[0]
            new_data=json.loads(data)
            # print new_data
            First_type=new_data["first_type"]
            Second_type=new_data["second_type"]
            Device_nums=new_data["device_number"]
            Current_status=new_data["current_status"]
            Request=new_data["request"]
            print First_type,Second_type,Device_nums,Current_status,Request
            # socket.sendto(First_type,Second_type,Device_nums,Current_status,Request, addr)
            Num2_message=Mysql.macWork.Product_isExist_inNum2(First_type,Second_type,int(Device_nums))
            Num12_message=Mysql.macWork.Product_isExist_inNum12(First_type,Second_type,int(Device_nums))           
            print Num2_message,Num12_message
            if Num2_message==None:
                Mysql.macWork.Register_mac(First_type,Second_type,int(Device_nums),Current_status,addr[0],addr[1])
                print "register_mac"
                socket.sendto("register_mac",addr)
                # socket.sendto("register_device success", addr)
                # socket.sendto("register_mac success", addr)
            else:
                Mysql.macWork.Update_mac(First_type,Second_type,int(Device_nums),Current_status,addr[0],addr[1])
                print "Update_mac"
                socket.sendto("update_mac",addr)
                if Num12_message!=None:
                    # print "data is exist",int(Num12_message[5]),int(Request),int(Num12_message[5])==int(Request)
                    socket.sendto("data is exist",addr)
                    if Num12_message[5]==Request:
                        print "equal"
                        socket.sendto("request == request in form_12", addr) 
                        pass
                    else:
                        Mysql.macWork.Update_Return_value(First_type,Second_type,int(Device_nums),Request)
                        print "Update_Return_value"
                        socket.sendto("Update_Return_value success", addr)
                else:
                    # print "data is not exist",int(Num12_message[5]),int(Request),int(Num12_message[5])==int(Request)
                    socket.sendto("not in 12", addr) 
                    pass
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close() 
            error_msg = '''error_code:103;'''
            socket.sendto(error_msg, addr)
    # else:
    #     error_msg = '''error_code:501;'''#发送出错
    #     socket.sendto(error_msg, addr)
    if "first_type" in data and "second_type" in data and "product_num" in data and "state" in data :
        timer_stop="false"
        socket.sendto("success_connect2", addr)
        try:
            new_data=json.loads(data)
            first_type=new_data["first_type"]
            second_type=new_data["second_type"]
            product_num=new_data["product_num"]
            State=new_data["state"]
            # info=json.loads("state")["current_status"]
            info=State["current_status"]
            print data
            print first_type,second_type,product_num,State,info
            # gg=str(state)
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close() 
            error_msg = '''error_code:103;'''
            socket.sendto(error_msg, addr)
        try:
            Mysql.userWork.Insert_log_switch(first_type,second_type,product_num,info)
            Num11_message=Mysql.macWork.Product_isExist_inNum11(first_type,second_type,int(product_num))
            if Num11_message == None :#判断是否在表11
                f=open("log.txt",'a')  
                traceback.print_exc(file=f)  
                f.flush()  
                f.close() 
                error_msg = '''error_code:106;not in 11'''
                socket.sendto(error_msg, addr)
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
                    First_type_list.append(target_message[3])
                    Second_type_list.append(target_message[4])
                    Product_num_list.append(target_message[5])
                    print Num2_message,Num12_message
                    # return First_type_list,Second_type_list,Product_num_list
                    try:
                        if Num2_message==None:
                            f=open("log.txt",'a')  
                            traceback.print_exc(file=f)  
                            f.flush()  
                            f.close() 
                            error_msg = '''error_code:105;not in 2'''
                            socket.sendto(error_msg, addr)
                        else:
                            Ip_list.append(Num2_message[5])
                            Port_list.append(Num2_message[6])
                            # return Ip_list,Port_list
                    except:
                        f=open("log.txt",'a')  
                        traceback.print_exc(file=f)  
                        f.flush()  
                        f.close() 
                        error_msg = '''error_code:107;'''
                        socket.sendto(error_msg, addr)
                    print target_message[3],target_message[4],int(target_message[5])
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
                        traceback.print_exc(file=f)  
                        f.flush()  
                        f.close() 
                        error_msg = '''error_code:108;'''
                        socket.sendto(error_msg, addr)
                # return Ip_list[0],Port_list[0],First_type_list[0],Second_type_list[0],Product_num_list[0]
                print Ip_list,Port_list,First_type_list,Second_type_list,Product_num_list                                                       
                # Num8_message=Mysql.macWork.Product_inNum8(first_type,second_type)
                # Property=Num8_message[2]#获取property值
                # return len(str(Request))
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
                # b=json.loads(Property)
                # c=0
                # d=""
                # while c<len(b["property"]):
                #     if c==0:
                #         d=d+str(b[str(b["property"][c])][str(a[str(b["property"][c])])])
                #         c=c+1
                #     elif c>0 and c<len(b["property"]):
                #         d=d+"_"+str(b[str(b["property"][c])][str(a[str(b["property"][c])])])
                #         c=c+1
                Order_send=str(a)+"_"+Order_request#生成指令，格式如：00_00_00_00000001                    
                print a,Order_send
                if len(Ip_list)==0:
                    print "there have no data"
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
                            stop_value=Num12_message_for_life[3]
                            print stop_value
                            time.sleep(1)#1s定时器
                            Device_num=0
                            # print "iiii"
                            while Device_num<len(Ip_list):
                                # print Device_num
                                Timer_message_inNum12=Mysql.userWork.Get_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]),Num12_message_for_life[3])
                                # return Timer_message_inNum12
                                if Timer_message_inNum12[4]==Timer_message_inNum12[5]:#请求值是否等于返回值
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
                                        # if Device_num==len(Ip_list):
                                        #     return_data["success"]=1
                                        #     return_more_data["success"]=1
                                        #     timer_stop="true"#停止定时器
                                        #     print "request == return,Ip_list>1"
                                        # Device_num=Device_num+1
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
                                            traceback.print_exc(file=f)  
                                            f.flush()  
                                            f.close() 
                                            error_msg = '''error_code:109;'''
                                            socket.sendto(error_msg, addr)
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
                                            # if Device_num==len(Ip_list):
                                            #     return_data["error_code"]=103
                                            #     return_more_data["error_code"]=103
                                            #     return_more_data["error_intr"]="life=0,send the order failed or only send one of order"
                                            #     timer_stop="true"#停止定时器
                                            #     print "life==0,delete,Ip_list>1"
                                    else:
                                        if stop_value%2==1:
                                            Device_num=int(Device_num)+1
                                            pass 
                                        else:
                                            Num12_message_for_request=Mysql.macWork.Product_isExist_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]))
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
                        traceback.print_exc(file=f)  
                        f.flush()  
                        f.close() 
                        error_msg = '''error_code:104;'''
                        socket.sendto(error_msg, addr)
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close() 
            error_msg = '''error_code:102;'''
            socket.sendto(error_msg, addr)      
def startservice():#启动udp
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
if __name__ == "__main__":
    startservice()

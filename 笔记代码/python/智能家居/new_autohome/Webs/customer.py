#-*-coding:utf-8-*-
import web
import traceback
import json
import Mysql.mysql
import Mysql.register
import Mysql.userWork
import Mysql.macWork
import socket
import time
import threading
# Host="120.27.95.22"
Host="172.22.225.5"
Port= 11999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.bind(('',Port))
class test():
    def GET(self):
        data=web.input(
            callback='',
            )
        try:
            ip_message=data.ip_message        #二级类型
            port_message=data.port_message    #设备编号
            data_send=data.data_send        #状态  
            # new_data="{"+""" " """+"state"+""" " """+":"+""" " """+data_send+""" " """+","+""" " """+"ip_message"+""" " """+":"+""" " """+ip_message+""" " """+","+""" " """+"port_message"+""" " """+":"+port_message+"}"
            # Host=ip_message
            # Port=int(port_message)
            # return ip_message,port_message,data_send,Host,Port
        except:
            return "canshu cuowu"
        # try:
        #     state="00_00_11111111111"
        #     sock.sendto(state,(ip_message,int(port_message)))
        #     sock.sendto(new_data,(Host,int(Port)))
        #     return "success"
        #     # return sock.sendto(str(data_send),(ip_message,int(port_message)))
        # except:
        #     return "send message error"
class Control_mac:#设备控制
    def GET(self):
        data=web.input(
            callback='',
            is_manager='',
            )
        return_data ={ "success":"0", "error_code":"0"}
        return_more_data={"success":"0", "error_code":"0","error_intr":""}
        timer_stop="false"
        try:
            mycallback = data.callback
            is_manager = data.is_manager
            user_id=data.user_id          #用户id
            first_type=data.first_type    #一级类型
            second_type=data.second_type        #二级类型
            product_num=data.product_num    #设备编号
            state=data.state        #状态
            # info=json.loads(state)["current_status"]
            info=data.info
            # return info
        except:
            return_data["error_code"]=101
            return_more_data["error_code"]=101
            return_more_data["error_intr"]="enter data is wrong"
            if is_manager=='':
                return json.dumps(return_data)
            else:
                return json.dumps(return_more_data)

        try:
            Mysql.userWork.Insert_log(user_id,info)
            Request=Mysql.userWork.Get_last_value() #当前的请求值
            Num2_message=Mysql.macWork.Product_isExist_inNum2(first_type,second_type,int(product_num))#获取id，port，6,7
            # return Num2_message
            if Num2_message==None:
                return_data["error_code"]=105
                return_more_data["error_code"]=105
                return_more_data["error_intr"]="data not in form_2,so the send_order hava not ip and port"
                if is_manager=='':
                    return json.dumps(return_data)
                else:
                    return json.dumps(return_more_data)
            else:
                pass                
            Num12_message=Mysql.macWork.Product_isExist_inNum12(first_type,second_type,int(product_num))           
            # return Num12_message
            # Num8_message=Mysql.macWork.Product_inNum8(first_type,second_type)
            # Property=Num8_message[2]#获取property值
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
            a=json.loads(state)#字符串变成json
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
            Order_send=str(a["current_status"])+"_"+Order_request#生成指令，格式如：00_00_00_00000001
            new_data="{"+""" " """+"state"+""" " """+":"+""" " """+Order_send+""" " """+","+""" " """+"ip_message"+""" " """+":"+""" " """+Num2_message[5]+""" " """+","+""" " """+"port_message"+""" " """+":"+json.dumps(Num2_message[6])+"}"                  
            # return new_data
            try:
                if Num12_message != None :#存在的话更新
                    print "i am in update"
                    Mysql.userWork.Update_Num12(first_type,second_type,int(product_num),Request,state)
                else:
                    print "i am in Insert"
                    Mysql.userWork.Insert_Num12(first_type,second_type,int(product_num),Request,state)
            except:
                f=open("log.txt",'a')  
                traceback.print_exc(file=f)  
                f.flush()  
                f.close()
                return_data["error_code"] = 105
                return_more_data["error_code"]=105
                return_more_data["error_intr"]="Num12_message have wrong"
            sock.sendto(new_data,(Host,int(Port)))
            try:
                while timer_stop=="false":#方便后面暂停
                    Num12_message_for_life=Mysql.macWork.Product_isExist_inNum12(first_type,second_type,int(product_num))
                    stop_value=int(Num12_message_for_life[3])
                    print stop_value
                    time.sleep(1)#1s定时器
                    Timer_message_inNum12=Mysql.userWork.Get_message_inNum12(first_type,second_type,int(product_num),Num12_message_for_life[3])
                    if Timer_message_inNum12[4]==Timer_message_inNum12[5]:#请求值是否等于返回值
                        Mysql.userWork.Delete_message_inNum12(first_type,second_type,int(product_num))
                        return_data["success"]=1
                        return_more_data["success"]=1
                        timer_stop="true"#停止定时器
                        print "request == return"
                    else:
                        if stop_value==0:#生存值是否为0
                            Mysql.userWork.Delete_message_inNum12(first_type,second_type,int(product_num))
                            return_data["error_code"]=103
                            return_more_data["error_code"]=103
                            return_more_data["error_intr"]="_"+return_more_data["error_intr"]+"_product_num"+"_"+str(product_num)+"_send failed"+" and life=0"
                            timer_stop="true"#停止定时器
                            print "life==0,delete"
                        else:
                            if stop_value%2==1:
                                pass
                            else:
                                Num12_message_for_request=Mysql.macWork.Product_isExist_inNum12(first_type,second_type,int(product_num))
                                if Num12_message_for_request[4]== Request:#判断当前请求值是否等于数据库的请求值                                    
                                    sock.sendto(new_data,(Host,int(Port)))
                                    print "send_again" #"重新发送刚刚的指令"
                                else:
                                    timer_stop="true"#停止定时器,因为有新的命令
                                    print "there have new order"                                                      
            except:
                f=open("log.txt",'a')  
                traceback.print_exc(file=f)  
                f.flush()  
                f.close()
                return_data["error_code"] = 104
                return_more_data["error_code"]=104
                return_more_data["error_intr"]="timer have wrong"

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return_more_data["error_code"]=102
            return_more_data["error_intr"]=" code have wrong"

        finally:
            if mycallback =="?":
                if is_manager=='':
                    return mycallback+"("+json.dumps(return_data)+")"
                else:
                    return mycallback+"("+json.dumps(return_more_data)+")"                    
            elif mycallback =='':
                if is_manager=='':
                    return json.dumps(return_data)
                else:
                    return json.dumps(return_more_data)
            else:
                pass

class Control_switch:#设备开关
    def GET(self):
        data=web.input(
            callback='',
            is_manager='',
            )
        return_data ={ "success":"0", "error_code":"0"}
        return_more_data={"success":"0", "error_code":"0","error_intr":""}
        timer_stop="false"
        try:
            mycallback = data.callback
            is_manager = data.is_manager
            first_type=data.first_type    #开关一级类型
            second_type=data.second_type        #开关二级类型
            product_num=data.product_num    #开关编号
            state=data.state        #状态
            # return state
        except:
            return_data["error_code"]=101
            return_more_data["error_code"]=101
            return_more_data["error_intr"]="enter data is wrong"
            if is_manager=='':
                return json.dumps(return_data)
            else:
                return json.dumps(return_more_data)

        try:
            Num11_message=Mysql.macWork.Product_isExist_inNum11(first_type,second_type,product_num)
            if Num11_message == None :#判断是否在表11
                return_data["error_code"]=106
                return_more_data["error_code"]=106
                return_more_data["error_intr"]="data not in form_11"
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
                    # return First_type_list,Second_type_list,Product_num_list
                    try:
                        if Num2_message==None:
                            # return "cixian"
                            return_data["error_code"]=105
                            return_more_data["error_code"]=105
                            return_more_data["error_intr"]="data not in form_2,so the send_order hava not ip and port"
                            # if is_manage=='':
                            #     return json.dumps(return_data)
                            # else:
                            #     return json.dumps(return_more_data)
                        else:
                            Ip_list.append(Num2_message[5])
                            Port_list.append(Num2_message[6])
                            # return Ip_list,Port_list
                    except:
                        f=open("log.txt",'a')  
                        traceback.print_exc(file=f)  
                        f.flush()  
                        f.close()
                        return_data["error_code"] = 107
                        return_more_data["error_code"]=107
                        return_more_data["error_intr"]="check form_2 hava wrong"
                    try:
                        if Num12_message != None:
                            Mysql.userWork.Update_Num12(target_message[3],target_message[4],int(target_message[5]),Request,state)
                            print "i am in update"
                        else :
                            Mysql.userWork.Insert_Num12(target_message[3],target_message[4],int(target_message[5]),Request,state)
                            print "i am in Insert"
                    except:
                        f=open("log.txt",'a')  
                        traceback.print_exc(file=f)  
                        f.flush()  
                        f.close()
                        return_data["error_code"] = 108
                        return_more_data["error_code"]=108
                        return_more_data["error_intr"]="check form_12 hava wrong"
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
                a=json.loads(state)#字符串变成json
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
                Order_send=str(a["current_status"])+"_"+Order_request#生成指令，格式如：00_00_00_00000001                    
                # return a,Order_send
                # send_number=0
                # return Ip_list[int(send_number)],Port_list[int(send_number)]
                if len(Ip_list)==0:
                    pass
                else:
                    i=0
                    while i <len(Ip_list):
                        # return i
                        new_data="{"+""" " """+"state"+""" " """+":"+""" " """+Order_send+""" " """+","+""" " """+"ip_message"+""" " """+":"+""" " """+Ip_list[i]+""" " """+","+""" " """+"port_message"+""" " """+":"+json.dumps(Port_list[i])+"}"                 
                        # sock.sendto(Order_send,(Ip_list[i],Port_list[i]))
                        sock.sendto(new_data,(Host,int(Port)))
                        # send_number=int(send_number)+1
                        print Ip_list[i],Port_list[i]
                        i=i+1
                        # print send_number
                    try:    
                        while timer_stop=="false":#方便后面暂停
                            Num12_message_for_life=Mysql.macWork.Product_isExist_inNum12(First_type_list[0],Second_type_list[0],int(Product_num_list[0]))
                            stop_value=Num12_message_for_life[3]
                            print stop_value
                            time.sleep(1)#1s定时器
                            Device_num=0
                            # return Device_num<len(Ip_list),len(Ip_list)
                            while Device_num<len(Ip_list):
                                # print Device_num
                                Timer_message_inNum12=Mysql.userWork.Get_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]),Num12_message_for_life[3])
                                # return Timer_message_inNum12
                                # timer_stop="true"
                                if Timer_message_inNum12[4]==Timer_message_inNum12[5]:#请求值是否等于返回值
                                    if len(Ip_list)==1:
                                        Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]))
                                        Device_num=int(Device_num)+1 
                                        return_data["success"]=1
                                        return_more_data["success"]=1
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
                                            return_more_data["error_intr"]="_"+return_more_data["error_intr"]+"_product_num"+"_"+str(Product_num_list[Device_num])+"_send failed"+" and life=0"
                                            Mysql.userWork.Delete_message_inNum12(First_type_list[int(Device_num)],Second_type_list[int(Device_num)],int(Product_num_list[int(Device_num)]))
                                            Ip_list.remove(Ip_list[Device_num])
                                            Port_list.remove(Port_list[Device_num])
                                            First_type_list.remove(First_type_list[Device_num])
                                            Second_type_list.remove(Second_type_list[Device_num])
                                            Product_num_list.remove(Product_num_list[Device_num])
                                            print Ip_list,Port_list,First_type_list,Second_type_list,Product_num_list
                                            # Device_num=int(Device_num)+1 
                                            return_data["error_code"]=103
                                            return_more_data["error_code"]=103
                                            timer_stop="true"#停止定时器
                                            print "life==0,delete,Ip_list=1"
                                        else:
                                            return_more_data["error_intr"]="_"+return_more_data["error_intr"]+"_product_num"+"_"+str(Product_num_list[Device_num])+"_send failed "
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
                                                news_data="{"+""" " """+"state"+""" " """+":"+""" " """+Order_send+""" " """+","+""" " """+"ip_message"+""" " """+":"+""" " """+Ip_list[int(Device_num)]+""" " """+","+""" " """+"port_message"+""" " """+":"+json.dumps(Port_list[int(Device_num)])+"}"                 
                                                # sock.sendto(Order_send,(Ip_list[int(Device_num)],Port_list[int(Device_num)]))
                                                sock.sendto(news_data,(Host,int(Port)))
                                                print Ip_list[int(Device_num)],Port_list[int(Device_num)]
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
                        return_data["error_code"] = 104
                        return_more_data["error_code"]=104
                        return_more_data["error_intr"]="timer have wrong"

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return_more_data["error_code"]=102
            return_more_data["error_intr"]=" code have wrong"

        finally:
            if mycallback =="?":
                if is_manager=='':
                    return mycallback+"("+json.dumps(return_data)+")"
                else:
                    return mycallback+"("+json.dumps(return_more_data)+")"
            elif mycallback =='':
                if is_manager=='':
                    return json.dumps(return_data)
                else:
                    return json.dumps(return_more_data)

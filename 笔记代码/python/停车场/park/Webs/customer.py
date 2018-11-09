#-*-coding:utf-8-*-
import web
import traceback
import json
import Mysql.mysql
import Mysql.park
import Mysql.user
import Mysql.cost

class Register:#注册
    def GET(self):
        data=web.input(
                        nickname='',
                        head_photo='',
                       )
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            password=data.password        #密码
            username=data.username        #用户名字
            nickname=data.nickname        #用户昵称
            head_photo=data.head_photo    #用户头像

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            code = 201 if Mysql.user.Username_isExist(username) else 0 #用户名已注册
            if code == 201:
                return_data["error_code"]=201
                return json.dumps(return_data)

            else:
                try:
                    Mysql.user.Register(Password=password,Username=username,Nickname=nickname,Head_photo=head_photo)
                    user_message={
                                "Request":'Register',
                    }
                    return_data["message"]=user_message
                    return_data["success"]=1

                except:
                    f=open("log.txt",'a')
                    traceback.print_exc(file=f)
                    f.flush()
                    f.close()
                    return_data["error_code"] = 103

                finally:
                    return json.dumps(return_data)

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)


class Login:#登录
    def GET(self):
        data=web.input()

        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            password=data.password        #密码
            username=data.username        #用户名字
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.user.get_by_username(username)#用户名不存在
            user_message={
                    "user_id":every_message[4],
                    "nickname":every_message[2],
                    "Request":'Login'
                }
            if every_message == None:
                return_data["error_code"]=202

            else:
                if password == every_message[1]:
                    return_data["message"]=user_message
                    return_data["success"]=1
                else:
                    return_data["error_code"]=104

        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data) 

class Register_park:#登记车场信息
    def GET(self):
        data=web.input(
                        wifi_password='',
                       )
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_name=data.park_name        #车场名字
            addr=data.addr                  #车场地址
            gps_x=data.gps_x          #GPS_x
            gps_y=data.gps_y          #GPS_y
            price=data.price          #每小时价格
            wifi_name=data.wifi_name        #wifi名
            wifi_password=data.wifi_password#wifi密码

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            code = 401 if Mysql.park.Park_name_isExist(park_name) else 0 #车场名已注册
            if code == 401:
                return_data["error_code"]=401
                return json.dumps(return_data)

            else:
                try:
                    Mysql.park.Register_park(Park_name=park_name,Addr=addr,Gps_x=gps_x,Gps_y=gps_y,Price=price,Wifi_name=wifi_name,Wifi_password=wifi_password)
                    user_message={
                            "Request":'Register_park'
                    }
                    return_data["message"]=user_message
                    return_data["success"]=1

                except:
                    f=open("log.txt",'a')
                    traceback.print_exc(file=f)
                    f.flush()
                    f.close()
                    return_data["error_code"] = 103

                finally:
                    return json.dumps(return_data)

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

class Show_park:#显示所有车场信息
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        password=data.password
        try:
            if password=="yjssys":
                every_message=Mysql.park.Show_park()
                park_id_list=[]
                park_name_list=[]
                addr_list=[]
                gps_x_list=[]
                gps_y_list=[]
                price_list=[]
                wifi_name_list=[]
                wifi_password_list=[]
                door_come_list=[]
                door_out_list=[]
                for message in every_message:
                    park_id_list.append(message[0])
                    park_name_list.append(message[1])
                    addr_list.append(message[2])
                    gps_x_list.append(message[3])
                    gps_y_list.append(message[4])
                    price_list.append(message[5])
                    wifi_name_list.append(message[6])
                    wifi_password_list.append(message[7])
                    door_come_list.append(message[8])
                    door_out_list.append(message[9])
                park_message ={
                            "park_id":park_id_list,
                            "park_name":park_name_list,
                            "addr":addr_list,
                            "gps_x":gps_x_list,
                            "gps_y":gps_y_list,
                            "price":price_list,
                            "wifi_name":wifi_name_list,
                            "wifi_password":wifi_password_list,
                            "door_come":door_come_list,
                            "door_out":door_out_list,
                            "Request":'Show_park'
                }
                return_data["message"]=park_message    
                return_data["success"]=1
            else:
                return_data["error_code"]=901
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)
class Show_current_park:#显示当前车场信息
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)
        try:
            every_message=Mysql.park.get_by_park_id(park_id)
            park_message ={
                        "park_id":park_id,
                        "park_name":every_message[1],
                        "addr":every_message[2],
                        "gps_x":every_message[3],
                        "gps_y":every_message[4],
                        "price":every_message[5],
                        "wifi_name":every_message[6],
                        "wifi_password":every_message[7],
                        "door_come":every_message[8],
                        "door_out":every_message[9],
                        "Request":'Show_current_park'
            }
            return_data["message"]=park_message    
            return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)

class Update_park_stall:#更新车位信息
    def GET(self):
        data=web.input(
                        park_show='',
                       )
        return_data = { "success":0, "error_code":0,"message":{}}

        try:
            park_id=data.park_id        #车场id
            park_surplus=data.park_surplus    #空闲车位
            park_all=data.park_all          #总车位
            park_show=data.park_show        #介绍

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.park.get_by_park_id(Park_id=park_id)#车场id是否存在
            if every_message == None:
                return_data["error_code"]=402 #车场id不存在
            else:
                try:
                    Mysql.park.Update_park_stall(Park_id=park_id,Park_surplus=park_surplus,Park_all=park_all,Park_show=park_show)
                    park_message={
                            "Request":'Update_park_stall'
                    }
                    return_data["message"]=park_message
                    return_data["success"]=1

                except:
                    f=open("log.txt",'a')
                    traceback.print_exc(file=f)
                    f.flush()
                    f.close()
                    return_data["error_code"] = 103

                finally:
                    return json.dumps(return_data)

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

class Show_park_stall:#显示车场车位信息
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)
        try:
            every_message=Mysql.park.Show_park_stall(Park_id=park_id)
            park_message ={
                        "park_surplus":every_message[1],
                        "park_all":every_message[2],
                        "park_show":every_message[3],
                        "park_book":every_message[4],
                        "park_used":every_message[5],
                        "Request":'Show_park_stall'
            }
            return_data["message"]=park_message    
            return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)

class Update_indoor_map:#更新室内地图
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id
            length=data.length          #长
            width=data.width            #宽

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.park.get_by_park_id(Park_id=park_id)#车场id是否存在
            if every_message == None:
                return_data["error_code"]=402 #车场id不存在
            else:
                try:
                    Mysql.park.Update_indoor_map(Park_id=park_id,Length=length,Width=width)
                    park_message={
                            "Request":'Update_park_stall'
                    }
                    return_data["message"]=park_message
                    return_data["success"]=1

                except:
                    f=open("log.txt",'a')
                    traceback.print_exc(file=f)
                    f.flush()
                    f.close()
                    return_data["error_code"] = 103

                finally:
                    return json.dumps(return_data)

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

class Show_indoor_map:#显示车场车位大小
    def GET(self):
        data=web.input()
        park_id=data.park_id
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message=Mysql.park.Show_indoor_map(Park_id=park_id)
            park_message ={
                        "length":every_message[1],
                        "width":every_message[2],
                        "Request":'Show_indoor_map'
            }
            return_data["message"]=park_message    
            return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)

class Input_wall:#加墙数
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id
            start=data.start            #起点
            end=data.end            #终点

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.park.get_by_park_id(Park_id=park_id)#车场id是否存在
            if every_message == None:
                return_data["error_code"]=402 #车场id不存在
            else:
                try:
                    Mysql.park.Input_wall(Park_id=park_id,Start=start,End=end)
                    park_message={
                            "Request":'Input_wall'
                    }
                    return_data["message"]=park_message
                    return_data["success"]=1

                except:
                    f=open("log.txt",'a')
                    traceback.print_exc(file=f)
                    f.flush()
                    f.close()
                    return_data["error_code"] = 103

                finally:
                    return json.dumps(return_data)

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

class Show_indoor_map_wall:#显示车场墙的情况
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message=Mysql.park.Show_indoor_map_wall(Park_id=park_id)
            start_list=[]
            end_list=[]
            for message in every_message:
                start_list.append(message[1])
                end_list.append(message[2])
            park_message ={
                        "park_id":park_id,
                        "start":start_list,
                        "end":end_list,
                        "Request":'Show_indoor_map_wall'
            }
            return_data["message"]=park_message    
            return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)

class Input_position:#加位数
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id
            start=data.start            #起点
            end=data.end            #终点

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.park.get_by_park_id(Park_id=park_id)#车场id是否存在
            if every_message == None:
                return_data["error_code"]=402 #车场id不存在
            else:
                try:
                    Mysql.park.Input_position(Park_id=park_id,Start=start,End=end)
                    park_message={
                            "Request":'Input_position'
                    }
                    return_data["message"]=park_message
                    return_data["success"]=1

                except:
                    f=open("log.txt",'a')
                    traceback.print_exc(file=f)
                    f.flush()
                    f.close()
                    return_data["error_code"] = 103

                finally:
                    return json.dumps(return_data)

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

class Show_indoor_map_position:#显示车场位的情况
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            park_id=data.park_id        #车场id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message=Mysql.park.Show_indoor_map_position(Park_id=park_id)
            start_list=[]
            end_list=[]
            for message in every_message:
                start_list.append(message[1])
                end_list.append(message[2])
            park_message ={
                        "park_id":park_id,
                        "start":start_list,
                        "end":end_list,
                        "Request":'Show_indoor_map_position'
            }
            return_data["message"]=park_message    
            return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)
class Balance:#存余额
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            user_id=data.user_id
            user_balance=data.user_balance
            password=data.password

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.cost.get_by_user_id(User_id=user_id)#用户id不存在
            if every_message == None:
                return_data["error_code"]=203

            else:
                Mysql.cost.Balance(User_id=user_id,User_balance=user_balance,Password=password)
                park_message={
                            "Request":'Balance'
                }
                return_data["message"]=park_message
                return_data["success"]=1

        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data)

class Show_balance:#显示余额
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            user_id=data.user_id        #用户id
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message=Mysql.cost.Show_balance(User_id=user_id)
            balance_message={
                            "balance":every_message,
                            "Request":'Show_balance'
            }
            return_data["message"]=balance_message    
            return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)

class For_password:#密码输入
    def GET(self):
        data=web.input()

        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            password=data.password        #密码
            user_id=data.user_id        #用户id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.cost.get_by_user_id_from_balance(User_id=user_id)#用户id不存在
            if every_message == None:
                return_data["error_code"]=501 #用户id不在余额表

            else:
                if int(password) == every_message[2]:
                    park_message={
                            "Request":'For_password'
                    }
                    return_data["message"]=park_message
                    return_data["success"]=1
                else:
                    return_data["error_code"]=104

        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data)

class Start_indent:#下单
    def GET(self):
        data=web.input(
                    payment_status='no',
                    power=1,
            )
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            user_id=data.user_id        #用户id
            park_id=data.park_id        #车场id
            payment_status=data.payment_status    #支付状态为no
            power=data.power    #入门权限

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            user_message = Mysql.cost.get_by_user_id(User_id=user_id)#用户id不存在
            if user_message == None:
                return_data["error_code"]=203

            else:
                try:
                    park_message = Mysql.park.get_by_park_id(Park_id=park_id)#车场id不存在
                    if park_message == None:
                        return_data["error_code"]=402 

                    else:
                        payment_status_message=Mysql.cost.get_by_indent(park_id,user_id)
                        if 'no' in payment_status_message:
                            return_data["error_code"]=409  #不允许下单，历史存在未支付订单

                        else:                 
                            every_message=Mysql.cost.Start_indent(User_id=user_id,Park_id=park_id,Park_name=park_message[1],Payment_status=payment_status,Power=power)
                            indent_id_message={
                                                "indent_id":every_message,
                                                "Request":'Start_indent'
                            }
                            if every_message == None:
                                return_data["error_code"]=502 #订单id不存在
                            else:
                                return_data["message"]=indent_id_message
                                return_data["success"]=1

                except:
                    f=open("log.txt",'a')
                    traceback.print_exc(file=f)
                    f.flush()
                    f.close()
                    return_data["error_code"] = 103

                finally:
                    return json.dumps(return_data)

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

class Finish_indent:#结单
    def GET(self):
        data=web.input(
                    payment_status='yes',
                    power=2,
            )
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            indent_id=data.indent_id        #订单id
            user_id=data.user_id            #用户id
            park_id=data.park_id
            payment_status=data.payment_status    #支付状态为yes
            power=data.power
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            indent_message = Mysql.cost.get_by_indent_id(Indent_id=indent_id)#订单id不存在
            if indent_message == None or indent_message[4]==payment_status :
                return_data["error_code"]=503#订单不存在，或者已结单

            else:               
                Mysql.cost.Finish_indent(Indent_id=indent_id,User_id=user_id,Park_id=park_id,Payment_status=payment_status,Power=power)
                park_message={
                            "Request":'Finish_indent'
                }
                return_data["message"]=park_message
                return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)

class Show_indent:#显示客户所有订单信息
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            user_id=data.user_id            #用户id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)
        try:
            every_message=Mysql.cost.Show_indent(user_id)
            indent_id_list=[]
            park_id_list=[]
            park_name_list=[]
            payment_status_list=[]
            cost_price_list=[]
            payment_time_list=[]
            start_time_list=[]
            power_list=[]
            for message in every_message:
                indent_id_list.append(message[0])
                park_id_list.append(message[2])
                park_name_list.append(message[3])
                payment_status_list.append(message[4])
                cost_price_list.append(message[9])
                payment_time_list.append(message[5])
                start_time_list.append(message[6])
                power_list.append(message[8])
            cost_message ={
                        "user_id":user_id,
                        "indent_id":indent_id_list,
                        "park_id":park_id_list,
                        "park_name":park_name_list,
                        "payment_status":payment_status_list,
                        "cost_price":cost_price_list,
                        "payment_time":payment_time_list,
                        "start_time_":start_time_list,
                        "power":power_list,
                        "Request":'Show_indent'
            }
            return_data["message"]=cost_message    
            return_data["success"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 103
            return json.dumps(return_data)

        finally:
            return json.dumps(return_data)


class Come_to_park:#进停车场
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            indent_id=data.indent_id      #订单id
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.cost.get_by_indent_id(indent_id)#用户id和车场id不存在于订单中
            if every_message == None:
                return_data["error_code"]=502

            else:
                if every_message[4] =='no':
                    Mysql.park.Update_news_for_comer(every_message[2],every_message[1])
                    user_message={
                        "Request":'Come_to_park'
                    }
                    return_data["message"]=user_message
                    return_data["success"]=1
                else:
                    return_data["error_code"]=601  #不准进来
        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data) 

class Out_to_park:#离开停车场
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            indent_id=data.indent_id      #订单id
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.cost.get_by_indent_id(indent_id)#用户id和车场id不存在于订单中
            if every_message == None:
                return_data["error_code"]=502

            else:
                if every_message[4] =='yes':
                    Mysql.park.Update_news_for_outer(every_message[2],every_message[1])
                    user_message={
                        "Request":'Out_to_park'
                    }
                    return_data["message"]=user_message
                    return_data["success"]=1
                else:
                    return_data["error_code"]=601  #不准进来
        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data)

class Car_in_park:#车辆过了入口
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            indent_id=data.indent_id      #订单id
            current_status=data.current_status  #车是否真的过了入口门
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.cost.get_by_indent_id(indent_id)#用户id和车场id不存在于订单中
            if every_message == None:
                return_data["error_code"]=502

            else:
                if current_status=="yes":
                    Mysql.cost.Update_news_for_comer_car(indent_id)
                    user_message={
                        "Request":'Car_in_park'
                    }
                    return_data["message"]=user_message
                    return_data["success"]=1
                else:
                    return_data["error_code"]=602  #没有进来或者出错
        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data)

class Car_out_park:#车辆过了出口
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            indent_id=data.indent_id      #订单id
            current_status=data.current_status  #车是否真的过了出口门
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.cost.get_by_indent_id(indent_id)#用户id和车场id不存在于订单中
            if every_message == None:
                return_data["error_code"]=502

            else:
                if current_status=="yes":
                    Mysql.cost.Update_news_for_outer_car(indent_id)
                    user_message={
                        "Request":'Car_out_park'
                    }
                    return_data["message"]=user_message
                    return_data["success"]=1
                else:
                    return_data["error_code"]=603  #没有离开或者出错
        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data)
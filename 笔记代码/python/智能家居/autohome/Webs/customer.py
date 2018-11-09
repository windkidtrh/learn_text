#-*-coding:utf-8-*-
import web
import traceback
import json
import Mysql.mysql
import Mysql.register
import Mysql.userWork
import Mysql.macWork
import socket
Host=""
Port=""
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class Register:
    def GET(self):
        data=web.input(
            username='',
            callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0"}
        try:
            mycallback = data.callback
            id_name=data.id_name          #账号
            password=data.password        #密码
            username=data.username        #用户名字

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            if Mysql.register.get_by_id_name(id_name) == None :
                Mysql.register.Register(Password=password,Username=username,Id_name=id_name)
                return_data["success"]=1

            else :
                return_data["error_code"]=1

        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102

        finally:
            if mycallback =="?":
               return mycallback+"("+json.dumps(return_data)+")"
            else:
               return json.dumps(return_data)

class Login:#登录
    def GET(self):
        data=web.input(
            callback=''
            )

        return_data = { "success":0, "error_code":0}
        try:
            mycallback = data.callback
            password=data.password        #密码
            id_name=data.id_name        #用户账户
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.register.get_by_id_name(id_name)#用户账户不存在
            if every_message == None:
                return_data["error_code"]=202

            else:
                if password == every_message[2]:
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
            if mycallback =="?":
               return mycallback+"("+json.dumps(return_data)+")"
            else:
               return json.dumps(return_data)

class Handle_mac:#添加设备
    def GET(self):
        data=web.input(
            callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0"}
        try:
            mycallback = data.callback
            id_name=data.id_name          #账号
            mac_number=data.mac_number    #设备编号
            check_number=data.check_number        #设备注册码

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            if Mysql.register.get_by_id_name(id_name) == None :
                return_data["error_code"]=202

            else:
                every_message=Mysql.register.Check_number(check_number)
                if every_message==None:
                    return_data["error_code"]=203
                else:
                    # return every_message
                    if every_message[0]==mac_number:
                        mac_isWork='yes'
                        Mysql.userWork.Update_user(mac_number,mac_isWork,id_name)
                        if Mysql.userWork.Check_relation(mac_number,id_name)==None:
                            Mysql.userWork.Relation(mac_number,id_name)
                        else:
                            pass
                        return_data["success"]=1
                    else:
                        return_data["error_code"]=205
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102

        finally:
            if mycallback =="?":
               return mycallback+"("+json.dumps(return_data)+")"
            else:
               return json.dumps(return_data)

class Handle_action:#发送请求
    def GET(self):
        data=web.input(
            callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0"}
        try:
            mycallback = data.callback
            mac_number=data.mac_number    #设备编号
            action_id=data.action_id        #指令id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message=Mysql.macWork.Mac_number_isExist(mac_number)#设备编号是否存在
            if every_message == None :
                return_data["error_code"]=204
            else:
                action_message=Mysql.register.Show_current_action(action_id)
                if action_message == None:
                    return_data["error_code"]=205
                else:
                    Mysql.macWork.Update_user_answer(mac_number,action_message[1])
                    if every_message[1]==action_message[1]:
                        return_data["success"]=1
                    else:
                        Host=every_message[3]
                        Port=every_message[4]
                        error_msg = '''error_code:401;'''
                        sock.sendto(error_msg, (Host,Port))#状态不一致
                        return_data["error_code"]=401
        except:
            f=open("log.txt",'a')  
            traceback.print_exc(file=f)  
            f.flush()  
            f.close()
            return_data["error_code"] = 102

        finally:
            if mycallback =="?":
               return mycallback+"("+json.dumps(return_data)+")"
            else:
               return json.dumps(return_data)

class Return_mac:#返回用户能控制的mac
    def GET(self):
        data=web.input(
            callback=''
            )

        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            mycallback = data.callback
            id_name=data.id_name        #用户账户
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.userWork.Return_mac(id_name)#用户账户不存在
            mac_list=[]
            if every_message == None:
                return_data["error_code"]=301

            else:
                for message in every_message:  
                    mac_list.append({"mac_number":message[0],"current_status":Mysql.userWork.Return_mac_current_status(message)[0]})
                id_message={
                    "id_name":id_name,
                    "driver":mac_list,
                }
                return_data["message"]=id_message
                return_data["success"]=1
        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            if mycallback =="?":
               return mycallback+"("+json.dumps(return_data)+")"
            else:
               return json.dumps(return_data)

class Return_base:#返回指定设备的信息
    def GET(self):
        data=web.input(
            callback=''
            )

        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            mycallback = data.callback
            id_name=data.id_name        #用户账户
            mac_number=data.mac_number  #设备编号
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.userWork.Check_relation(mac_number,id_name)#关系是否存在？
            if every_message == None:
                return_data["error_code"]=302

            else:
                base_message=Mysql.macWork.Mac_number_isExist(mac_number)
                id_message={
                    "mac_number":base_message[0],
                    "current_status":base_message[1],
                    "action_name":base_message[2],
                    "mac_ip":base_message[3],
                    "mac_port":base_message[4],
                }
                return_data["message"]=id_message
                return_data["success"]=1
        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            if mycallback =="?":
               return mycallback+"("+json.dumps(return_data)+")"
            else:
               return json.dumps(return_data)
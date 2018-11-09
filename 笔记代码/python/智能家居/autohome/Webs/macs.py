#-*-coding:utf-8-*-
import web
import traceback
import json
import Mysql.mysql
import Mysql.register
import socket
import random

class Check_number:#检验码
    def GET(self):
        data=web.input()

        return_data = { "success":0, "error_code":0}
        try:
            mac_number=data.mac_number
            check_number=data.check_number
        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.register.Check_number(check_number)#判断是否存在
            if every_message == None:
                return_data["error_code"]=302#检验码不存在

            else:
                if int(id_number) == every_message[0]:
                    Mysql.register.Delete_number(check_number)
                    return_data["success"]=1
                else:
                    return_data["error_code"]=105#编号不对

        except:
            f=open("log.txt",'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            return_data["error_code"] = 103

        finally:
            return json.dumps(return_data)

class Input_number:#加入随机检验码
    def GET(self):

        data=web.input()
        result_get=''
        i=0
        return_data = { "success":0, "error_code":0}
        while i<100:
            list_radom="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
            slice_r=random.sample(list_radom,5)#从list中随机获取5个元素，作为一个片断返回
            result_get=result_get.join(slice_r)
            try:
                every_message = Mysql.register.Check_number(result_get)#判断是否存在
                if every_message == None:
                    Mysql.register.Input_number(result_get)
                    result_get=''
                    i=i+1
                else:
                    pass
            except:
                f=open("log.txt",'a')
                traceback.print_exc(file=f)
                f.flush()
                f.close()
                return_data["error_code"] = 103
        if i==100:
            return_data["success"]=1            
            return json.dumps(return_data)
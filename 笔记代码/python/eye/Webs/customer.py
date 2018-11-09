#-*-coding:utf-8-*-
import web
import traceback
import json
import Mysql.mysql
import Mysql.record
import Mysql.register

# TIMEFORMAT= "%Y-%m-%d %H:%M:%S"
# import time

class Register:#注册
    def GET(self):
        data=web.input(
                        nickname='',
                        head_photo=''
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
            code = 201 if Mysql.register.Username_isExist(username) else 0 #用户名已注册
            if code == 201:
                return_data["error_code"]=201
                return json.dumps(return_data)

            else:
                try:
                    Mysql.register.Register(Password=password,Username=username,Nickname=nickname,Head_photo=head_photo)
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
            every_message = Mysql.register.get_by_username(username)#用户名不存在
            if every_message == None:
                return_data["error_code"]=202

            else:
                if password == every_message[2]:
                    user_message={
                                "user_id":every_message[0],
                                "Request":'Login',
                    }
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

class Record_eye:#存视力记录
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            record_id=data.record_id
            left_eye=data.left_eye
            right_eye=data.right_eye

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.record.get_by_record_id(Record_id=record_id)#id不存在
            if every_message == None:
                return_data["error_code"]=203

            else:
                Mysql.record.Record_eye(Record_id=record_id,Left_eye=left_eye,Right_eye=right_eye)
                user_message={
                            "Request":'Record_eye',
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

class Get_record_eye:#获取视力记录
    def GET(self):
        data=web.input()

        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            record_id=data.record_id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            id_message = Mysql.record.get_by_record_id(Record_id=record_id)#id不存在
            if id_message == None:
                return_data["error_code"]=203

            else:
                every_message = Mysql.record.Get_record_eye(Record_id=record_id)
                user_message ={
                               "time":every_message[0],
                               "left_eye":every_message[1],
                               "right_eye":every_message[2],
                               "Request":'Get_record_eye'
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

class Record_health:#存健康记录
    def GET(self):
        data=web.input()
        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            record_id=data.record_id
            health_status=data.health_status

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message = Mysql.record.get_by_record_id(Record_id=record_id)#id不存在注册表
            if every_message == None:
                return_data["error_code"]=203

            else:
                Mysql.record.Record_health(Record_id=record_id,Health_status=health_status)
                user_message={
                            "Request":'Record_health',
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

class Get_record_health:#获取健康记录
    def GET(self):
        data=web.input()

        return_data = { "success":0, "error_code":0,"message":{}}
        try:
            record_id=data.record_id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            id_message = Mysql.record.get_by_record_id(Record_id=record_id)#id不存在
            if id_message == None:
                return_data["error_code"]=203

            else:
                every_message = Mysql.record.Get_record_health(Record_id=record_id)
                health_list=[]
                time_list=[]
                for message in every_message:
                    time_list.append(message[0])
                    health_list.append(message[1])
                user_message ={
                               "time":time_list,
                               "health_status":health_list,
                               "Request":'Get_record_health'
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
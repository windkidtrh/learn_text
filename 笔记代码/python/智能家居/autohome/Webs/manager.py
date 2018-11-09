#-*-coding:utf-8-*-
import web
import traceback
import json
import Mysql.mysql
import Mysql.register
import Mysql.userWork
import Mysql.macWork
import socket

class Input_action:
    def GET(self):
        data=web.input(
            action_show='',
            callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0"}
        try:
            mycallback = data.callback
            action_name=data.action_name          #指令
            action_show=data.action_show        #指令描述

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            Mysql.register.Input_action(action_name,action_show)
            return_data["success"]=1

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

class Update_action:
    def GET(self):
        data=web.input(
            action_show='',
            action_name='',
            callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0"}
        try:
            mycallback = data.callback
            action_id=data.action_id       #指令id
            action_name=data.action_name          #指令
            action_show=data.action_show        #指令描述

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            Mysql.register.Update_action(action_id,action_name,action_show)
            return_data["success"]=1

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

class Show_action:
    def GET(self):
        data=web.input(
            callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0","message":{}}
        try:
            mycallback = data.callback

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            every_message=Mysql.register.Show_action()
            action_id_list=[]
            action_name_list=[]
            action_show_list=[]
            for message in every_message:
                action_id_list.append(message[0])
                action_name_list.append(message[1])
                action_show_list.append(message[2])
            action_message ={
                        "action_id":action_id_list,
                        "action_name":action_name_list,
                        "action_show":action_show_list,
            }
            return_data["message"]=action_message 
            return_data["success"]=1

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

class Show_current_action:
    def GET(self):
        data=web.input(
        	callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0"}
        try:
            mycallback = data.callback
            action_id=data.action_id          #指令id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            action_message=Mysql.register.Show_current_action(action_id)
            if action_message == None:
                return_data["error_code"]=205
            else:
                every_message=Mysql.register.Show_current_action(action_id)
                result_message ={
                     "action_id":action_id,
                     "action_name":every_message[1],
                     "action_show":every_message[2],
                }
                return_data["message"]=result_message 
                return_data["success"]=1

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

class Delete_action:
    def GET(self):
        data=web.input(
            callback='',
            )
        
        return_data ={ "success":"0", "error_code":"0"}
        try:
            mycallback = data.callback
            action_id=data.action_id          #指令id

        except:
            return_data["error_code"]=101
            return json.dumps(return_data)

        try:
            Mysql.register.Delete_action(action_id)
            return_data["success"]=1

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
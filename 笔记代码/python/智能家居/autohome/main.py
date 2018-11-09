#-*-coding:utf-8-*-
import web
#import time
#import datetime
import Mysql.mysql
import Mysql.register
import Webs.customer
import Webs.macs
import Mysql.userWork
import Mysql.macWork
import SocketServer
import socket
import threading
import traceback
import Webs.manager
import SimpleHTTPServer
import udpserver
import sys
sys.path.append("..")

urls=(
      '/Register','Webs.customer.Register',
      '/Login','Webs.customer.Login',
      '/Check_number','Webs.macs.Check_number',
      '/Input_number','Webs.macs.Input_number',
      '/Handle_mac','Webs.customer.Handle_mac',
      '/Handle_action','Webs.customer.Handle_action',
      '/Return_mac','Webs.customer.Return_mac',
      '/Return_base','Webs.customer.Return_base',
      '/Input_action','Webs.manager.Input_action',
      '/Update_action','Webs.manager.Update_action',
      '/Show_action','Webs.manager.Show_action',
      '/Show_current_action','Webs.manager.Show_current_action',
      '/Delete_action','Webs.manager.Delete_action',
)
  
if __name__ == "__main__":
  try:
    threading.Thread(target=udpserver.startservice).start()   
  except:
    print "fail to create threads"
    f=open("log.txt",'a')  
    traceback.print_exc(file=f)  
    f.flush()  
    f.close()
  app=web.application(urls,globals())
  app.run()
 
#-*-coding:utf-8-*-
import web
#import time
#import datetime
import Mysql.mysql
import Mysql.register
import Mysql.record
import Webs.customer
#import threading
#import traceback

urls=(
      '/everyone/Register','Webs.customer.Register',
      '/everyone/Login','Webs.customer.Login',
      '/everyone/Record_eye','Webs.customer.Record_eye',
      '/everyone/Get_record_eye','Webs.customer.Get_record_eye',
      '/everyone/Record_health','Webs.customer.Record_health',
      '/everyone/Get_record_health','Webs.customer.Get_record_health',      
)
    
if __name__== "__main__":
    app=web.application(urls,globals())
    app.run()
 
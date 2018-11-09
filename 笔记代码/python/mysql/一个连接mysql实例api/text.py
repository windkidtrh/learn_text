#-*-coding:utf-8-*-
import web
#import time
#import datetime
# import Mysql.mysql
# import Mysql.register
import Webs.customer
#import threading
#import traceback

urls=(
      '/Register','Webs.customer.Register',
      # '/everyone/Login','Webs.customer.Login',
      # '/everyone/Check_number','Webs.customer.Check_number',
      # '/everyone/Input_number','Webs.customer.Input_number',

)
    
if __name__== "__main__":
    app=web.application(urls,globals())
    app.run()
 
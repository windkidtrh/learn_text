#-*-coding:utf-8-*-
import web
#import time
#import datetime
import Mysql.mysql
import Mysql.park
import Mysql.user
import Webs.customer
#import threading
#import traceback

urls=(
      '/everyone/Register','Webs.customer.Register',
      '/everyone/Login','Webs.customer.Login',
      '/everyone/Register_park','Webs.customer.Register_park',
      '/everyone/Show_park','Webs.customer.Show_park',
      '/everyone/Show_current_park','Webs.customer.Show_current_park',      
      '/everyone/Update_park_stall','Webs.customer.Update_park_stall',
      '/everyone/Show_park_stall','Webs.customer.Show_park_stall',
      '/everyone/Update_indoor_map','Webs.customer.Update_indoor_map',
      '/everyone/Show_indoor_map','Webs.customer.Show_indoor_map',
      '/everyone/Input_wall','Webs.customer.Input_wall',
      '/everyone/Show_indoor_map_wall','Webs.customer.Show_indoor_map_wall',
      '/everyone/Input_position','Webs.customer.Input_position',
      '/everyone/Show_indoor_map_position','Webs.customer.Show_indoor_map_position',
      '/everyone/Balance','Webs.customer.Balance',
      '/everyone/Show_balance','Webs.customer.Show_balance',      
      '/everyone/For_password','Webs.customer.For_password',
      '/everyone/Start_indent','Webs.customer.Start_indent',
      '/everyone/Finish_indent','Webs.customer.Finish_indent',
      '/everyone/Show_indent','Webs.customer.Show_indent',
      '/everyone/Come_to_park','Webs.customer.Come_to_park',
      '/everyone/Out_to_park','Webs.customer.Out_to_park', 
      '/everyone/Car_in_park','Webs.customer.Car_in_park',
      '/everyone/Car_out_park','Webs.customer.Car_out_park',
)
    
if __name__== "__main__":
    app=web.application(urls,globals())
    app.run()
 
#-*-coding:utf-8-*-
import SocketServer
import Mysql.mysql
import threading
import traceback
import json
import time
import Mysql.macWork
import Mysql.userWork
import sys
import threading
reload(sys) 
sys.setdefaultencoding('utf8')

# def cut_online_value():
while True:
	# time.sleep(1)
    Mysql.userWork.test_show()
    time.sleep(2)
#     timer=threading.Timer(0.5,cut_online_value)
#     timer.start()
# timer=threading.Timer(0.5,cut_online_value)
# timer.start()

if __name__ == "__main__":
    startservice()

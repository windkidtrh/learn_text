# -*- coding: cp936 -*-
import json
import time
import threading
b="haha"
timer=threading.Timer(3,c)
timer.start()
def c():
    print b
    i=0
    timer=threading.Timer(3,c)
    timer.start()
    if i==0:
      timer.cancel()
      print "end"


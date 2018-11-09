#!/usr/bin/env python
import os
import sys
import threading
# import Mysql.udpserver
if __name__ == "__main__":
    # threading.Thread(target=udpserver.startservice).start()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
    # try:
    #     threading.Thread(target=udpserver.startservice).start()   
    # except:
    #     logging_set.log_message.logging.warning('fail to create threads')
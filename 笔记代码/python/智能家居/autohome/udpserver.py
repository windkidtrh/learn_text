#-*-coding:utf-8-*-
import SocketServer
import Mysql.mysql
import threading
import traceback
import Mysql.register
import Mysql.macWork
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
HOST = "127.0.0.1" #localhost
PORT = 55123


# mutex = threading.Lock() #create a lock for handling database
                  
class MyUDPHandler(SocketServer.BaseRequestHandler):
  
    def handle(self):
        data = self.request[0].strip()#设备发来设备状态，设备编号
        socket = self.request[1]
        if "connection" in data:
            socket.sendto("success", self.client_address)
            file=open("back.txt",'w')
            file.write("{} wrote:\n".format(self.client_address[0]))  
            file.write(data)
            file.flush()
            file.close() 
        handle_message(data, self.client_address, socket)        
        print "{} wrote:".format(self.client_address[0])
        print data

def handle_message(data, addr, socket):
    if "connection" in data:
        if "mac_number" in data and "current_status" in data:
            try:
                Mac_number  = data.split("mac_number:")[1].split(";")[0]
                Current_status = data.split("current_status:")[1].split(";")[0]
                every_message=Mysql.macWork.Mac_number_isExist(Mac_number)
                if every_message==None:
                    Mysql.macWork.Register_mac(Mac_number,Current_status,addr[0],addr[1])
                    # right_msg = '''success:1;'''
                    # socket.sendto(right_msg, addr)
                    #加一个返回？
                else:
                    Mysql.macWork.Update_mac(Mac_number,Current_status)
                    if every_message[2]==Current_status:
                        pass
                        # right_msg = '''success:1;'''
                        # socket.sendto(right_msg, addr)
                    else:
                        error_msg = '''error_code:401;'''
                        socket.sendto(error_msg, addr)#状态不一致
            except:
                f=open("log.txt",'a')  
                traceback.print_exc(file=f)  
                f.flush()  
                f.close() 
                error_msg = '''error_code:103;'''
                socket.sendto(error_msg, addr)
        else:
            error_msg = '''error_code:501;'''#发送出错
            socket.sendto(error_msg, addr)

def startservice():#启动udp
    server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()

if __name__ == "__main__":
    startservice()

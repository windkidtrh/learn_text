#coding:utf-8
import socket
import datetime
 """
定义基本的信息
"""
HOST = "127.0.0.1"            #主机
PORT = 23151         #端口
ADD = (HOST, PORT)
BUFFERSIZE = 1024    #缓冲区大小
 """
建立socket，绑定地址和开始监听
"""
TcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #创建socket
TcpSerSock.bind(ADD)       #绑定地址和端口
TcpSerSock.listen(10)      #开始监听，监听数目同时间不超过10个
 """
socekt建好后，开始进行连接和数据的传输
"""
print "服务器等待连接......"
TcpCliSock, addr = TcpSerSock.accept()  #开始连接
while True:
    date = TcpCliSock.recv(BUFFERSIZE)   #接受数据
    if date:     #如果接受到了数据
        curTime = datetime.datetime.now()  #获得当前时间 格式是：datetime.datetime(2012, 3, 13, 1, 29, 51, 872000)
        curTime = curTime.strftime('%Y-%m-%m %H:%M:%S')     #转换格式
        print "%s  %s" % (addr, curTime) 
        print date
        #发数据
        sendDate = raw_input("input:")
        TcpCliSock.send('%s' % (sendDate))   #发数据   
        if date == '88':
            break  
     
"""
连接完毕，关闭套接字
"""
print "server close"
TcpCliSock.close()
TcpSerSock.close()

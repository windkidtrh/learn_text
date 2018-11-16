#!/usr/bin/env python
#coding:utf -8
from socket import *

myhost = 'localhost'
myport= 8080
sockobj = socket(AF_INET,SOCK_STREAM)#前面表示通过（TCP/IP - IPv4），后者代表数据流，还有一些可以网上找
print sockobj
sockobj.bind((myhost,myport))
sockobj.listen(128)#128代表客户端链接数
while True:
	connection, address = sockobj.accept()#
	print "connect by",address
	while  True:
		data = connection.recv(1024)#一次接受1024字节
		if not data:
			break
		connection.send('echo' + data)
	connection.close()

'''
server2.py
from SocketServer import TCPServer,BaseRequestHandler
import traceback
class MyBaseRequestHandler(BaseRequestHandler):#继承BaseRequestHandler
	def handle(self):
		print self
		while True:
			try:
				data = self.request.recv(1024).strip()#一次性读取1024字节，并去除两端的空白字符（包括空格,TAB,\r,\n）
				print "receive from (%r):%r"%(self.client_address,data)

				self.request.sendall(data.upper())
			except:
				traceback.print_exc()
				break
if __name__ == '__main__':
	host = "127.0.0.1"
	port = 8080
	addr = (host,port)
	server = TCPServer(addr,MyBaseRequestHandler)
	server.server_forever() 


server3.py
from SocketServer import ThreadingTCPServer,StreamRequestHandler
import traceback
class MyStreamRequestHandler(StreamRequestHandler):
	def handle(self):
		while True:
			try:
				data = self.rfile.readline().strip()
				print "receive from (%r):%r"%(self.client_address,data)

				self.wfile.write(data.upper())
			except:
				traceback.print_exc()
				break
if __name__ == '__main__':
	host = "127.0.0.1"
	port = 8080
	addr = (host,port)
	#ThreadingTCPServer从ThreadingMixin和TCPServer继承
	#class ThreadingTCPServer(ThreadingMixin,TCPServer)：pass
	server = ThreadingTCPServer(addr,MyStreamRequestHandler)
	server.server_forever()

'''
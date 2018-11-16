#!/usr/bin/env python
#coding:utf -8
a = {}.get('page',1)
print a
# from socket import *

# myhost = 'localhost'
# myport= 8080
# sockobj = socket(AF_INET,SOCK_STREAM)#前面表示通过（TCP/IP - IPv4），后者代表数据流，还有一些可以网上找
# print sockobj
# sockobj.bind((myhost,myport))
# sockobj.listen(128)#128代表客户端链接数
# while True:
# 	connection, address = sockobj.accept()#
# 	print "connect by",address
# 	while  True:
# 		data = connection.recv(1024)#一次接受1024字节
# 		if not data:
# 			break
# 		connection.send('echo' + data)
# 	connection.close()
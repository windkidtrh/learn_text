from socket import *  
HOST = '127.0.0.1'
PORT = 14444
BUFSIZ = 128  
ADDR = (HOST, PORT)  
  
#�����ͻ���UDP�׽���  
udpClient = socket(AF_INET, SOCK_DGRAM)  
  
while True:  
    data = raw_input('>')  
    if not data:  
        break  
#��������˷�������  
    udpClient.sendto(data,ADDR)  
#�������Է������˵�����  
    data, ADDR = udpClient.recvfrom(BUFSIZ)  
    print data  
    if not data:  
        break  
  
udpClient.close()

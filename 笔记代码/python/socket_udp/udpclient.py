import socket
import sys
import json
HOST, PORT = "127.0.0.1", 12349
data1 = {"first_type":"AABC","second_type":"AASX","device_number":2,"current_status":{"horizontal":1,"vertical":1,"run":1},"request":0}
#data=json.dumps(data1)
data="haha"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(str(data1) + "\n", (HOST, PORT))
#received = sock.recvfrom(1024)
print "Sent:     {}".format(data1)
#print "Received: {}".format(received)

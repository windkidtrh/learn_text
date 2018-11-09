import socket
import SocketServer
import json
class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data1 = self.request[0].strip()
        data=json.loads(data1)
        socket = self.request[1]
        #print "{} wrote:".format(self.client_address[0])
        #print data["first_type"]
        print data1
        print data
if __name__ == "__main__":
        HOST, PORT = "127.0.0.1", 12349
        server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
        server.serve_forever()

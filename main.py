import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 8080)
sock.bind(addr)

sock.listen(1)

while True:
    connection, client = sock.accept()

    data = connection.recv(16)
    if data:
        connection.sendall(data)
        print data
    else:
        print 'no data'
        connection.close()
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

b_addr = raw_input("Where would you like to bind to: ")
b_port = raw_input("What port would you like to listen to: ")

addr = (b_addr, int(b_port))
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
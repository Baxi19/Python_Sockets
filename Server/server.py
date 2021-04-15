import socket
import sys

# it should be in .env
ip = 'localhost'
port = 10000
connections = 1

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (ip, port)
print('SERVER>starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(connections)

while True:
    # Wait for a connection
    print('SERVER>waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('SERVER>connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('SERVER>received {!r}'.format(data))
            if data:
                print('SERVER>sending data back to the client')
                connection.sendall(data)
            else:
                print('SERVER>no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

import socket
import sys

# it should be in .env
ip = 'localhost'
port = 10000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (ip, port)
print('CLIENT>connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    message = b'Hola, este es un msj de prueba.'
    print('CLIENT>sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('CLIENT>received {!r}'.format(data))

finally:
    print('CLIENT>closing socket')
    sock.close()

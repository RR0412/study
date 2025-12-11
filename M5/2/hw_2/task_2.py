import socket
import math

HOST = '127.0.0.1'
PORT = 2345

s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print(f'Waiting for connection on {PORT} port')
conn, addr = s.accept()
print(f'Connected by address {addr}')
conn.sendall(b'Please enter the number:\n')
data=conn.recv(1024)
number = int(data.decode())
if number > 50000:
    message = b'Can not calculate,number is too big'
else:
    result = str(math.factorial(number))
    message = b'The factorial of ' + (str(number)).encode() + b' is ' + result.encode()
conn.sendall(message)

conn.close()
s.close()


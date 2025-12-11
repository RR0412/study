import socket

HOST = '127.0.0.1'
PORT = 2811

s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print(f'Waiting for connection on {PORT} port')
conn, addr = s.accept()
print(f'Connected by address {addr}')
conn.sendall(b'Please enter the first number:\n')
data1=conn.recv(1024) 
conn.sendall(b'Please enter the second number:\n')
data2=conn.recv(1024)
number1 = int(data1.decode())
number2 = int(data2.decode())
addition =  b'The sum is ' + (str(((number1)+(number2)))).encode() + b'\n'
subtraction = b'The subtraction is ' + (str(((number1)-(number2)))).encode() + b'\n'
multiplication = b'The multiplication is ' + (str((number1)*(number2))).encode()  + b'\n'
division = b'The division is ' + (str((number1)/(number2))).encode() 
conn.sendall(addition)
conn.sendall(subtraction)
conn.sendall(multiplication)
conn.sendall(division)
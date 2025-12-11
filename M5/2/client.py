import socket

HOST  = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    message = s.recv(1024)
    print('Message: ', repr(message))

    s.sendall(b'Dmitrii')
    answer = s.recv(1024)

    print('Received answer: ',repr(answer))
    
    
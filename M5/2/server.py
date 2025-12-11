import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 8000

s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print(f'Waiting for connection on {PORT} port')
conn, addr = s.accept()

print(f'Connected by {addr}')

now = f'Datetime is now: {datetime.now()}\n'
conn.sendall(now.encode())

conn.close()
s.close()
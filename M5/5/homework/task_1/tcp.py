import socket

HOST = '127.0.0.1'
PORT = 2811

s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print(f'Waiting for connection on {PORT} port')
conn,addr = s.accept()
print(f'Connected by address {addr}')
entries = []
while True:
    data = conn.recv(1024)
    entry = data.decode().strip()
    entries.append(entry)
    if entry == '--END--':
        break
total_lines = len(entries)
length = ''.join(entries)
total_length = len(length)
binary = b''
for element in entries:
    binary += str(element).encode()+b'\n'
binary += b'Hello, Client!\n'
lines = b'Total lines :' + str(total_lines).encode() + b'\n'
length = b'Total length :' + str(total_length).encode() + b'\n'


conn.sendall(binary)
conn.sendall(lines)
conn.sendall(length)
conn.close()
s.close()










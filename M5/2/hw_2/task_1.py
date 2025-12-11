import socket
import random

HOST = '127.0.0.1'
PORT = 1234

s = socket.socket(socket. AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print(f'Waiting for connection on {PORT} port')
conn, addr = s.accept()

print(f'Connected by address {addr}')

quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Small steps every day lead to big changes.",
    "Your only limit is the one you set yourself.",
    "Dream big, start small, act now.",
    "Discipline is choosing what you want most over what you want now.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Doubt kills more dreams than failure ever will.",
    "What you do today can improve all your tomorrows.",
    "The future depends on what you do in the present.",
    "Every accomplishment begins with the decision to try."
]

random_quote = random.choice(quotes)
phrase = f'Random phrase is:  {random_quote}\n'
conn.sendall(phrase.encode())

conn.close()
s.close()

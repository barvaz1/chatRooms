import socket
import sys
import select

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 80))
do = True
while do:
    name = input()


    my_socket.send(name.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data)
    if (name == 'EXIT'):
        do = False
my_socket.close()
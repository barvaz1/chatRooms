import socket
import re

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 80))


def sendChetMsg(str1):
    """

    :param str1: string
    """
    my_socket.send(str1.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data)


def sign_up(user_name, eMail, first_name, last_name, password1, password2):
    print(2)
    # Are they all not 0?
    for msg in ["sign_up", user_name, eMail, first_name, last_name, password1]:
        if msg is None:
            return
    print(3)
    # check the the user name
    if len(user_name) <= 4:
        return "user name can only have more then 4 letters"
    print(4)
    # check if the email is xxxx@xxx.xx:
    if re.match(r'[A-Za-z1-9._%+-]+@+[A-Za-z1-9._%+-]+\.+[A-Za-z1-9._%+-]', "mobarak9136@gmail.com") is None:
        return "Invalid email address"
    print(5)
    # Does the password match the password authentication?
    if password1 != password2:
        return "check your password"
    print(6)
    if len(password1) < 8:
        return "password too short"
    print(7)
    if not password1.isalnum():
        return "password must contain numbers and letters"
    print(8)
    # check if the name is all text and more then 1 letters
    for name in [first_name, last_name]:
        if not name.isalpha():
            return "name can only have letters"
        print(9)
        if len(name) <= 1:
            print(10)
            return "name can only have more then 1 letters"
    print(11)
    for msg in ["sign_up", user_name, eMail, first_name, last_name, password1]:
        print(msg)
        data = ""
        while data != msg:
            my_socket.send(msg.encode())  # send to the server data
            data = my_socket.recv(1024).decode()
            print("The server sent " + data)


def disconnectServer():
    my_socket.close()

import socket
import re

my_socket = socket.socket()
my_socket.connect(('127.0.0.1', 80))

SIGN_UP = "sign"
LOG_IN = "loin"
DIVIDER = "&"
LOG_OUT = "lout"
ERROR = "Error"

def sendChetMsg(str1):
    """
    :param str1: string
    """
    my_socket.send(str1.encode())
    data = my_socket.recv(1024).decode()
    print("The server sent " + data)


def sign_up(user_name, last_name, first_name, eMail, Mobile_num, password1, password2):
    print(2)
    # Are they all not 0?
    for msg in [SIGN_UP, user_name, eMail, first_name, last_name, password1, Mobile_num]:
        if msg == "":
            return "You must fill in all the details"
    print(3)

    # Mobile_num len =10
    if len(Mobile_num) != 10:
        return "Mobile num can only have 10 digits"

    if not Mobile_num.isnumeric():
        "Mobile num can only have 10 digits"
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

    return send_cmd([SIGN_UP, user_name, last_name, first_name, eMail, Mobile_num, password1])


def log_in(user_name, password):
    for msg in [LOG_IN, user_name, password]:
        if msg == "":
            return "You must fill in all the details"

    return send_cmd([LOG_IN, user_name, password])


def log_out():
    send_cmd(LOG_OUT)


def send_cmd(lst):
    print(12)
    # The form of the message: cmd param1 param2 param3...&
    data = " ".join(lst)

    print(data)
    data = "" + data + DIVIDER + str(len(data))

    print(data)
    my_socket.send(data.encode())
    return my_socket.recv(1024).decode()


def disconnectServer():
    my_socket.close()

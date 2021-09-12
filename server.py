import socket
import select
import hashlib

import server_db

MAX_MSG_LENGTH = 1024
SERVER_PORT = 80
SERVER_IP = "0.0.0.0"

SIGN_UP = "sign"
DIVIDER = "&"
LOG_IN = "loin"
NAME = "name"
LOG_OUT = "lout"
SUCCESS = "success"
ERROR = "Error"

# The number of the room where a client is
OPEN_ROOM = 0
LOBBY = 1


def check_msg(data):
    lst = data.split(DIVIDER)
    return len(lst[0]) == int(lst[1])


def handle_requests(data, conn):
    data = data.split(DIVIDER)[0]
    cmd = data[0:4]
    data = data[5:].split()

    # sign up?
    if cmd == SIGN_UP:
        data[-1] = hashlib.md5(data[-1].encode()).hexdigest()
        return server_db.create_user(conn, data)

    elif cmd == LOG_IN:
        data[-1] = hashlib.md5(data[-1].encode()).hexdigest()
        return server_db.check_password(conn, data[0], data[1])
    else:
        return ERROR


def main():
    conn = server_db.create_connection(r"Users.db")

    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()

    # lst of all the sockets
    client_sockets = {}
    messages_to_send = []

    # handle requests until user asks to exit
    done = False
    while not done:

        # create list of all the sockets
        client_sockets_lst = list(client_sockets.keys())

        # socket before connection
        r_list, w_list, x_list = select.select([server_socket] + client_sockets_lst, client_sockets_lst, [])

        for current_socket in r_list:

            # new client?
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets[connection] = [OPEN_ROOM, None]

            else:
                # get data from existing client
                print("Data from existing client")
                data = current_socket.recv(MAX_MSG_LENGTH).decode()

                # empty data?
                if data == "":
                    print("Connection closed", )
                    del client_sockets[current_socket]
                    current_socket.close()

                # new cmd?
                else:
                    if check_msg(data):

                        answer = handle_requests(data, conn)

                        # any data that need to be save?
                        print(answer)
                        if answer.split()[0] == NAME:
                            print(2)
                            # save the names and move the client to the lobby
                            client_sockets[current_socket][0] = LOBBY
                            client_sockets[current_socket][1] = answer.split()[1]
                            print(client_sockets)
                            answer = SUCCESS

                        messages_to_send.append((current_socket, answer))

                    else:
                        messages_to_send.append((current_socket, "Error, please try again"))

        for message in messages_to_send:
            current_socket, data = message
            if current_socket in w_list:
                current_socket.send(data.encode())
            messages_to_send.remove(message)


if __name__ == '__main__':
    main()

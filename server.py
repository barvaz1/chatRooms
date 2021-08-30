import socket
import select
import server_db
import hashlib

MAX_MSG_LENGTH = 1024
SERVER_PORT = 80
SERVER_IP = "0.0.0.0"

SIGN_UP = "sign"
DIVIDER = "&"
LOG_IN = "log_"


def check_msg(data):
    lst = data.split(DIVIDER)
    return len(lst[0]) == int(lst[1])


def handle_requests(data, conn):
    data = data.split(DIVIDER)[0]
    print(data)
    cmd = data[0:4]
    data = data[5:].split()


    # sign up?
    if cmd == SIGN_UP:
        data[-1] = hashlib.md5(data[-1].encode()).hexdigest()
        print(1)
        return server_db.create_user(conn, data)

    elif cmd == LOG_IN:
        data[-1] = hashlib.md5(data[-1].encode()).hexdigest()
        print(data)
        return server_db.check_password(conn, data[0], data[1])



def main():
    conn = server_db.create_connection(r"Users.db")

    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()

    # lst of all the sockets
    client_sockets = []
    messages_to_send = []

    # handle requests until user asks to exit
    done = False
    while not done:
        # socket before connection
        sign_up_rlist, sign_up_wlist, sign_up_xlist = select.select([server_socket] + client_sockets, client_sockets,
                                                                    [])

        for current_socket in sign_up_rlist:

            # new client?
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(connection)

            else:
                # get data from existing client
                print("Data from existing client")
                data = current_socket.recv(MAX_MSG_LENGTH).decode()

                # empty data?
                if data == "":
                    print("Connection closed", )
                    client_sockets.remove(current_socket)
                    current_socket.close()

                # new cmd?
                else:
                    if check_msg(data):

                        messages_to_send.append((current_socket, handle_requests(data, conn)))
                    else:
                        messages_to_send.append((current_socket, "Error, please try again"))

        for message in messages_to_send:
            current_socket, data = message
            if current_socket in sign_up_wlist:
                print(data)
                current_socket.send(data.encode())
            messages_to_send.remove(message)


if __name__ == '__main__':
    main()

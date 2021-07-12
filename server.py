import socket
import select

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"


def main():
    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()

    #lst of all the sockets
    client_sockets = []

    # handle requests until user asks to exit
    done = False
    while not done:
        rlist, wlist, xlist = select.select( [server_socket] + client_sockets, [], [] )

        for current_socket in rlist:
            if current_socket is server_socket:
                connection, client_address = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(connection)

            else:
                print("Data from existing client\n")

if __name__ == '__main__':
    main()
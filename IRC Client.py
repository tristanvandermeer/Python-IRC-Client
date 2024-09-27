import socket
import threading
import re # Regex


def send_message(client):

    # COMPLETE

    pass


def receive_messages(client):
    while True:
        response = client.recv(4096).decode("utf-8")

        if response:
            print(response)
            pongCheck = re.search("^PING", response )

            if str(pongCheck) == "None":

                pass

            else:

                pongCode = str(response).split(":")
                client.send(f"PONG {pongCode[1]}".encode("utf-8"))
                print(f"[SENT MESSAGE] PONG {pongCode[1]}")


def irc_client(HOST, PORT, NICK, CHANNEL):
    # Automatically get IP Address of host
    # print(socket.gethostbyname(socket.gethostname()))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    threading.Thread(target=receive_messages, args=(client,)).start()

    client.send(f"NICK {NICK}\r\n".encode("utf-8"))
    client.send(f"USER {USER}\r\n".encode("utf-8"))



HOST = "irc.freenode.net"
PORT = 6667
ADDR = (HOST, PORT)
NICK = "HangedMan"
USER = "Guest 0 * :tarot"
REALNAME = "tarot"
CHANNEL = ""

# USER_MESSAGE = (USER, socket.gethostbyname(socket.gethostname()), HOST, REALNAME)

irc_client(HOST, PORT, NICK, CHANNEL)

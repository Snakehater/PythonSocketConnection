#UDP client broadcasts to server(s)
import socket
from time import sleep

address = ('<broadcast>', 54545)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

data = "Request"
client_socket.sendto(data, address)

recv_data, addr = client_socket.recvfrom(2048)
print addr,recv_data
# while True:
#     recv_data, addr = client_socket.recvfrom(2048)
#     print addr,recv_data
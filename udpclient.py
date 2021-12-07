import socket
import time


msgFromClient = "Hello UDP Server"

bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

for x in range(10):
    t1 = time.perf_counter()
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    t2 = time.perf_counter()
    msg = "Rely from Server {}\tRTT={}".format(msgFromServer[0], (t2 - t1)*1000)

    print(msg)
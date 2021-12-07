import socket
import time
import sys
import statistics

def clientOf(ip=None):
    if ip is None:
        ip = '127.0.0.1'
    msgFromClient = "Hello UDP Server"

    bytesToSend = str.encode(msgFromClient)

    serverAddressPort = (ip, 20001)

    bufferSize = 1024

    # Create a UDP socket at client side

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocket.settimeout(1)
    # Send to server using created UDP socket

    rttList = []

    for x in range(10):
        t1 = time.perf_counter()

        try:
            UDPClientSocket.sendto(bytesToSend, serverAddressPort)
            msgFromServer = None
            msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        except socket.timeout:
            print('Timeout ! Over 1 second')

        t2 = time.perf_counter()
        if msgFromServer is not None:
            msg = "Rely from Server {}\tRTT={}ms".format(msgFromServer[0], (t2 - t1)*1000)
            rttList.append((t2 - t1)*1000)
            print(msg)
    
    print('Max=%fms\t Min=%fms\navg=%sms' %(max(rttList), min(rttList), statistics.mean(rttList)))


if __name__ == '__main__':
    try:
        server = sys.argv[1]
    except IndexError:
        server = None
    finally:
        clientOf(server)
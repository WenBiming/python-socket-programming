import socket
import sys


def serverOf(ip):

    port = 20001
    buffersize = 1024


    msgFromServer = 'This is upd server speaking'
    bytesToSend = str.encode(msgFromServer)
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)


    s.bind((ip, port))


    print('UDP server {}\t{} up and listening'.format(hostname, hostip))
    count = 0

    while True:
        message, address = s.recvfrom(buffersize)
        print('Message from Client:{}'.format(message))
        print('client IP address: {}'.format(address))
        
        s.sendto(bytesToSend, address)
        count += 1
        if count == 10:
            break

    s.close()

if __name__ == '__main__':
    try:
        client = sys.argv[1]
    except IndexError:
        client = ''
    finally:
        serverOf(client)
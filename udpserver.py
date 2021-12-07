import socket


ip = '127.0.0.1'
port = 20001
buffersize = 1024

msgFromServer = 'This is upd server speaking'
bytesToSend = str.encode(msgFromServer)
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
s.bind((ip, port))
print('UDP server up and listening')
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
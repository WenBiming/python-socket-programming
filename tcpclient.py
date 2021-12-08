import socket
import sys


def clientOf(target_host=None):
    if target_host is None:
        target_host = '127.0.0.1'

    target_port = 51112
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    client.connect((target_host, target_port))
    # user_input = 'file.txt'
    user_input = input('please input the file name in server\n')
    client.send(user_input.encode())

    try:
        response = client.recv(4096)
        print(response.decode())
    except socket.timeout:
        print('timeout')

  
    client.close()


if __name__ == '__main__':
    try:
        ip = sys.argv[1]
        print('connecting to %s' % ip)
        clientOf(ip)
    except IndexError:
        print('connecting to localhost')
        clientOf()

        
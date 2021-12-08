import socket
import threading


def handle_client(client_socket):
    message, address = client_socket.recvfrom(1024)
    print('recieve {} from {}\n'.format(message, address))
    
    try:
        f = open(str(message))
        for x in f:
            # client_socket.send(x.encode())
            print(x)
    except FileNotFoundError:
        client_socket.send('file not found in server'.encode())
    
    client_socket.close()
    

def serverOf(): 
    bind_ip = '0.0.0.0'
    bind_port = 51112

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    
    server.bind((bind_ip, bind_port))

    server.listen(5)
    print('tcp server up and listening')
    

    while True:
        client, addr = server.accept()
        print('acception from {}\n'.format(addr))
        
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
        

if __name__ == '__main__':
    serverOf()
        
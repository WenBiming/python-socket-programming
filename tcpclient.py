import socket


target_host = '127.0.0.1'
target_port = 51112

while True:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((target_host, target_port))
    
    user_input = None
    while user_input is None:
        user_input = input('please input the file name you want to fetch\n')
        
    
    
    client.send(user_input.encode())
    
    while True:
        try:
            response, address = client.recvfrom(1024)
            print(str(response))
        except socket.timeout:
            break

    
client.close()
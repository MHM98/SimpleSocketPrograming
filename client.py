import socket
name=input('enter the name:')
#address=input('enter your address:')
#root_address=address+'/'+name+'.html'
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65435        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(name.encode())
    respons = s.recv(1024)
    
    if(respons.decode()=='200'):
        while True:
            data=s.recv(1024)
            if not data:
                break
            with open(name+'.html','wb') as content:
                content.write(data)
                print('File downloaded.')
                break
    
    else:
        print("404NOTFOUNDED")
            
    
   
    

#print('Received', repr(data))
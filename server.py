import urllib.request
import socket
import os
links=['https://stackoverflow.com','https://www.wikipedia.org','https://www.reddit.com','https://www.yahoo.com','https://www.twitch.tv','https://www.linkedin.com','https://www.instagram.com','https://www.github.com']
   
for i in links:
    html_res = urllib.request.urlopen(i)
    html_content = html_res.read()
    i=i.replace('https://','')
    name="serverFile/"+i+".html"
    file = open(name, 'w',encoding='utf-8') 
    file.write(html_content.decode())
    file.close()
    

files=os.listdir('serverFile')


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65435        # Port to listen on (non-privileged ports are > 1023)
FileFounded=False
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('server is runnig...')
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            for file in files:
                if data + ".html" == file:
                    FileFounded=True
                    conn.send('200'.encode()) 
                    with open('serverFile/'+file,'rb') as client_file:
                     conn.sendfile(client_file)
            if not FileFounded:
                s.sendall('404NOTFOUNDED'.encode())     
                
                    
        
            
                
            
            
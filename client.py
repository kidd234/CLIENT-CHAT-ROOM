import socket
import sys
import time
# creating the socket and accepting user hostname
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080


#connecting to the server
print('this is your ip address: ', ip)
server_host = input('Enter friend\'s IP address:')
name = input("Enter Your name: ")

socket_server.connect((server_host, sport))

#Recieving packets and messages from server
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name,' has joined...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ':', message)
    message = input("Me : ")
    socket_server.send(message.encode())


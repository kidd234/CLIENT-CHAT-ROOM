#importing required librarys
import socket
import sys
import time
#https://www.askpython.com/python/examples/create-chatroom-in-python

#creating socket and retrieving the hostname
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
port = 8080

#brinding the host and port

new_socket.bind((host_name, port))
print('Binding successful!')
print('this is your IP:', s_ip)

#listening for connections
name = input('Enter name:')
new_socket.listen(1)

#accpeting incoming connection
conn, add= new_socket.accept()
print("Recieved connection from ", add[0])
print("Connection Esatblished, connected from:",add[0])

#storing incomming connection data
client = (conn.recv(1024)).decode()
print(client + ' has connected')
conn.send(name.encode())

#Delivering Packets/Messages
while True:
    message = input('Me : ')
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ':', message)
    
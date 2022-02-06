import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 80
ThreadCount = 4

try:
	ServerSocket.bind((host, port))

except socket.error as e:
	print(str(e))

print('Waiting for a Connection..')

ServerSocket.listen(5)


def threaded_client(connection):
	connection.send(str.encode('Welcome to your favorite Euchure app!'))
	while True:
		data = connection.recv(2048)
		reply = 'Server Says: ' + data.decode('utf-8')
		if not data:
			break

		connection.sendall(str.encode(reply))
	connection.close()

while True:
	Client, address = ServerSocket.accept()
	print('Connected to: ' + address[0] + ';' + str(address[1]))
	start_new_thread(threaded_client, (Client, ))
	ThreadCount += 1
	print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
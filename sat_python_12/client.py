# -*- coding: utf-8 -*-

import time, socket, threading

def receving(name, sock, switch):
	while not switch:
		try:
			while True:
				data, addr = sock.recvfrom(1024)
				print('\n'+data.decode("utf-8"))
				time.sleep(0.2)
		except:
			pass


# Выкл; подключение 	
shutdown = False
join = False

# ваш ip  и порт
host = socket.gethostbyname(socket.gethostname())
port = 0

server = ("192.168.31.22", 11719)

# подключаемся к серверу
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

name = input("$ name: ")

# отправляет сообщения 
s.sendto(("["+name+"] => join chat ").encode("utf-8"), server)
time.sleep(0.2)



# -*-coding:utf-8-*-

import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while 1:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rw', 0)
    clientfile.write('Welcome' + str(clientaddr) + "\n")
    clientfile.write('please enter string :')
    line = clientfile.readline().strip()
    clientfile.write('You entered %d characters \n' % len(line))
    clientfile.close()
    clientsock.close()

## UDP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
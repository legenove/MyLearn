# -*-coding:utf-8-*-

import sys
import socket


port = 70
host = sys.argv[1]
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Error %s" % e
    sys.exit(1)
# s.sendall(filename + "\r\n")
#
# while 1:
#     buf = s.recv(2048)
#     if not buf:
#         break
#     sys.stdout.write(buf)


fd = s.makefile('rw', 0)

fd.write(filename + "\r\n")

for line in fd.readlines():
    sys.stdout.write(line)
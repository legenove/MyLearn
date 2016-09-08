# -*-coding:utf-8-*-

import sys
import time
import socket
from tornado.tcpserver import TCPServer
from tornado.netutil import bind_sockets
from tornado.ioloop import IOLoop
from tornado.ioloop import PeriodicCallback

port = 8888
host = ''
family = socket.AF_UNSPEC
solist = [x for x in dir(socket) if x.startswith('SO_')]
for sol in solist:
    print sol

for res in set(socket.getaddrinfo(host, port, family, socket.SOCK_STREAM)):
    print res
# bind_sockets(port)
print all([6, -1, 5, 6, 3])

if not -1:
    print 1

server = TCPServer()
server.listen(8888)


def test_run():
    print 'runstart'
    time.sleep(0.1)
    print 'runstop'


PeriodicCallback(test_run(), 1000).start()
IOLoop.current().start()
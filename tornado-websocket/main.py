# -*- coding: utf-8 -*-

import time
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket


class Index(tornado.web.RequestHandler):
    def get(self):
        self.write('''
<html>
<head>
<script>
var ws=new Array()
for (var i=0;i<200;i++)
{
    ws[i] = new WebSocket('ws://0.0.0.0:8888/soc');
}
ws[0].onmessage = function(event) {
    var table = document.getElementById('message');
    table.insertRow().insertCell().innerHTML = event.data;
};
</script>
</head>
<body>
<p>hi</p>
<table id='message'></table>
        ''')



class SocketHandler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    clients = set()

    @staticmethod
    def send_to_all(message):
        for c in SocketHandler.clients:
            c.write_message(message)

    def open(self):
        self.write_message('Welcome to WebSocket')
        SocketHandler.send_to_all(str(id(self)) + ' has joined')
        SocketHandler.clients.add(self)
        print len(SocketHandler.clients)

    def on_close(self):
        SocketHandler.clients.remove(self)
        SocketHandler.send_to_all(str(id(self)) + ' has left')
        print len(SocketHandler.clients)

if __name__ == "__main__":
    application = tornado.web.Application([
        ('/', Index),
        ('/soc', SocketHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.bind(8888)
    http_server.start(1)
    # application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

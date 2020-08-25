import random
import time

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler


class RabbitHandler(RequestHandler):
    def get(self):
        self.render('msg/rabbit.html')


class MessageHandler(WebSocketHandler):
    # 当前处理器是一个长连接
    online_clients = []

    def send_all(self, msg):
        for client in self.online_clients:
            self.write_message(msg)

    def open(self):
        # ip = self.request.remote_ip
        username = self.get_secure_cookie('username').decode()
        self.online_clients.append(self)
        self.send_all('%s 进入聊天室' % username)
        # 表示客户端请求连接
        # self.write_message('%s 进入聊天室' % username)

    def on_message(self, message):
        # ip = self.request.remote_ip
        username = self.get_secure_cookie('username').decode()
        msg = self.write_message('%s说: %s' % (username, message))
        self.send_all(msg)

    def on_connection_close(self):
        self.online_clients.remove(self)


class MessageOldHandler(WebSocketHandler):
    # 当前处理器是一个长连接

    def open(self):
        ip = self.request.remote_ip
        # 表示客户端请求连接
        self.write_message('hello, %s' % ip)

        # 每间隔一秒发送一个数字
        self.write_message('---start---')
        for i in range(10):
            time.sleep(1)
            number = random.randint(1, 100)
            self.write_message('%s' % number)
        self.write_message('---end---')

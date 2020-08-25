import os

from tornado.web import Application

from app.ui.menu import MenuModule
from app.views.cookie_v import CookieHandler
from app.views.index_v import IndexHandler
from app.views.order_v import OrderHandler
from app.views.search_v import SearchHandler
from app.views.download import DownloadHandler, AsyncDownloadHandler, Async2DownloadHandler
from app.views.message import RabbitHandler, MessageHandler
from app.views.user import UserHandler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 'D:\Codes\PycharmProjects\pythonProject\pythonProject\microServer\app\_init_.py'

settings = {
    'debug': True,
    'template_path': os.path.join(BASE_DIR, 'templates'),
    'static_path': os.path.join(BASE_DIR, 'static'),
    'static_url_prefix': '/s/',
    'ui_modules': {
        'Menu': MenuModule
    },
    'cookie_secret': 'oliasdjasdpoe&)^31'
}


def make_app(host='localhost'):

    return Application(handlers=[
        ('/', IndexHandler),
        ('/search', SearchHandler),
        ('/cookie', CookieHandler),
        ('/download', DownloadHandler),
        ('/download2', AsyncDownloadHandler),
        ('/download3', Async2DownloadHandler),
        ('/rabbit', RabbitHandler),
        ('/message', MessageHandler),
        ('/login', UserHandler),
        (r'/order/(?P<action_code>\d+)/(?P<order_id>\d+)', OrderHandler),
    ], default_host=host, **settings)

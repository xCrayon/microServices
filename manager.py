import tornado.web
import tornado.ioloop
import tornado.options
from tornado.httputil import HTTPServerRequest


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 1. 请求参数读取
        wd = self.get_argument('wd')
        print(wd)

        # 2. 读取多个参数名相同的参数值
        titles = self.get_arguments('title')
        print(titles)

        # 3. 从查询参数中读取url路径参数
        wd2 = self.get_query_argument('wd')
        print(wd2)
        titles2 = self.get_query_arguments('title')
        print(titles2)

        # 4. 从请求对象中读取参数
        req: HTTPServerRequest = self.request

        # request请求中的数据都是dict字典类型
        wd3 = req.arguments.get('wd')
        print(wd3)    # 字典key对应的value都是bytes字节类型

        titles3 = req.query_arguments.get('title')
        print(titles3)

        self.write('<h3>我是主页</h3>')

    def post(self):
        # 新增数据
        # 读取表单参数
        # name = self.get_argument('name')
        # city = self.get_argument('city')

        # 建议使用以下方式
        name = self.get_body_argument('name')
        city = self.get_body_argument('city')

        wd = self.get_query_argument('wd')

        self.write('<h3>我是POST请求方式: %s %s %s</h3>' % (name, city, wd))

    def put(self):
        self.write('<h3>我是PUT请求方式</h3>')

    def delete(self):
        self.write('<h3>我是DELETE请求方式</h3>')


def make_app():
    return tornado.web.Application([
        ('/', IndexHandler)
    ], default_host=tornado.options.options.host)


if __name__ == '__main__':
    # 定义命令行参数
    tornado.options.define('port',
                           default=8000,
                           type=int,
                           help='bind socket port')

    tornado.options.define('host',
                           default='localhost',
                           type=str,
                           help='set host name')
    # 解析命令行参数
    tornado.options.parse_command_line()

    app = make_app()
    app.listen(tornado.options.options.port)

    print('starting Web Server http://%s:%s'
          % (tornado.options.options.host,
             tornado.options.options.port))
    # 启动服务
    tornado.ioloop.IOLoop.current().start()

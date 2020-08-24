from tornado.web import RequestHandler


class CookieHandler(RequestHandler):
    def get(self):
        # 验证参数中是否存在 name?
        if self.request.arguments.get('name'):
            # 从查询参数中读取Cookie的名称
            name = self.get_query_argument('name')

            # 从cookie中获取name的对象或值
            value = self.get_cookie(name)
            self.write(value)
        else:
            # 查看所有的cookie
            cookies: dict = self.request.cookies
            html = '<ul>%s<ul>'
            ls = []
            for key in cookies:
                ls.append('<li>%s: %s</li>' % (key, self.get_cookie(key)))

            html = ('显示所有的cookie' + html % ''.join(ls))
            html += """
                <form method="post">
                    <input name="name" placeholder="请输入cookie的名称">
                    <button>提交</button>
                </form>
            """

            self.write(html)

    def post(self):
        name = self.get_argument('name')
        if self.request.cookies.get(name, None):
            # 存在的cookie
            self.clear_cookie(name)
            self.write('<h3 style="color:green">删除 %s 成功</h3>' % name)
        else:
            self.write('<h3 style="color:red">删除 %s 失败，该cookie不存在</h3>' % name)

        self.redirect('/cookie')    # 重定向
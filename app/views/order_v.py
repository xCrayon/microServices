from tornado.web import RequestHandler


class OrderHandler(RequestHandler):

    goods = [
        {
            'id': 1,
            'name': 'Python高级开发',
            'author': 'crayon',
            'price': 9999
        },
        {
            'id': 2,
            'name': 'Artificial Intelligence',
            'author': 'crayon',
            'price': 9999
        },
    ]

    action_map = {
        1: '取消订单',
        2: '再次购买',
        3: '评价'
    }

    def query(self, order_id):
        for item in self.goods:
            if item.get('id') == order_id:
                return item

    def initialize(self):
        # 所有的请求方法在调用之前都会进行初始化操作
        print('----initialize----')
        pass

    def prepare(self):
        # 在初始化之后，调用行为方法之前
        # 调用此方法进行预处理
        print('----prepare----')

    def get(self, order_id, action_code):
        print('----get----')
        self.write('订单查询')
        html = """
            <p>
                商品编号: %s
            </p>
            <p>
                商品名称: %s
            </p>
            <p>
                商品价格: %s
            </p>
        """
        goods = self.query(int(order_id))
        self.write(html % (goods.get('id'), goods.get('name'), goods.get('price')))
        self.write(self.action_map.get(int(action_code)))

    def post(self, action_code, order_id):
        print('----post----')
        self.write('----post----')

    def on_finish(self):
        print('-onfinish-')
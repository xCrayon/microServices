from tornado.web import UIModule
from utils.conn import session
from app.models.menu import Menu


class MenuModule(UIModule):
    def render(self):
        # 准备数据（从缓存，从数据库）
        # data = {
        #     'menus': [
        #         {'title': '百度', 'url': 'https://www.baidu.com'},
        #         {'title': '京东', 'url': 'https://www.jd.com'},
        #         {'title': '阿里', 'url': 'https://www.aliyun.com'}
        #     ]
        # }

        data = {
            'menus': session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        }
        # 渲染ui模块的模板
        return self.render_string('ui/menu.html', **data)

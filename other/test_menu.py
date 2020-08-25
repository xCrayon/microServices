from unittest import TestCase

from utils.conn import session, Base
from app.models.menu import Menu


class TestMenuORM(TestCase):
    def test_creat(self):
        Base.metadata.drop_all()
        Base.metadata.create_all()

    def test_add(self):
        m1 = Menu()
        m1.title = '用户管理'

        session.add(m1)
        session.commit()

    def test_adds(self):
        session.add_all([
            Menu(title='订单管理'),
            Menu(title='会员管理', url='/user1', parent_id=1),
            Menu(title='派件员', url='/user2', parent_id=1),
            Menu(title='合作商', url='/user3', parent_id=1),
            Menu(title='订单统计', url='/order_cnt', parent_id=2)
        ])

        session.commit()

    def test_get(self):
        # 查询-session.query(模型类)
        m = session.query(Menu).get(1)
        print(m.title)
        print('----查看子菜单----')
        for cm in m.childs:
            print(cm)

    def test_query_root_menu(self):
        # 查看所有的一级菜单
        ms = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
        for first_m in ms:
            print(first_m)
            # 查看二级菜单
            for second_m in ms.childs:
                print('-'*3, second_m)

    def test_update(self):
        menu = session.query(Menu).get(5)
        menu.title = '合作伙伴'
        session.commit()

    def test_remove(self):
        menu = session.query(Menu).get(5)
        session.delete(menu)
        session.commit()
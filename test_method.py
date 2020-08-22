from unittest import TestCase
import requests


class TestTornadoRequest(TestCase):

    base_url = 'http://localhost:8000'

    def test_index_get(self):
        url = self.base_url + '/'
        # 查询参数
        resp = requests.get(url, params={
            'wd': 'crayon',
            'title': 20
        })
        # 可能会出现400 错误： 原因是查询参数没有给对
        print(resp.text)

    def test_index_post(self):
        url = self.base_url + '/?wd=python'
        resp = requests.post(url, data={
            'name': 'crayon',
            'city': '长沙'
        })
        print(resp.text)

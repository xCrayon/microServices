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


class TestCookieRequest(TestCase):
    url = 'http://localhost:8000/cookie'

    def test_search(self):
        resp = requests.get('http://localhost:8000/search', params={
            'wd': 'python'
        })
        print(resp.text)
        print(resp.cookies)
        for key, cookie in resp.cookies.items():
            print(key, resp.cookies.get(key))

    def test_get(self):
        resp = requests.get(self.url)
        print(resp.text)

    def test_delete(self):
        resp = requests.delete(self.url, params={
            'name': 'token'
        })
        print(resp)

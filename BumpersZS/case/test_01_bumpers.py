#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Software: PyCharm
# @File: test_01_bumpers.py
# @Author: 陈厦林
# @Time: 1月 28, 2021
import unittest
import ddt
import requests

from Script.handle_mysql import do_mysql
from data.bumpers import bumpers_data
from Script.handle_yaml import do_yaml
import json


@ddt.ddt
class TestBumpers(unittest.TestCase):
    """撞客测试-TestBumpers
    """
    def setUp(self):
        """初始化数据
        """
        pass

    @classmethod
    def setUpClass(cls):
        """每次执行用例前删除数据库数据
        """
        do_mysql.delete_data(sql=do_yaml.get_data("mysql", "delete_clue_sql"))

    def tearDown(self):
        """测试完毕清理环境数据
        """
        pass

    @ddt.data(*bumpers_data)
    def test_bumpers(self, item):
        # 第一步：准备测试用例数据
        expected = item["expected"]
        data = item["data"]
        # 第二步：传入参数
        self.url = do_yaml.get_data("api", "base_url")
        self.headers = do_yaml.get_data("api", "headers")
        requests.post(url=self.url, headers=self.headers, json=data)
        # 第三步：更改数据库数据
        do_mysql.update_data()
        # 第四步：再次请求
        res = requests.post(url=self.url, headers=self.headers, json=data)
        # 第五步：断言撞客
        self.assertEqual(expected["code"], res.json()["code"], msg='断言返回值是0接口请求成功')
        self.assertEqual(1, len(res.json()["data"]["failure"]), msg='断言精准撞客失败数据返回数量是否为1')


if __name__ == '__main__':
    unittest.main()


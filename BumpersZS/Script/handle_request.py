#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Software: PyCharm
# @File: handle_request.py
# @Author: 陈厦林
# @Time: 1月 28, 2021
import requests


class HandleRequest:

    def __init__(self):
        self.session = requests.Session()

    def post_bumpers_check_pending_company(self, url, data, headers):
        """post请求撞客待审核数据
        """
        pass
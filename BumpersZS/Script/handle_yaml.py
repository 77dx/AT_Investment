#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Software: PyCharm
# @File: handle_yaml.py
# @Author: 陈厦林
# @Time: 1月 28, 2021
import yaml
import os


class HandleYaml:
    """获取yaml里边的数据，参数化读取，修改直接改yaml
    """
    def __init__(self, filename=None):
        if filename is None:
            CONF_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            filename = os.path.join(CONF_PATH, "conf\\bumperscase.yaml")
            with open(filename, encoding="utf-8") as file:
                self.config_data = yaml.full_load(file)
        else:
            raise Exception("请在bumperscase.yaml配置文件名")


    def get_data(self, section, option):
        """
        读取配置文件数据
        :param section: 区域名
        :param option: 选项名
        :return: 值
        """
        return self.config_data[section][option]

    def get_all_data(self, section):
        """
        读取配置文件某个区域下的所有数据
        :param section:
        :return: 值
        """
        return self.config_data[section]

do_yaml = HandleYaml()


if __name__ == '__main__':
    do_yaml = HandleYaml()
    # print(do_yaml.get_data("mysql", "update_clue_sql") % (1, do_yaml.get_data("company", "not_receive_company")))
    a = do_yaml.get_all_data("company")
    for (i, j) in zip(a, range(len(do_yaml.get_all_data("company")))):
        print(i, j)
    company = []
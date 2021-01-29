#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Software: PyCharm
# @File: handle_create_data.py
# @Author: 陈厦林
# @Time: 1月 28, 2021
from Script.handle_mysql import do_mysql, do_yaml


class HandleCreateData:
    """自动查询数据库是否存在该条数据，如果存在则删除，如果不存在则造新数据，更改数据库状态
    """
    # def handle_received_data(self, args=None):
    #     """查询数据库是否存在已接待数据
    #     """
    #     try:
    #         res_company = do_mysql.get_bumpers_data(sql=do_yaml.get_data("mysql", "select_received_company_sql"))[
    #             "company"]
    #         res_clues_status = do_mysql.get_bumpers_data(sql=do_yaml.get_data("mysql", "select_received_company_sql"))[
    #             "clues_status"]
    #         print(res_company)
    #         print(res_clues_status)
    #     except:
    #         print("往数据库造新数据")

    def get_check_pending_company_data(self, sql, args=None):
        """查询数据库该公司是否存在待审核
        """
        try:
            do_mysql.get_data(sql=sql)
        except Exception:
            raise Exception('报错啦！啦！啦！')

    def get_not_receive_company_data(self, sql, args=None):
        """查询数据库该公司是否存在待接待
        """
        pass

    def get_been_received_company_data(self, sql, args=None):
        """查询数据库该公司是否存在已接待
        """
        pass

    def get_signed_contract_company_data(self, sql, args=None):
        """查询数据库该公司是否存在已签约
        """
        pass

    def get_invalid_company_company_data(self, sql, args=None):
        """查询数据库该公司是否存在无效
        """
        pass


if __name__ == '__main__':
    do_Create = HandleCreateData()
    do_Create.get_check_pending_company_data(do_yaml.get_data("mysql", "delete_check_pending_company_sql"))

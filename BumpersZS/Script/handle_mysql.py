#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Software: PyCharm
# @File: handle_mysql.py
# @Author: 陈厦林
# @Time: 1月 28, 2021
import pymysql
from Script.handle_yaml import do_yaml


class HandleMysql:
    """执行sql语句
    """

    def __init__(self):
        self.conn = pymysql.connect(host=do_yaml.get_data("mysql", "host"),
                                    user=do_yaml.get_data("mysql", "user"),
                                    password=do_yaml.get_data("mysql", "password"),
                                    database=do_yaml.get_data("mysql", "db"),
                                    port=do_yaml.get_data("mysql", "port"),
                                    charset="utf8")
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_data(self, sql, args=None):
        """查询数据库数据返回数据
        """
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        return self.cursor.fetchone()

    def delete_data(self, sql, args=None):
        """删除数据库数据返回数据
        """
        delete_company = ""
        for (i, j) in zip(do_yaml.get_all_data("company"), range(len(do_yaml.get_all_data("company")))):
            delete_company += (do_yaml.get_all_data("company")[i])+"','"
        sql = sql % delete_company
        self.cursor.execute(sql, args=args)
        self.conn.commit()
        return self.cursor.fetchone()

    def update_data(self, args=None):
        """更改数据库数据
        """
        sql1 = "UPDATE wzwl_investment.clue SET clues_status=0 WHERE company='撞客自动化测试待审核科技有限公司' AND clues_type=0;"
        self.cursor.execute(sql1, args=args)
        self.conn.commit()
        sql2 = "UPDATE wzwl_investment.`clue` SET clues_status=1 WHERE company='撞客自动化测试未接待科技有限公司' AND clues_type=0;"
        self.cursor.execute(sql2, args=args)
        self.conn.commit()
        sql3 = "UPDATE wzwl_investment.`clue` SET clues_status=2 WHERE company='撞客自动化测试已接待科技有限公司' AND clues_type=0;"
        self.cursor.execute(sql3, args=args)
        self.conn.commit()
        sql4 = "UPDATE wzwl_investment.`clue` SET clues_status=3 WHERE company='撞客自动化测试已签约科技有限公司' AND clues_type=0;"
        self.cursor.execute(sql4, args=args)
        self.conn.commit()
        sql5 = "UPDATE wzwl_investment.`clue` SET clues_status=5 WHERE company='撞客自动化测试无效科技有限公司' AND clues_type=0;"
        self.cursor.execute(sql5, args=args)
        self.conn.commit()
        # sql = do_yaml.get_data("mysql", "update_clue_sql")
        # print(sql, company, clues_status)
        # for (j, i) in zip(range(len(do_yaml.get_all_data("company"))), do_yaml.get_all_data("company")):
        #     print(j, i)
        #     if i == do_yaml.get_data("company", "check_pending_company"):
        #         sql = do_yaml.get_data("mysql", "update_clue_sql").format(0, do_yaml.get_data("company", "check_pending_company"))
        #     elif i == do_yaml.get_data("company", "not_receive_company"):
        #         sql = do_yaml.get_data("mysql", "update_clue_sql").format(1, do_yaml.get_data("company", "not_receive_company"))
        #     elif i == do_yaml.get_data("company", "been_received_company"):
        #         sql = do_yaml.get_data("mysql", "update_clue_sql").format(2, do_yaml.get_data("company", "been_received_company"))
        #     elif i == do_yaml.get_data("company", "signed_contract"):
        #         sql = do_yaml.get_data("mysql", "update_clue_sql").format(3, do_yaml.get_data("company", "signed_contract"))
        #     elif i == do_yaml.get_data("company", "invalid_company"):
        #         sql = do_yaml.get_data("mysql", "update_clue_sql").format(5, do_yaml.get_data("company", "invalid_company"))
        #     elif i == None:
        #         pass
        #     else:
        #         # raise Exception("情况场景没有覆盖到，请联系开发者完善")
        #         pass
        #     return sql

do_mysql = HandleMysql()

if __name__ == '__main__':
    do_mysql = HandleMysql()
    # print(do_mysql.delete_data(sql=do_yaml.get_data("mysql", "delete_clue_sql")))
    print(do_mysql.update_data())

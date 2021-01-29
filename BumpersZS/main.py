import time
import unittest
import os
from BeautifulReport import BeautifulReport
from Script.handle_yaml import do_yaml

now = time.strftime("%Y-%m-%d %H：%M：%S", time.localtime(time.time()))
localpath = os.getcwd()
filepath = os.path.join(localpath, 'case')
# 按类加载全部testxxx测试用例
suite = unittest.defaultTestLoader.discover(filepath, 'test*.py')
# 加载执行用例生成报告
result = BeautifulReport(suite)
# 定义报告属性
result.report(description=do_yaml.get_data("report", "description"),
              filename=os.path.join("Reports", do_yaml.get_data("report", "filename") + now),
              theme='theme_default', log_path=filepath)

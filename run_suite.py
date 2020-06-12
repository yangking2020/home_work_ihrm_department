# 导包
import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
import app
# 创建测试套件
suite = unittest.TestLoader().discover('./script','test*.py')
# 定义报告文件
file_name = app.BASE_DIR + '/report/ihrm%s.html' % time.strftime('%Y%m%d%H%M%S')
# 运行并读写
with open(file_name,'wb') as f:
    runner = HTMLTestRunner(f,verbosity=1,title='ihrm部门测试报告',description='完美的测试报告')
    runner.run(suite)
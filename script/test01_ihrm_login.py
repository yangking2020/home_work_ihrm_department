# 导包
import logging
import unittest
# 设计测试类
from parameterized import parameterized

import app
from api.ihrm_login_api import LoginIhrmApi
from utiles import assert_commen, read_data


class TestLoginIhrm(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.loginihrmapi = LoginIhrmApi()
    # 测试用例
    def tearDown(self):
        ...
    # 定义文件路径
    file_name = app.BASE_DIR + '/data/data_login.json'
    @parameterized.expand(read_data(file_name))
    def test01_login_success(self,case_name,request_body,http_code,success,code,message):
        # 构建数据
        # data = {"mobile": "13800000002", "password": "123456"}
        # 调用登陆接口
        response = self.loginihrmapi.login_api(request_body,{"Content-Type":"application/json"})
        # 打印
        logging.info(response.json())
        # 断言
        assert_commen(self,http_code,success,code,message,response)



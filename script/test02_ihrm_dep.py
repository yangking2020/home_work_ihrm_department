# 导包
import unittest
import logging
from parameterized import parameterized
import app
from api.ihrm_department_api import DepartmentIhrmApi
from api.ihrm_login_api import LoginIhrmApi
from utiles import assert_commen, read_dep_data


# 创建测试类
class TestIhrmDep(unittest.TestCase):

    # 初始化
    def setUp(self):
        self.dep_api = DepartmentIhrmApi()
        self.login_api = LoginIhrmApi()

    def tearDown(self):
        ...

    file_name = app.BASE_DIR + '/data/data_dep.json'
    # 测试用例登陆
    def test01_login_success(self):

        # 构建数据
        data = {"mobile": "13800000002", "password": "123456"}
        # 调用登陆接口
        response = self.login_api.login_api(data,{"Content-Type":"application/json"})
        # 打印结果
        logging.info(response.json())
        # 获取令牌
        token = 'Bearer ' + response.json().get('data')
        # 组合响应头数据
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}

    # 测试用例部门添加
    @parameterized.expand(read_dep_data(file_name, 'add_dep'))
    def test02_add_dep(self,name,dep_code,http_code,success,code,massage):
        # 调用添加接口
        response = self.dep_api.add_dep_api(name,dep_code,app.HEADERS)
        # 打印结果
        logging.info(response.json())
        # 获取部门
        app.DEP_ID = response.json().get('data').get('id')
        logging.info(app.DEP_ID)
        # 断言
        assert_commen(self, http_code, success, code, massage, response)
    # 测试用例部门查询
    @parameterized.expand(read_dep_data(file_name, 'query_dep'))
    def test03_query_dep(self,http_code,success,code,massage):
        # 调用查询接口
        response = self.dep_api.query_dep_api(app.DEP_ID,app.HEADERS)
        # 打印结果
        logging.info(response.json())
        # 断言
        assert_commen(self, http_code, success, code, massage, response)

    # 测试用例部门修改
    @parameterized.expand(read_dep_data(file_name,'modify_dep'))
    def test04_modify_dep(self,modify,http_code,success,code,massage):
        # 调用修改接口
        response = self.dep_api.modify_dep_api(app.DEP_ID,modify,app.HEADERS)
        # 打印结果
        logging.info(response.json())
        # 断言
        assert_commen(self, http_code, success, code, massage, response)
    # 测试用例部门删除
    @parameterized.expand(read_dep_data(file_name, 'delete_dep'))
    def test05_delete_dep(self,http_code,success,code,massage):
        # 调用修改接口
        response = self.dep_api.delete_dep_api(app.DEP_ID,app.HEADERS)
        # 打印结果
        logging.info(response.json())
        # 断言
        assert_commen(self, http_code, success, code, massage, response)
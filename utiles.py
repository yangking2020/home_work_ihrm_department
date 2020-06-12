# 导包
import json
import logging.handlers
import app
# 封装类 生成日志
def init_logging():
    # 生成日志器
    logger = logging.getLogger()
    # 设置级别
    logger.setLevel(level=logging.INFO)
    # 处理器 (控制台,文件)
    sh = logging.StreamHandler()
    file_name = app.BASE_DIR + '/log/ihrm.log'
    tr = logging.handlers.TimedRotatingFileHandler(file_name,when='M',interval=1,backupCount=2,encoding='utf-8')
    formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    sh.setFormatter(formatter)
    tr.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(tr)
# 断言
def assert_commen(self,http_code,success,code,massage,response):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(massage, response.json().get('message'))

# 引入参数函数
def read_data(filename):
    list_params = []
    # 转变车python格式
    with open(filename,encoding='utf-8') as f:
        jsondata = json.load(f)
        # 遍历
        for i in jsondata:
            list_params.append(tuple(i.values()))
        # 返回列表
    return list_params
# 引入参数函数
def read_dep_data(filename,interface):
    with open(filename,encoding='utf-8') as f:
        jsondata = json.load(f)
        list_params = jsondata.get(interface)
        result_list = []
        result_list.append(tuple(list_params.values()))
    return result_list
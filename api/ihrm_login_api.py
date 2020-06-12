# 导包
import requests
# 登陆接口类
class LoginIhrmApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"
    # 调用登陆接口
    def login_api(self,data,headers):
        return requests.post(url=self.login_url,json=data,
                             headers=headers)


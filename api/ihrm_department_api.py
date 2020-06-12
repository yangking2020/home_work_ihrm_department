# 导包
import requests
# 部门增改查删
class DepartmentIhrmApi:
    def __init__(self):
    # 初始化数据
        self.dep_url = "http://ihrm-test.itheima.net" + "/api/company/department"
    # 调用增加部门接口
    def add_dep_api(self,name,code,header):
        return requests.post(url=self.dep_url,
                             json={"name": name,
                                   "code": code,
                                   "manager": "淘气",
                                   "introduce": 1,
                                   "pid": "测试部"},
                             headers=header)
    # 调用查询接口
    def query_dep_api(self,dep_id,header):
        return requests.get(url=self.dep_url+'/'+dep_id,headers=header)

    # 调用修改接口
    def modify_dep_api(self,dep_id,data,header):
        return requests.put(url=self.dep_url+'/'+dep_id,json=data,headers=header)

    # 调用删除接口
    def delete_dep_api(self,dep_id,header):
        return requests.delete(url=self.dep_url+'/'+dep_id,headers=header)

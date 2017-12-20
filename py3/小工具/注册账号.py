#!/usr/bin/env python
# -*- coding:utf-8 -*-


import json
import requests

email = "244896035@qq.com"
pwd = "bryan123"
name = "Bryan"
acc_type = "user"

# 删除账户

url = "http://192.168.3.6:5118/v1/" + acc_type + "?email=" + email
data = {
    'email': email,
    "password": pwd,
    "name": name
}
headers = {'content-type': 'application/json'}
try:
    res = requests.delete(url)

except Exception as e:
    print("%s" % e)

try:
    print(res.json())
except Exception as e:
    print("%s" % e)


# 注册账户
url = "http://192.168.3.6:5118/v1/" + acc_type
data = {
    'email': email,
    "password": pwd,
    "name": name
}
headers = {'content-type': 'application/json'}
try:
    res = requests.post(url, data=json.dumps(data), headers=headers)

except Exception as e:
    print("%s" % e)
print(res.json())
assert res.status_code == 200, "创建账户失败"




url = "http://192.168.3.6:5118/v1/" + acc_type + "/token?type=activate&email=" + email

headers = {'content-type': 'application/json'}
try:
    res = requests.get(url, headers=headers)
except Exception as e:
    print("%s" % e)
assert res.status_code == 200, "创建账户失败"
print(res.json())
result = res.json()
token = result["token"]
print(token)
print("----获取账户token成功----")


url = "http://192.168.3.6:5118/v1/" + acc_type + "/activate?ticket=" + token

headers = {'content-type': 'application/json'}
try:
    res = requests.get(url, headers=headers)
except Exception as e:
    print("%s" % e)

print(res.json())
assert res.status_code == 200, "激活账户失败"
assert res.json()["type"] == "activate", "激活账户失败"

print("----激活账户成功----")

""""""
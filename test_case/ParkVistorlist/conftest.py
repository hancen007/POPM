# -*- coding: utf-8 -*-
# @File  : conftest.py
# @Author: 岑苏岸
# @Date  : 2018/11/22
# @Desc  :


from common.Req import Req
import pytest






@pytest.fixture(scope="class")
def sysLogin():

    S = Req()

    headers ={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    seccode = "http://47.106.221.58:5002/mgr/normal/authz/seccode.do"

    re = S.get(seccode)

    verify_seccode = "http://47.106.221.58:5002/mgr/normal/authz/verify_seccode.do"

    data = {"seccode": 9999}

    re = S.post(verify_seccode,data=data)

    print(re.text)


    url = "http://47.106.221.58:5002/mgr/normal/ajax/login.do"

    data = {
    "username": "autotest",
    "password": "123456",
    "seccode": 9999}

    re =S.post(url,data,headers=headers)

    return S


if __name__ == "__main__":

    sysLogin()
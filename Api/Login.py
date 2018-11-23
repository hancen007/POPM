# -*- coding: utf-8 -*-
# @File  : parkVisitorlist.py
# @Author: 岑苏岸
# @Date  : 2018/11/16
# @Desc  :

from common.Req import Req
from Config.Config import Config
from urllib.parse import urljoin
from collections import OrderedDict
import allure

import requests

import json

class Login():

    def __init__(self):

        self.conf = Config()
        self.host = self.conf.host
        self.Seesion = requests.Session()

    def login(self):

        seccode = urljoin(self.host,"/mgr/normal/authz/seccode.do")

        verify_seccode = urljoin(self.host,"/mgr/normal/authz/verify_seccode.do")

        url = urljoin(self.host,"/mgr/normal/ajax/login.do")


        headers ={
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }
        re = self.Seesion.get(seccode)

        data = {"seccode": 9999}

        re = self.Seesion.post(verify_seccode,data=data)

        data = {
            "username": "autotest",
            "password": "123456",
            "seccode": 9999
        }
        re = self.Seesion.post(url,data,headers=headers)
        print(re.json())
        return self.Seesion


if __name__ == "__main__":

    L = Login()

    L.login()

# -*- coding: utf-8 -*-
# @File  : test_baidu.py
# @Author: 岑苏岸
# @Date  : 2018/11/16
# @Desc  :

import pytest,os
import allure
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(BASE_DIR, "../.."))
from common.utils import YmlUtils
from Api.parkVisitorlist import parkVistorlist



class TestparkVisitorlist():
    """车辆模块"""
    def test_car_getParklist(self,Login):
        """验证关键字查询"""
        P = parkVistorlist(Login)

        result = P.getParklist("CY009")

        print(result)

    def test_car_save(self,Login):
        """新增停车信息"""

        P = parkVistorlist(Login)

        re = P.save()


    def test_car_del(self,Login):
        """删除停车信息"""

        P = parkVistorlist()

        re = P.delete()

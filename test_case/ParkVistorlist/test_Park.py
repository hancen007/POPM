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
    def test_car_getParklist(self):
        """验证关键字查询"""
        P = parkVistorlist()

        result = P.getParklist("CY009")

        print(result)


    def test_car_save(self,sysLogin):
        """新增停车信息"""

        P = parkVistorlist(sysLogin)

        re = P.save()


    def test_car_del(self,sysLogin):
        """删除停车信息"""

        P = parkVistorlist(sysLogin)

        re = P.delete()

# -*- coding: utf-8 -*-
# @File  : test_park_data_driven.py
# @Author: 岑苏岸
# @Date  : 2018/11/26
# @Desc  :


import pytest,os
import allure
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
root_path = os.path.abspath(os.path.join(BASE_DIR, "../.."))
from common.utils import YmlUtils
from Api.parkVisitorlist import parkVistorlist

args_item = "send_data,expect"

test_data,case_desc = YmlUtils("/test_data/Park/parklist.yml").getData
@allure.feature("博客文章内容")
@pytest.mark.parametrize(args_item, test_data, ids=case_desc)
class TestWordpress():
    """验证搜索的关键字"""
    @allure.story('验证查询')
    def test_getlist(self,send_data,expect):

        re = parkVistorlist().getParklist(send_data["carLicenseNumber"])
        result =re.json()
        assert result["status"] == expect["status"]
        assert result["resultCode"] == expect["resultCode"]
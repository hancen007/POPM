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
from Api.wordpress import Wordpress

args_item = "keyword,expect"

test_data,case_desc = YmlUtils("/test_data/wordpress/wordpress.yml").load_file
@allure.feature("博客文章内容")
@pytest.mark.parametrize(args_item, test_data, ids=case_desc)
class TestWordpress():
    """验证搜索的关键字"""
    @allure.story('验证查询')
    def test_getlist(self,keyword,expect):

        result = Wordpress().KeyWord().json()
        print(result)
        assert result[0]["id"] == expect["id"]
# -*- coding: utf-8 -*-
# @File  : test_smoke.py
# @Author: 岑苏岸
# @Date  : 2018/10/16
# @Desc  :



import pytest

@pytest.mark.smoke
class TestUserHandling_smoke(object):
    def test_login(self):
        pass
    def test_modification(self):
        assert 0

    def test_deletion(self):
        pass

def test_normal():
    pass
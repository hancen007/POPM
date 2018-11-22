# -*- coding: utf-8 -*-
# @File  : login_page.py
# @Author: 岑苏岸
# @Date  : 2018/10/25
# @Desc  :

from Pages.base_page import BasePage

class HomePage(BasePage):
    """首页"""

    url = ""

    def home_page(self,keyword):

        self.open()

        self.by_id("kw").send_keys(keyword)

        self.by_id("su").click()





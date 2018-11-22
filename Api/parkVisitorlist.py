# -*- coding: utf-8 -*-
# @File  : parkVisitorlist.py
# @Author: 岑苏岸
# @Date  : 2018/11/22
# @Desc  :


from common.Req import Req
from urllib.parse import urljoin
from collections import OrderedDict
import allure


@allure.feature("访客车辆模块")
class parkVistorlist(Req):
    """访客车辆"""
    """
    def __init__(self):
        super(parkVistorlist,self).__init__(*args,**kwargs)
        self.save_url = urljoin(self.host, "/mgr/park/parkVisitorlist/save.do")
        self.del_url = urljoin(self.host,"/mgr/park/parkVisitorlist/del.do")
        self.Visitorlist_url = urljoin(self.host,"/mgr/park/parkVisitorlist/getParkVisitorlist.do")
    """
    @allure.story("查询车辆信息")
    def getParklist(self,carNum):

        self.Visitorlist_url = urljoin(self.host,"/mgr/park/parkVisitorlist/getParkVisitorlist.do")

        """
        查询车辆信息
        :param carNum: 车牌号码
        :return:

        """
        from_data = OrderedDict()

        from_data["page"] = 1

        from_data[""] = 10

        from_data["carLicenseNumber"] = carNum

        re = self.get(self.Visitorlist_url,json=from_data)

        return re

    @allure.story("新建或者修改车辆信息")
    def save(self):
        """新建或者修改车辆信息"""
        hearders = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

        form_data ={

            "id": "",
            "carLicenseNumber": "CY009",
            "owner": "小苏",
            "ownerPhone": "13425131429",
            "visitReason": "pytest",
            "remark1": "",
            "remark2": "",
            "remark3": "",
            "specialCarTypeConfigId": "130",
            "visitFrom": "2018-11-22 00:00:00",
            "visitTo": "2018-11-23 00:00:00"
        }

        re = self.post(self.save_url,data=form_data,hearders=hearders)
        return re

    @allure.story("删除车辆信息")
    def car_del(self):
        """删除车辆信息"""

        self.del_url = urljoin(self.host,"/mgr/park/parkVisitorlist/del.do")

        hearders = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

        form_data ={

            "parkVisitorlistId": 146
        }

        re = self.post(self.del_url,data=form_data,hearders=hearders)
        return re


if __name__ == "__main__":

    pass










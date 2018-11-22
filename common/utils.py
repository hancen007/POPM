# -*- coding: utf-8 -*-
# @File  : utils.py
# @Author: 岑苏岸
# @Date  : 2018/10/15
# @Desc  :

import os
import yaml
from Config.Config import Config

class YmlUtils(object):

    def __init__(self,yamlPath):

        self.C = Config()
        self.all_data = []
        self.load_file = self.getData(yamlPath)

    def load_yaml(self,yamlPath):

        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = root_path+yamlPath

        f = open(full_path, 'r', encoding='UTF-8')
        cfg = f.read()
        self.all_data = yaml.load(cfg)  # 用load方法转字典

        return self.all_data

    def format_data(self):
        d = self.all_data
        item = []
        for i in range(0,len(d)):
            for value in d[i].values():
                child = []
                child.append(value['name'])
                child.append(value['send_data'])
                child.append(value['except'])
                item.append(tuple(child))
        return item



    def getData(self,yamlPath):

        d = self.load_yaml(yamlPath)
        array=[]  # 每条案例对应的测试数据信息
        desc=[]   # 每条案例对应的描述信息
        for i in range(0,len(d)):
            for value in d[i].values():
                childarray = []
                childarray.append(value['send_data'])
                childarray.append(value['except'])
                desc.append(value['desc'])
                array.append(tuple(childarray))
        return array,desc

    def single_data(self):
        pass
    #TODO 先占个位置


    def data_flow(self):
        """业务流数据"""
        pass



if __name__ == "__main__":
    test_data,case_desc = OperationYaml("/test_data/authInvitation/invitation_code.yml").load_file


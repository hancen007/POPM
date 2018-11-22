# -*- coding: utf-8 -*- 
# @File : config.py
# @Author: julia 
# @Date : 2018/9/13 
# @Desc : 读取config.ini 配置文件

from configparser import ConfigParser
import os
from sys import argv

class Config(object):

    VALUE_ENT_HOST = "host"
    VALUE_ENT_DB = "DB"
    VALUE_ENT_DB_PORT = "port"
    VALUE_ENT_DB_NAME = "db_name"

    def __init__(self,env="SIT"):

        self.CATEGORY = env
        self.config = ConfigParser()

        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path)
        self.host = self.config.get(self.CATEGORY,self.VALUE_ENT_HOST)
        self.db = self.config.get(self.CATEGORY,self.VALUE_ENT_DB)
        self.db_port = self.config.get(self.CATEGORY,self.VALUE_ENT_DB_PORT)
        self.db_name = self.config.get(self.CATEGORY,self.VALUE_ENT_DB_NAME)

    def get(self,title,value):
        return self.config.get(title, value)


if __name__=='__main__':
    C = Config()
    print(C.host)
    print(C.db)

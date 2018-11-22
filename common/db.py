
# -*- coding: utf-8 -*-
# @File : dbopertor.py
# @Author: julia
# @Date : 2018/10/12
# @Desc : 数据库操作
import pymysql.cursors
from Config.Config import *
import traceback
from common.logger import logger

class Db:
    def __init__(self):
        self.C = Config()

    def conection_db(self,sql):
        # 连接MySQL数据库
        connection = pymysql.connect(host=self.C.db,
                                     user=self.C.db_user,
                                     password=self.C.db_pwd,
                                     database=self.C.db_name,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        print(connection)

        # 使用 cursor() 方法创建一个游标对象 cursor
        issucess=False
        cursor = connection.cursor()
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交修改
            connection.commit()
            issucess=True
        except Exception:
            # 发生错误时回滚
            logger.info(traceback.print_exc())
            connection.rollback()
            issucess = False

        # 关闭数据库连接
        connection.close()
        return issucess

    def deletinfo_id(self,id):
        sql = "DELETE from t_ebill_ent_enterprise  where enterprise_id='"+id+"'"
        print(sql)
        return self.conection_db(sql)

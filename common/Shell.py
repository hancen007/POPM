# -*- coding: utf-8 -*-
# @File  : shell.py
# @Author: 岑苏岸
# @Date  : 2018/9/11
# @Desc  :



import subprocess


class Shell:
    """封装执行shell语句方法"""
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o


import time

from sys import argv



'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、用例运行策略，
*  -s 指定运行目录或文件，例: -s  ./test_case/ ,  -s  /test_case/test_demo.py
*  --html  指定测试报告目录及文件名。
*  --self-contained-html 表示创建独立的测试报告。
*  --reruns 3   指定用例失败重跑次数。
'''


import sys

import pytest

from common.Shell import Shell

test_dir = "."

if __name__ == "__main__":

    shell = Shell() # 构建一个cmd运行

    xml_report_path = "--junitxml=./reports/report.xml"

    html_report_path = "--html=./reports/report.html"

    allure_report = "--alluredir=allure-results"

    # 定义测试集
    #allure_list = '--allure_features=Home,Personal'

    args = ['-s','-v',test_dir, xml_report_path,html_report_path,allure_report]

    self_args = sys.argv[1:]

    pytest.main(args)

    """

    #cmd = 'allure generate %s -o %s' % ("allure-results", "allure-report")

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
    """

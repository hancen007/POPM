# -*- coding: utf-8 -*-
# @File  : test_yaml.py
# @Author: 岑苏岸
# @Date  : 2018/11/21
# @Desc  :
import pytest
def test_person(yaml_output):
    print("Test for %s" % yaml_output['test'])
    for person in yaml_output['persons']:
        assert person['age'] == 20, "I am %s" % person['name']


if __name__ == "__main__":
    pytest.main(["test_yaml.py","--yaml-file","yaml.yml"])
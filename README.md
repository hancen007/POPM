



# 框架能提供什么给我们
- 测试框架的设计,不是设计出来，重构出来
- 先写用例，用例多了维护不过来的时候，试着重构用例和相关内容
- 需求驱动，根据需求去增加框架功能
- 测试框架通用的需求
- 多人维护用例：模块化
- 用例运行策略：用例过滤器
- 回归测试策略：定时回归？根据代码库变化动态回归？
- 代码管理：多人同时维护代码，需要代码管理
- 测试报告：详细的报告/简略的报告/更加多媒体化的报告
- 通知的需求：短信/邮件/IM/语音电话
- 多语言支持：开发用java，测试用python，希望可以同时支持
- 精确定位错误：精准定位错误/错误一目了然
- 运行时问题：多台机器保证运行时环境一致
- 统一配置问题：框架的配置管理(约定大于配置)


## 框架目录：

- Project/:  系统名称
  - APi:/  接口测试基础类
  - Pages  UI测试基础类
  - Lib  依赖库
    -driver 浏览器驱动
  - report/： 存储测试结果
  - Log  执行日志
  - test_case/： 接口测试用例
  - test_data 测试数据YML
  - run_test:  执行接口测试入口

#### 插件
文件夹存放开发的公共方法；数据的初始化，动态生成数据；

#### run_test
批量执行测试案例的触发文件；

### YML测试数据数据

- #### 单用例测试的结构
~~~
- test:
    name: wordpress
    desc: 搜索-融资
    send_data:
      keyword: 融资
    except:
      id: 38
~~~


- #### 场景用例测试的结构
~~~
- config:
    name: "user management testset."
    request:
        headers:
            Content-Type: application/json
            device_sn: $device_sn
- test:
    name: api_001
    request:
        json:
            sign: ${get_sign($user_agent, $device_sn, $os_platform, $app_version)}
    extract:
        - token: content.token
    validate:
        - eq: [status_code, 200]
- test:
    name: api_002
    request:
        json:
            sign: ${get_sign($user_agent, $device_sn, $os_platform, $app_version)}
    extract:
        - token: content.token
    validate:
        - eq: [status_code, 200]
~~~
# 聊天机器人

sunday的聊天机器人模块

已经对接机器人:

1. [小i机器人](http://i.xiaoi.com/#)

# 安装插件

该插件依赖[sunday](https://github.com/pysunday/pysunday), 需要先安装sunday

执行sunday安装目录：`sunday_install pysunday/tools-imrebot`

# 机器人小i

## 试玩

克隆当前项目

执行命令：`python3 xiaoi.py`

## 外部使用

### 引入

```python
from sunday.tools.imrobot import Xiaoi
from sunday.tools.imrobot.xiaoi import Xiaoi
```

### 使用

```python
# 1. 创建机器人
xiaoi = Xiaoi()
# 2. 初始化小i
xiaoi.open()
# 3. 开启心跳, 返回关闭心跳方法
cancelHeat = xiaoi.heartbeat()
# 4. 与小i聊天
print(xiaoi.askText('你好'))
# 关闭心跳
cancelHeat()
```

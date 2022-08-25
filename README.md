# 聊天机器人

sunday的聊天机器人模块

已经对接机器人:

1. 小i机器人
2. 茉莉机器人
3. 青云客机器人

# 安装插件

该插件依赖[sunday](https://github.com/pysunday/pysunday), 需要先安装sunday

执行sunday安装目录：`sunday_install pysunday/tools-imrebot`

# 青云客机器人

# 茉莉机器人

## 试玩

执行命令：`python3 qingyunke.py`

## 外部使用

### 引入

```python
from sunday.tools.imrobot import Qingyunke
from sunday.tools.imrobot.qingyunke import Qingyunke
```

### 使用

```python
# 1. 创建机器人
qingyunke = Qingyunke()
# 4. 与机器人聊天
print(qingyunke.askText('你是谁'))
```

## 试玩

**需要从在茉莉机器人网站上先创建机器人，然后进入机器人页面取到Api-Secret和Api-Key，将`.env.example`改名为`.env`，修改env文件中的`MOLI_KEY`和`MOLI_SECRET`字段为刚刚获取的两个，然后执行聊天程序才能看到结果**

执行命令：`python3 moli.py`

## 外部使用

### 引入

```python
from sunday.tools.imrobot import Moli
from sunday.tools.imrobot.moli import Moli
```

### 使用

```python
# 1. 创建机器人
moli = Moli(key, secret)
# 4. 与机器人聊天
print(moli.askText('你是谁', '朋友id', '朋友姓名'))
```

# 小i机器人

## 试玩

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

# 机器人收集

1. [小i机器人](http://i.xiaoi.com/#)：速度快且完全免费，但是会有很多回不上话的情况
2. [春松机器人](https://docs.chatopera.com/products/chatbot-platform/overview.html)：首次注册赠送1万次调用
3. [微软小冰](https://www.xiaoice.com/)：现在已经不回话了
4. [青云客机器人](http://www.qingyunke.com/)：完全免费，且都能回上话，但是返回较慢
5. [图灵机器人](https://www.turingapi.com/)：一天只有一百条免费回复
6. [茉莉机器人](https://mlyai.com/)：个人开发维护，每天免费500条


# coding: utf-8
import json
import time
import re
import inquirer
from inquirer.themes import GreenPassion
from threading import Timer
from sunday.core import Logger, Fetch, exit
from sunday.tools.robot.config import processOpenResponse, processMsg
from pydash import pick, get

class Xiaoi():
    def __init__(self, isConsole=False):
        """
        isConsole: 标记是直接打印还是返回文本
        """
        self.logger = Logger('机器人小i').getLogger()
        self.fetch = Fetch()
        self.timer = None
        self.sessionData = None
        self.isConsole = isConsole
        self.stopHeart = None

    def getCurrentTime(self):
        # 当前时间戳
        return int(time.time() * 1000)

    def parseData(self, text):
        # 解析数据
        self.logger.debug('解析机器人返回数据: %s' % text)
        text = re.sub(r'(\n|\r)', '', text)
        data = re.findall(r'__webrobot_{1,2}process(?:Msg|OpenResponse)\((.*?)\);', text)
        return [json.loads(item) for item in data]

    def open(self):
        # 初始化并获取cookie和会话数据
        data = { "type": "open" }
        res = self.fetch.get(processOpenResponse % (json.dumps(data), self.getCurrentTime()))
        ans = self.parseData(res.text)
        self.sessionData = ans[0]
        self.logger.info('初始化成功, 会话信息：%s' % self.sessionData)

    def heartbeat(self, beatTime=50):
        # 会话心跳
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(beatTime, self.keepalive)
        self.timer.start()
        self.logger.info('开启会话心跳, 心跳时间：%d' % beatTime)
        def stop():
            self.timer.cancel()
            self.timer = None
            self.logger.info('关闭会话心跳')
        self.stopHeart = stop
        return stop

    def keepalive(self):
        # 保持会话为激活状态
        data = { "type": "keepalive" }
        self.fetch.get(processMsg % (json.dumps(data), self.getCurrentTime()))
        self.logger.info('会话激活成功')

    def sessionopen(self):
        # 打招呼
        data = { "type": "sessionopen" }
        data.update(pick(self.sessionData, ['robotId', 'userId', 'sessionId']))
        res = self.fetch.get(processMsg % (json.dumps(data), self.getCurrentTime()))
        return self.console(self.parseData(res.text))

    def askText(self, text):
        # 与机器人对话
        data = { "body": { "content": text }, "type": "txt" }
        data.update(pick(self.sessionData, ['robotId', 'userId', 'sessionId']))
        res = self.fetch.get(processMsg % (json.dumps(data), self.getCurrentTime()))
        return self.console(self.parseData(res.text))

    def console(self, ans):
        # 打印或返回机器人回话内容
        rets = []
        for item in ans:
            if item.get('type') == 'txt':
                content = get(item, 'body.content') or '哈哈 卡壳了'
                content = content.strip()
                if self.isConsole: print('机器人: %s' % content)
                rets.append(content)
        if not self.isConsole:
            self.logger.info('机器人回话: %s' % rets)
            return '\n'.join(rets)
        return ''

    def chat(self):
        while True:
            answers = inquirer.prompt([inquirer.Text('question', message="请输入")], theme=GreenPassion())
            question = answers.get('question')
            if question in ['Q', 'quit', 'exit']:
                if self.stopHeart: self.stopHeart()
                exit('主动退出')
            elif question:
                self.askText(answers['question'])


if __name__ == "__main__":
    robot = Xiaoi(True)
    robot.open()
    robot.heartbeat()
    robot.sessionopen()
    robot.chat()


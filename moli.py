# coding: utf-8
import json
import re
import os
import inquirer
from inquirer.themes import GreenPassion
from sunday.core import Logger, Fetch, exit, enver
from sunday.tools.imrobot.config import moli_reply
from pydash import get

class Moli():
    def __init__(self, isConsole=False, key=None, secret=None):
        """
        isConsole: 标记是直接打印还是返回文本
        """
        self.isConsole = isConsole
        self.logger = Logger('茉莉机器人').getLogger()
        self.fetch = self.getFetch(key, secret)

    def getFetch(self, key, secret):
        if self.isConsole:
            fetch = Fetch()
            pwd = os.path.dirname(os.path.abspath(__file__))
            (getenv, setenv, getfile) = enver(os.path.join(pwd, '.env'))
            key = getenv('MOLI_KEY')
            secret = getenv('MOLI_SECRET')
        fetch.add_header({
            'Content-Type': 'application/json;charset=UTF-8',
            'Api-Key': key,
            'Api-Secret': secret
        })
        return fetch

    def askText(self, text, userid, username):
        # 与机器人对话
        data = {
                'content': text,
                'type': 1,
                'from': userid,
                'fromName': username
                }
        res = self.fetch.post(moli_reply, data=json.dumps(data))
        try:
            resjson = res.json()
        except Exception as e:
            resjson = {}
        self.logger.info(resjson)
        return self.console(resjson.get('data') or [])

    def console(self, ans):
        # 打印或返回机器人回话内容
        rets = []
        for item in ans:
            if item.get('typed') == 1:
                content = get(item, 'content') or '哈哈 卡壳了'
                content = content.strip()
                if self.isConsole: print('机器人: %s' % content)
                # 当机器人回答不上来就会返回defaultReply
                if content != 'defaultReply': rets.append(content)
        if not self.isConsole:
            if len(rets) > 0: rets.append('--来自茉莉机器人')
            self.logger.info('机器人回话: %s' % rets)
            return '\n'.join(rets)
        return ''

    def chat(self):
        while True:
            answers = inquirer.prompt([inquirer.Text('question', message="请输入")], theme=GreenPassion())
            question = answers.get('question')
            if question in ['Q', 'quit', 'exit']:
                exit('主动退出')
            elif question:
                self.askText(answers['question'], '唯一id', '名称')


if __name__ == "__main__":
    robot = Moli(True)
    robot.chat()


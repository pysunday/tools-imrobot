# coding: utf-8
import json
import re
import inquirer
from inquirer.themes import GreenPassion
from sunday.core import Logger, Fetch, exit
from sunday.tools.imrobot.config import qingyunke_api
from pydash import get

class Qingyunke():
    def __init__(self, isConsole=False):
        """
        isConsole: 标记是直接打印还是返回文本
        """
        self.logger = Logger('青云客机器人').getLogger()
        self.fetch = Fetch()
        self.isConsole = isConsole

    def askText(self, text):
        # 与机器人对话
        res = self.fetch.get(qingyunke_api % text)
        try:
            resjson = res.json()
        except Exception as e:
            resjson = {}
        self.logger.info(resjson)
        return self.console([resjson])

    def console(self, ans):
        # 打印或返回机器人回话内容
        rets = []
        for item in ans:
            if item.get('result') == 0:
                content = get(item, 'content') or '哈哈 卡壳了'
                content = content.strip().replace('{br}', '\n')
                if self.isConsole: print('机器人: %s' % content)
                # 当机器人回答不上来就会返回defaultReply
                if content != 'defaultReply': rets.append(content)
        if not self.isConsole:
            if len(rets) > 0: rets.append('--来青云客机器人')
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
                self.askText(answers['question'])


if __name__ == "__main__":
    robot = Qingyunke(True)
    robot.chat()


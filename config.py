# coding: utf-8

baseUrl = 'http://i.xiaoi.com/robot/webrobot'

# 初始化会话
processOpenResponse = baseUrl + '?&callback=__webrobot__processOpenResponse&data=%s&ts=%d'

# 发送事件
processMsg = baseUrl + '?&callback=__webrobot_processMsg&data=%s&ts=%d'

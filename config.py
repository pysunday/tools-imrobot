# coding: utf-8

baseUrl = 'http://i.xiaoi.com/robot/webrobot'

# 初始化会话
processOpenResponse = baseUrl + '?&callback=__webrobot__processOpenResponse&data=%s&ts=%d'

# 发送事件
processMsg = baseUrl + '?&callback=__webrobot_processMsg&data=%s&ts=%d'

# 茉莉机器人请求接口
moli_reply = 'https://api.mlyai.com/reply'

# 青云客机器人请求接口
qingyunke_api = 'https://api.qingyunke.com/api.php?key=free&appid=0&msg=%s'

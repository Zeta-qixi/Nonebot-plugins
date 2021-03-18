import nonebot
from nonebot import on_command, CommandSession, Message
from nonebot import on_natural_language, NLPSession, IntentCommand
import os
import sys
import random
import time
import re
from aiocqhttp.exceptions import ActionFailed

#变量
path_tome ='data/chat/tome.txt'
path_nm ='data/chat/nm.txt'
path_ft ='data/chat/ft.txt'
path = 'data/chat/data.txt'
bot = nonebot.get_bot()
master = bot.config.MASTER
me = '894296015'
      
# -global- #
trigger = {}
lock = 0
data_tome = []
data_nm = []
data_ft = []
data = {}
ptalk = {}

with open(path) as f:
    for line in f.readlines():
        k = line.split()
        data[k[0]] = k[1:]
        
'''
1.判定内容
    判定是否@ （属于msg
        判定是否master
            to do 
'''

@bot.on_message('group')
async def chat(context):
    message = context['raw_message'].strip()
    group_id = context['group_id']
    user_id = context['user_id']
    
    global ptalk
      #第一次对话初始化变量
    ptalk.setdefault(group_id,0.3)
    trigger.setdefault(group_id,' ')

'''
4个if判定：
1. 判断关键词 
2. 对字符<2 用精准匹配
3. 是否已触发
4. 回复概率
'''
    for i in data:
        if i in message :
            if len(i) > 2 or i == message:
                if trigger[group_id] != i :
                    if random.random() < ptalk[group_id]:
                        await bot.send_group_msg(group_id=group_id,message=random.choice(data[i]))
                        trigger[group_id] = i
                        return 0



####--- 下面是 Command-- ####

@on_command('setP', aliases=('setp',),only_to_me=True)
async def setP(session: CommandSession):
    group_id = session.ctx['group_id']
    user_id=session.ctx['user_id']
    if user_id in master:
        msg=session.current_arg.strip()
        global ptalk
        if not msg:
            msg = session.get('message', prompt='设置概率~ \n--这是范围[0,1]')
        ptalk[group_id] = float(msg)
        await session.send(message= f'现在的回复率为：{ptalk[group_id]}')
    else :
        await session.send(message= '不是master， 爬')




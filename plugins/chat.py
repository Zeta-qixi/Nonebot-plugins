import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import json
import random
import time
import re
from aiocqhttp.exceptions import ActionFailed

bot = nonebot.get_bot()
master = bot.config.MASTER
   
# -global- #
trigger = {}
lock = 0
data = {} 
ptalk = {} #回复率


gpath =os.path.dirname(__file__)
#语料库地址
path = gpath +'/data.json'
with open(path) as f:
    data = json.load(f)

@bot.on_message('group')
async def chat(context):
    message = context['raw_message'].strip()
    group_id = context['group_id']
    user_id = context['user_id']
    
    global ptalk
    ptalk.setdefault(group_id,0.1)
    trigger.setdefault(group_id,' ')

    for i in data:
        if i in message and user_id != master[0] :
            #长度大于3模糊匹配
            if len(i) > 3 or i == message:
                if trigger[group_id] != i :
                    if random.random() < ptalk[group_id] :
                        time.sleep(random.randrange(5))
                        await bot.send_group_msg(group_id=group_id,message=random.choice(data[i]))
                        trigger[group_id] = i
                        return 0

'''
下面是 Command

'''

#添加语录
@on_command('set', aliases=('设置',),only_to_me=True)
async def setword(session: CommandSession):

    comman = session.ctx['raw_message'].split()
    try:
        global data
        #comman[0] 是 'set'
        keys = comman[1]
        #录入库
        if keys not in data:
            data.setdefault(keys,[])
            data [keys] = comman[2:]
        else:  
            for i in comman[2:]:
                if i not in data[keys]: 
                    data[keys].append(i)
        
        with open(path, 'w+') as f :
            tojson = json.dumps(data,sort_keys=True, ensure_ascii=False, indent=4,separators=(',',': '))
            f.write(tojson)

        text = ''
        for i in comman[2:]:    
            text = text + i + ' '   
        await session.send(message= f'已保存{keys}:{text}')
    except:
        await session.send(message= f'失败了QAQ')

#设置回复率
@on_command('setP', aliases=('setp',),only_to_me=True)
async def setP(session: CommandSession):
    group_id = session.ctx['group_id']
    user_id=session.ctx['user_id']
    if user_id == master[0]:
        msg=session.current_arg.strip()
        global ptalk
        if not msg:
            msg = session.get('message', prompt='设置概率~ \n--范围[0,1]')
        ptalk[group_id] = float(msg)
        await session.send(message= f'你群现在的回复率为：{ptalk[group_id]}')
    else :
        await session.send(message= '?')


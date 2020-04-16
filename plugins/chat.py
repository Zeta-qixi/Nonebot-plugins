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
path_nm ='data/chat/nm.txt'
path_ft ='data/chat/ft.txt'
path = 'data/chat/data.txt'
bot = nonebot.get_bot()
master = bot.config.MASTER
me = '894296015'
      
# -global- #
latest_message = {}
My_repeat_time = {}
latest_message_user = {}
repeat_times = {}
repeat_message = {}
lock = 0
data_nm = []
data_ft = []
data = {}
ptalk = {}
with open(path_nm) as f:
    for line in f.readlines():
        data_nm.append(line.strip())
with open(path_ft) as f:
    for line in f.readlines():
        data_ft.append(line.strip())
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
    ptalk.setdefault(group_id,0.3)

    if '老婆' in message and me in message :
        if user_id == master[0]:
            msg_list=['(〃ω〃)', '(///▽///)']
            await bot.send_group_msg(group_id=group_id,message=random.choice(msg_list))
        elif random.random() > 0.5:
            msg_list=['?', '？？', '[CQ:face,id=32]']
            await bot.send_group_msg(group_id=group_id,message=random.choice(msg_list))

    


    for i in data:
        if i in message and user_id != master[0] :
            if len(i) >= 2 or i == message:
                if random.random() < ptalk[group_id] :
                    await bot.send_group_msg(group_id=group_id,message=random.choice(data[i]))
                    return 0


    if me in message :
        for i in data_nm :
            if i in message:

                if random.random() < 0.95:
                    await bot.send_group_msg(group_id=group_id,message=random.choice(data_ft))
                    return 0
                else :
                    await bot.send_group_msg(group_id=group_id,message='[CQ:face,id=146]')
                    await bot.send_group_msg(group_id=group_id,message=f'[CQ:at,qq={user_id}] 今天的人品值是：0')
                    return 0
        tome = ['( ^ω^ )', '?', '¿', '......','(･_･;', '呵呵', '[CQ:face,id=13][CQ:face,id=13][CQ:face,id=13]']
        await bot.send_group_msg(group_id=group_id,message=random.choice(tome))



    

####--- 下面是 Command-- ####
@on_command('set', aliases=('设置',),only_to_me=True)
async def setword(session: CommandSession):
    global lock
    while lock >= 1:
        await time.sleep(1)
    lock = 1
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
        text = ''
        for i in comman[2:]:    
            text = text + i + ' '   
        await session.send(message= f'已保存{keys}:{text}')
    except:
        await session.send(message= f'失败了，可以找master在后台导入')
    lock = 0

@on_command('save', aliases=('保存',),only_to_me=True)
async def saveword(session: CommandSession):
        with open(path, 'w+') as f :
            for i in data:
                f.write(f'{i} ')
                words = ''
                for ii in data[i]:
                    words = words + ii +' '

                f.write(f'{words}\n')
        await session.send(message= 'ok~')


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
        await session.send(message= f'你群现在的回复率为：{ptalk[group_id]}')
    else :
        await session.send(message= '不是master， 爬')


@on_command('addmaster', only_to_me=True)
async def addM(session: CommandSession):

    user_id=session.ctx['user_id']
    global master
    if user_id == master[0]:
        ##todo
        msg=session.current_arg.strip()
        if not msg:
            msg = session.get('message', prompt='誰ですか~')
        
        p=r'\d+'
        qq=re.findall(p,msg)
        master.append(int(qq[0]))
        await session.send(message= f'添加新master：{msg}')
    else :
        await session.send(message= '?')



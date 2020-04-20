import nonebot
from nonebot import on_command, CommandSession, Message
import os

import random
import time
from aiocqhttp.exceptions import ActionFailed

#变量
bot = nonebot.get_bot()
master = bot.config.MASTER
me = '894296015'
      
# -global- #
latest_message = {}
My_repeat_time = {}
latest_message_user = {}
repeat_times = {}
repeat_message = {}
extras = {
    '草' : ['草']
    ,"人？" : ['人？','tql']
}

@bot.on_message('group')
async def chat(context):
    message = context['raw_message'].strip()
    group_id = context['group_id']
    user_id = context['user_id']
#复读判定
    #启动后 群第一次信息 创建字典
    global repeat_times
    global latest_message
    global latest_message_user
    global repeat_message

    #特殊处理
    if 'jrrp' in message:
        return 
    for i in extras :
        if message == i and repeat_message[group_id] != message and random.random()<0.7:
            await bot.send_group_msg(group_id=group_id,message=random.choice(extras[i]))
            repeat_message[group_id] = message

        #第一次消息
    if group_id not in repeat_times:
        repeat_times[group_id] = 1
        repeat_message[group_id] = ''
    else:
        #判定是否为复读
        if latest_message[group_id] == message :
            if latest_message_user[group_id] != user_id:
                repeat_times[group_id] +=1
        else :
            repeat_times[group_id] = 1 

    
    #发动
    if (repeat_times[group_id] - 1) * 0.2 > random.random() :
        if '能' in message or 'zdn' in message:
            await bot.send_group_msg(group_id=group_id,message='打断(･_･;')
        elif repeat_message[group_id] != message :
                await bot.send_group_msg(group_id=group_id,message=message)
                repeat_message[group_id] = message

    latest_message[group_id] = message
    latest_message_user[group_id] = user_id
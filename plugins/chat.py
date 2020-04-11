import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import random
import time
from aiocqhttp.exceptions import ActionFailed

root=os.path.join(os.path.dirname(__file__),'data','chat')
path = 'data/chat/'
path_nm ='data/chat/nm.txt'
path_ft ='data/chat/ft.txt'
bot = nonebot.get_bot()
master = bot.config.MASTER
me = '894296015'

#变量


#------------
latest_message = {}
My_repeat_time = {}
latest_message_user = {}
repeat_times = {}
repeat_message = {}

#读取语言库
try:
    data = []
    with open(path_nm) as f:
        for line in f.readlines():
            data.append(line)
    ft = []
    with open(path_nm) as f:
        for line in f.readlines():
            data.append(line)
    print('导入成功')
except:
    print('没打开文件')


'''
接受到群消息
1.获取消息信息（id msg time ...
2.判定是msg包含字段
3.判定是否复读
'''

    



@bot.on_message('group')
async def ycm(context):
    message = context['raw_message'].strip()
    group_id = context['group_id']
    user_id = context['user_id']
#复读判定
    if group_id not in repeat_times:
        repeat_times[group_id] = 1
        My_repeat_time[group_id] = time.time()
    else:
        if latest_message[group_id] == message :
            if latest_message_user != user_id:
                repeat_times[group_id] +=1
        else :
            repeat_times[group_id] = 1
    if (repeat_times[group_id] - 1) * 0.2 > random.random() :
        if  repeat_message[group_id] != message :
            await bot.send_group_msg(group_id=group_id,message=message)
            repeat_message[group_id] = message

    latest_message[group_id] = message
    latest_message_user[group_id] = user_id


    if 'ycm' == message:
        msg_list=['myc', '无', 'myc，爬', 'https://bandoristation.com/']
        if user_id == master[0] :
            await bot.send_group_msg(group_id=group_id,message='^_^' + msg_list[3])
        else:
            await bot.send_group_msg(group_id=group_id,message=random.choice(msg_list))

    for i in data:
        if i in message :
            if me in message :
                await bot.send_group_msg(group_id=group_id,message=random.choice(ft))
            elif user_id != master[0] and random.random() > 0.7:
                await bot.send_group_msg(group_id=group_id,message= i +' ( ^ω^ )')








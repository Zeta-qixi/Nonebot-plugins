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

-------------------------
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
#复读判定
    #启动后 群第一次信息 创建字典
    if group_id not in repeat_times:
        repeat_times[group_id] = 1
    else:
        if latest_message[group_id] == message :
            if latest_message_user != user_id:
                repeat_times[group_id] +=1
        else :
            repeat_times[group_id] = 1 
    #发动复读
    if (repeat_times[group_id] - 1) * 0.2 > random.random() :
        if  repeat_message[group_id] != message :
                await bot.send_group_msg(group_id=group_id,message=message)
                repeat_message[group_id] = message

    latest_message[group_id] = message
    latest_message_user[group_id] = user_id


    if 'ycm' in message :
        msg_list=['myc', '无', 'myc，爬', 'https://bandoristation.com/']
        if user_id == master[0] :
            await bot.send_group_msg(group_id=group_id,message='^_^' + msg_list[3])
        else:
            await bot.send_group_msg(group_id=group_id,message=random.choice(msg_list))


    elif '老婆' in message and me in message :
        if user_id in master:



    for i in data:
        if i in message :
            if me in message :
                await bot.send_group_msg(group_id=group_id,message=random.choice(ft))
                break
            elif user_id in master and random.random() > 0.7:
                await bot.send_group_msg(group_id=group_id,message= random.choice(ft) +' ( ^ω^ )')
                break








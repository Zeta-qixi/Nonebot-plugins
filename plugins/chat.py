import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import random
import time
from aiocqhttp.exceptions import ActionFailed
sys.path.append(os.path.join(os.path.dirname(__file__), 'data','chat'))
import ycm

#变量

bot = nonebot.get_bot()
path_nm ='data/chat/nm.txt'
path_ft ='data/chat/ft.txt'
master = bot.config.MASTER
me = '894296015'
      
# -global- #
latest_message = {}
My_repeat_time = {}
latest_message_user = {}
repeat_times = {}
repeat_message = {}
latest_ycm = 0

#读取语言库
'''
设置 语言库 设置qq添加
'''

data_nm = []
data_ft = []


with open(path_nm) as f:
    for line in f.readlines():
        data_nm.append(line.strip())
with open(path_ft) as f:
    for line in f.readlines():
        data_ft.append(line.strip())
            



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
    global repeat_times
    global latest_message
    global latest_message_user
    global repeat_message

    if group_id not in repeat_times:
        repeat_times[group_id] = 1
    else:
        if latest_message[group_id] == message :
            if latest_message_user != user_id:
                repeat_times[group_id] +=1
        else :
            repeat_times[group_id] = 1 
    #发动
    if (repeat_times[group_id] - 1) * 0.2 > random.random() :
        if '能' in message or 'zdn' in message:
            await bot.send_group_msg(group_id=group_id,message='打断(･_･;')
        elif  repeat_message[group_id] != message :
                await bot.send_group_msg(group_id=group_id,message=message)
                repeat_message[group_id] = message

    latest_message[group_id] = message
    latest_message_user[group_id] = user_id


    if 'ycm' in message :
        global latest_ycm
        if time.time() - latest_ycm > 30:
            await bot.send_group_msg(group_id=group_id,message='现在爬')
            latest_ycm = time.time()
            room = []
            room = ycm.Read_room()
            msg_list=['myc', '无']
            if not room :
                await bot.send_group_msg(group_id=group_id,message=random.choice(msg_list))
            else :
                text = ''
                for i in room:
                    text = text + i +'\n\n'
                    await bot.send_group_msg(group_id=group_id,message=text)
        else :
            await bot.send_group_msg(group_id=group_id,message='爬累了 （cd中）')

    elif '老婆' in message and me in message :
        if user_id == master[0]:
            msg_list=['(〃ω〃)', '(///▽///)']
            await bot.send_group_msg(group_id=group_id,message=random.choice(msg_list))
        elif random.random() > 0.5:
            msg_list=['?', '？？', '[CQ:face,id=32]']
            await bot.send_group_msg(group_id=group_id,message=random.choice(msg_list))

    
    for i in ['睡觉', '歇了', '睡了', '眠了']:
        if i in message:
            if user_id in master:
                await bot.send_group_msg(group_id=group_id,message=f'[CQ:at,qq={user_id}] 晚安~ mua~')
                break
            else:
                await bot.send_group_msg(group_id=group_id,message=' 晚安啦hhh')
                break

    for i in data_nm:
        if i in message :
            try:
                if "谁是" in message:
                    await bot.send_group_msg(group_id=group_id,message=f'[CQ:at,qq=1109144843] 是你群{i}')
                    break
                elif me in message :
                    if random.random() > 0.10:
                        await bot.send_group_msg(group_id=group_id,message=random.choice(data_ft))
                    else :
                        await bot.send_group_msg(group_id=group_id,message='[CQ:face,id=146]')
                        await bot.send_group_msg(group_id=group_id,message=f'[CQ:at,qq={user_id}] 今天的人品值是：0')
                    break
                elif user_id not in master and random.random() > 0.7:
                    await bot.send_group_msg(group_id=group_id,message= random.choice(data_ft) +' ( ^ω^ )')
                    break
            except:
                await bot.send_private_msg(user_id=master[0], message='出错了')
    

        







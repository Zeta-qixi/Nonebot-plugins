
import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import random
import time
from aiocqhttp.exceptions import ActionFailed
path ='data/jrrp.txt'

def RP(a):
    try:
        data = []
        with open(path) as f:
            for line in f.readlines():
                eachdata = line.split()
                data.append(eachdata)
        for i in range(len(data)):
            if a == data[i][0]:
                return(data[i][1], 0)
        rd = random.randrange(101)
    except:
        return(-1, -1)
        
    with open(path,'a+') as f:
        f.write(a+' '+str(rd)+'\n')
    return(rd, 1)


bot = nonebot.get_bot()
master = bot.config.MASTER
@on_command('jrrp', only_to_me=False)
async def jrrp(session: CommandSession):
    user_id=session.ctx['user_id']
    rp, ft= RP(str(user_id))
    if rp == -1 :
        await session.send(message='没有人品（找不到文件~')
    else:
        await session.send(message=f'[CQ:at,qq={user_id}] 今天的人品值是：{rp}')
    if ft == 1:
        try:
            
            if int(rp) <10:
                time.sleep(2)
                talk = random.choice(['不愧是您.jpg', '残念','[CQ:face,id=20]'])
                await session.send(message=talk)
           
            elif int(rp) == 100:
                newrp = random.random() + 99.5
                await session.send(message='~~：' + newrp)
                await session.send(message=f'[CQ:at,qq={user_id}] 赶紧十连！！')

            elif int(rp) >= 95:
                talk = random.choice(['( ´ ▽ ` )ﾉ', '该抽卡了','建议抽卡'])
                await session.send(message=talk)

            else :
                if random.random() > 0.8:
                    talk = random.choice(['......', '(^_^)','ええ、'])
                    await session.send(message=talk)
        except:
            await session.send(message=f'[CQ:at,qq={master[0]}] 好像出问题了 (･_･;')


##0点清空文件
@nonebot.scheduler.scheduled_job('cron', hour='0', minute='0', second='0', misfire_grace_time=60) # = UTC+8 1445
async def clean():
    with open(path,'w+') as f:
        f.write('0'+' '+'0'+'\n')

##命令清空
@on_command('clean', only_to_me=False)
async def clean2(session: CommandSession):
    user_id=session.ctx['user_id']
    if user_id in master:
        try:
            with open(path,'w+') as f:
                f.write('0'+' '+'0'+'\n')
            await session.send(message='clean！')
        except:
            pass                                                                       
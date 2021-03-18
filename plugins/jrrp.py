import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import random
import time
from . import nickname
from aiocqhttp.exceptions import ActionFailed


bot = nonebot.get_bot()
master = bot.config.MASTER 

class rp:
    def __init__(self):
        self.rp = {}

    def RP(self,num):
        if num in self.rp.keys():
            return self.rp[num]
        else:
            if num == master[0]:
               self.rp[num] = random.randrange(51) + 50 #?
            else:
                self.rp[num] = random.randrange(101) 
            return self.rp[num]

rpbot = rp()

@on_command('jrrp', only_to_me=False)
async def jrrp(session: CommandSession):
    user_id = user_id=session.ctx['user_id']
    jrrp = rpbot.RP(user_id)
    if nickname.my_name(user_id):
        await session.send(message=f'{nickname.my_name(user_id)} 今天的人品值是：{jrrp}')
    else:
        await session.send(message=f'[CQ:at,qq={user_id}] 今天的人品值是：{jrrp}')

@nonebot.scheduler.scheduled_job('cron', hour='0', minute='0', second='0', misfire_grace_time=60) # = UTC+8 1445
async def clean():
    rpbot.rp = {}

@on_command('clean', only_to_me=True)
async def clean2(session: CommandSession):
    user_id=session.ctx['user_id']
    if user_id == master[0]:
        try:
            rpbot.rp = {}
            await session.send(message='clean！')
        except:
            pass    

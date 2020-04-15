import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import random
import time
from aiocqhttp.exceptions import ActionFailed


#---------------------------
path = 'data/chat/data.txt'

#---------------------
@on_command('log', only_to_me=True)
async def log(session: CommandSession):
    with open('log.txt',encoding='UTF-8') as f:  #no r
        lines = f.readlines()  # 读取所有行
        data = ''
        for i in lines[-100:]:
            if 'meta_event.heartbeat' not in i:
                data = data + (i.split('] ')[-1])
        await session.send(message=data)


@on_command('showdict', only_to_me=True)
async def showdict(session: CommandSession):
    
    with open(path) as f:  #no r
        text = ''
        i = 1
        for line in f.readlines():
            words = line.split()
            text = text + f'{i}.{words[0]}: {words[1:]}\n'
            i = i+1
        
        await session.send(message=text)
            
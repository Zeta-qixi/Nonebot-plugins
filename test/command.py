import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import random
import time
from aiocqhttp.exceptions import ActionFailed

root=os.path.join(os.path.dirname(__file__),'data','chat')
path = 'data/chat/'

bot = nonebot.get_bot()
master = bot.config.MASTER
me = '894296015'
tsugu = 2990556280
group_id = ''
'''
bot 随便加个有tsugu的群， 
'''
@bot.on_message('group')
async def chat(context):
    message = context['raw_message'].strip()
    group_id = context['group_id']

    if 'ycm' in message :
        await bot.send_group_msg(group_id=group_id,message='开始请求')
        try:
            await bot.send_private_msg(user_id= tsugu, message='ycm')

        except :
            await bot.send_group_msg(group_id=group_id,message='失败')

@bot.on_message('private')
async def call_tsugu(context):

    user_id = context['user_id']
    url = context['message'][-1]['data']['url']

    if user_id == tsugu :
        await bot.send_group_msg(group_id=group_id,message=url)
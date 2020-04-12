import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
from aiocqhttp.exceptions import ActionFailed

bot = nonebot.get_bot()
master = bot.config.MASTER

#@on_natural_language({'天气'}, only_to_me=False) 自然语言 { } is a set

tlist = ['t1', 't2']
@on_command('test', aliases=tlist ,only_to_me=False)
async def Url_Test2(session: CommandSession):
    user_id=session.ctx['user_id']
    if user_id in master:
        await session.send(message='[CQ:face,id=20]')
        await session.send(message='123')

@bot.on_message('group')
async def chat(context):
    message = context['raw_message'].strip()
    group_id = context['group_id']
    user_id = context['user_id']

    if user_id in master :
        await bot.send_group_msg(group_id=group_id,message=' ( ^ω^ )')
        await bot.send_group_msg(group_id=group_id,message=message)
        print('i say: ' + message)

    if '894296015' in message:
        await bot.send_group_msg(group_id=group_id,message='is me')


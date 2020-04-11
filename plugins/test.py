import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
from aiocqhttp.exceptions import ActionFailed

bot = nonebot.get_bot()
master = bot.config.MASTER

#@on_natural_language({'天气'}, only_to_me=False) 自然语言


@on_command('test', only_to_me=True)
async def Url_Test2(session: CommandSession):
    user_id=session.ctx['user_id']
    if user_id in master:
        await session.send(message='[CQ:face,id=20]')
        await session.send(message='123')
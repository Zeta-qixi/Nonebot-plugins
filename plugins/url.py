import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
from aiocqhttp.exceptions import ActionFailed
bot = nonebot.get_bot()
master = bot.config.MASTER

@on_command('音游地图',aliases=('引诱地图',), only_to_me=False)
async def yyMap(session: CommandSession):
    await session.send(message='https://map.bemanicn.com/')

@on_command('搜图',aliases=('查图',), only_to_me=False)
async def FindPicture(session: CommandSession):
    await session.send(message='https://saucenao.com/testing/')


@on_command('课程',only_to_me=False)
async def MyClass(session: CommandSession):
    await session.send(message='https://ke.qq.com/webcourse/index.html?cid=1604111&term_id=101703432&lite=1&from=800021724')

@on_command('作业',only_to_me=False)
async def MyHomework(session: CommandSession):
    await session.send(message='http://www.icourse163.org/spoc/course/GDY250-1452793196')

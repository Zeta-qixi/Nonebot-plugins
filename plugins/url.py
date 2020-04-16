import nonebot
from nonebot import on_command, CommandSession, Message
import os
import sys
import time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))
import ycm
from aiocqhttp.exceptions import ActionFailed
bot = nonebot.get_bot()
master = bot.config.MASTER
latest_ycm = 0
setycm = 1
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

@on_command('ycm',aliases=('有车吗',), only_to_me=False)
async def find_room(session: CommandSession):
    global latest_ycm
    global setycm
    if setycm == 0 :
        await session.send(message='......')
    elif time.time() - latest_ycm > 60 :
        await session.send(message='...')
        latest_ycm = time.time()
        room = []
        room = ycm.Read_room()
        msg_list=['myc', '无','窝屎就有', '地平线就有', 'gta就有']
        if not room :
            await session.send(message=random.choice(msg_list))
        else :
            text = ''
            for i in room:
                text = text + i +'\n'
            await session.send(message=text)
    else :
        await session.send(message='自己看 https://bandoristation.com/')



@on_command('setycm', only_to_me=True)
async def set_ycm(session: CommandSession):
    global setycm
    if setycm :
        setycm = 0
    else:
        setycm = 1
    status = ['关', '开']
    await session.send(message=f'功能ycm状态：{status[setycm]}')


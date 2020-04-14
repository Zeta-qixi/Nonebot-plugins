# -*- coding:utf-8 -*-
from datetime import datetime
import nonebot

bot = nonebot.get_bot()
master = 1019289695
#使用计划任务模块之前请在命令行执行pip install nonebot[scheduler]
#可自行添加不发送定时消息的群列表
DZJJ = 576875663
@nonebot.scheduler.scheduled_job('cron', hour='8', minute='0', second='0', misfire_grace_time=60) # = UTC+8 1445
async def a8():
     await bot.send_group_msg(group_id=DZJJ, message='[CQ:at,qq=1109144843] 美好的一天从清体开始，赶紧qqt！!')

@nonebot.scheduler.scheduled_job('cron', hour='15', minute='0', second='0', misfire_grace_time=60) # = UTC+8 1445
async def a17():
     await bot.send_group_msg(group_id=DZJJ, message='[CQ:at,qq=1109144843] 体力满了，该清清体了！！')

@nonebot.scheduler.scheduled_job('cron', hour='22', minute='0', second='0', misfire_grace_time=60) # = UTC+8 1445
async def a22():
     await bot.send_group_msg(group_id=DZJJ, message='[CQ:at,qq=1109144843] 现在日本时间23点，太君 睡觉前先清清体！!')

##
@nonebot.scheduler.scheduled_job('cron', hour='22', minute='0', second='0', misfire_grace_time=60) # = UTC+8 1445
async def m22():
    await bot.send_private_msg(user_id=master, message='上个号')

@nonebot.scheduler.scheduled_job('cron', hour='11', minute='0', second='0', misfire_grace_time=60) # = UTC+8 1445
async def m11():
    await bot.send_private_msg(user_id=master, message='打卡')



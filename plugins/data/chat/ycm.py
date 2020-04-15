from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')#解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x3000') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

def Read_room(): 
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://bandoristation.com/')
    time.sleep(0.3)
    text=driver.page_source
    driver.quit()
    t2 = text.split('<div class="content">')[-1].split('<div class="home-side-button-container">')[0]
    t3 = t2.split('<span class="room-number-data-raw-msg">')[1:]
    room = []
    for i in t3:
        room.append(i.split('<')[0])
    return room
    
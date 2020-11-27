# -*- coding: utf-8 -*-
# @Auth      :monijuan
# @Time      :2020/11/26 16:02
# @CSDN      :https://blog.csdn.net/qq_34451909
# @File      :core.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import map
import control
import move

def start():
    mapsize = 4                 # 定义尺寸4*4
    MAP = map.Map(mapsize)      # 初始化【面板】
    MOVE = move.Move(mapsize)   # 初始化【移动面板的工具】
    CONTROL = control.Control() # 初始化【获取键盘的工具】

    # MAP.setTestMap_1()  # 自定义初始化，用于测试
    MAP.printMap()      # 显示初始面板
    GAMEOVER = False
    while GAMEOVER==False:  # 循环主体
        dir = CONTROL.getdir()              # 获取键盘方向
        ISCHANGE = MOVE.movemap(MAP,dir)    # 根据方向执行操作，返回【面板】是否有变化
        if ISCHANGE:                        # 如果【面板】有变化
            LASTONE = MAP.addone()          #   肯定可以添加，返回是不是最后一个空
            MAP.printMap()                  #   打印面板
            # 如果填充是最后一个空，则判断是否不能再操作
            GAMEOVER = MAP.isend() if LASTONE else False
    print('Game over!')

if __name__ == '__main__':
    start()

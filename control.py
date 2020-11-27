# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 16:17
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :control.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
class Control
    提供方法：获取键盘按键
"""
from pynput.keyboard import Key,Listener
from direction import Direction

class Control:
    def __init__(self):
        self.dir_ = None # dir一定要用成员变量，不然没办法在on_press中修改

    def getdir(self):
        self.dir_ = None    # 如果是不是上下左右则返回None
        def on_press(key):
            if key == Key.up:self.dir_ = Direction.UP
            elif key == Key.down:self.dir_ = Direction.DOWN
            elif key == Key.left:self.dir_ = Direction.LEFT
            elif key == Key.right:self.dir_ = Direction.RIGHT
            return False
        listener = Listener(on_press=on_press) # 创建监听器
        listener.start()    # 开始监听，每次获取一个键
        listener.join()     # 加入线程
        listener.stop()     # 结束监听
        return self.dir_

if __name__ == '__main__':
    c = Control()
    i = 0
    while True:
        i+=1
        print(i,c.getdir())
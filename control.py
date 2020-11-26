# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 16:17
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :control.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import cv2 as cv
import keyboard
from pynput.keyboard import Key,Controller,Listener

from direction import Direction

class Control():
    def __init__(self):
        self.dir_ = None
        self.keyboard_ = Controller()

    def getdir(self):
        self.dir_ = None
        def on_release(key):return False
        def on_press(key):
            if key == Key.up:self.dir_ = Direction.UP
            elif key == Key.down:self.dir_ = Direction.DOWN
            elif key == Key.left:self.dir_ = Direction.LEFT
            elif key == Key.right:self.dir_ = Direction.RIGHT
        listener = Listener(on_press=on_press,on_release=on_release)
        listener.start()
        listener.join()
        return self.dir_


def main():
    con = Control()
    i = 0
    while True:
        i+=1
        dir = con.getdir()
        print(i,dir)
        # print('get dir is {}'.format(dir))


if __name__ == '__main__':
    main()
    # print(Direction.UP.value)

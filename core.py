# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 16:02
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :core.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import map
import control

def main():
    # init
    MAP=map.Map(4)
    CONTROL = control.Control()
    # while 1
    while True:
        # TODO get input
        dir = CONTROL.getdir()

        # TODO try move
        # TODO try true -> move
        # TODO try false -> restart
        pass


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 16:02
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :core.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import os
import map
import control
import move
from direction import Direction

def main():
    mapsize = 4
    MAP = map.Map(mapsize)
    MOVE = move.Move(mapsize)
    CONTROL = control.Control()
    GAMEGOON = True
    os.system('cls')
    # MAP.setTestMap()# TODO del
    MAP.printMap()

    while GAMEGOON:
        dir = CONTROL.getdir()
        if dir == Direction.UP:ISCHANGE=MOVE.moveup(MAP)
        elif dir == Direction.DOWN:ISCHANGE=MOVE.movedown(MAP)
        elif dir == Direction.LEFT:ISCHANGE=MOVE.moveleft(MAP)
        elif dir == Direction.RIGHT:ISCHANGE=MOVE.moveright(MAP)
        else:continue
        if ISCHANGE:
            os.system('cls')
            if MAP.addone():MAP.printMap()
            else:GAMEGOON=False
        else:
            # TODO try false -> restart
            pass


if __name__ == '__main__':
    main()

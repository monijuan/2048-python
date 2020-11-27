# -*- coding: utf-8 -*-
# @Auth      :monijuan
# @Time      :2020/11/26 17:33
# @CSDN      :https://blog.csdn.net/qq_34451909
# @File      :move.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
class Move
    提供方法：根据移动的方向，修改map
"""
import map
import copy
from direction import Direction

class Move:
    def __init__(self,size):
        self.size_ = size       # 尺寸和map一样
        self.needmerge_ = []    # 临时存放需要合并的一行、一列
        self.oldmap_ = []       # 用来与合并后的map作比较

    def movemap(self,map,dir):
        """
        根据输入的方向移动
        如果map变化了返回True，如果没变化返回False
        """
        if dir == Direction.UP:return self.moveup(map)
        elif dir == Direction.DOWN:return self.movedown(map)
        elif dir == Direction.LEFT:return self.moveleft(map)
        elif dir == Direction.RIGHT:return self.moveright(map)
        else:return False

    def merge(self):
        """
        合并 needmerge_，思路：去零->合并->去零->补零
        """
        self.needmerge_ = [x for x in self.needmerge_ if x!=0]
        for i in range(len(self.needmerge_)-1):
            if(self.needmerge_[i]==self.needmerge_[i+1]):
                self.needmerge_[i]*=2
                self.needmerge_[i+1]=0
        self.needmerge_ = [x for x in self.needmerge_ if x!=0]
        while len(self.needmerge_)<self.size_:
            self.needmerge_.append(0)

    def moveup(self,map):
        """
        需求：
            2048执行向上操作
            深拷贝一份，用来比较是否发生变化
        思路：
            对每一列操作：
                获取这一列放到列表 needmerge_ 中
                合并 needmerge_
                从 needmerge_ 放回
        """
        self.oldmap_ = copy.deepcopy(map.map_)
        for col in range(self.size_):
            self.needmerge_.clear()
            for row in range(self.size_):
                self.needmerge_.append(map.map_[row][col])
            self.merge()
            for row in range(self.size_):
                map.map_[row][col] = self.needmerge_[row]
        return self.oldmap_ != map.map_

    def movedown(self,map):
        """
        2048执行向下操作，参考moveup
        """
        self.oldmap_ = copy.deepcopy(map.map_)
        for col in range(self.size_):
            self.needmerge_.clear()
            for row in range(self.size_-1,-1,-1):
                self.needmerge_.append(map.map_[row][col])
            self.merge()
            for row in range(self.size_):
                map.map_[self.size_-row-1][col] = self.needmerge_[row]
        return self.oldmap_ != map.map_

    def moveleft(self,map):
        """
        需求：
            2048执行向左操作
            深拷贝一份，用来比较是否发生变化
        思路：
            对每一行操作：
                获取每一行到 needmerge_
                合并
                放回
        """
        self.oldmap_ = copy.deepcopy(map.map_)
        for row in range(self.size_):
            self.needmerge_=map.map_[row]
            self.merge()
            map.map_[row] = self.needmerge_.copy()
        return self.oldmap_ != map.map_

    def moveright(self,map):
        """
            2048执行向右操作，参考moveleft
        """
        self.oldmap_ = copy.deepcopy(map.map_)
        for row in range(self.size_):
            self.needmerge_=map.map_[row][::-1]
            self.merge()
            map.map_[row] = self.needmerge_[::-1].copy()
        return self.oldmap_ != map.map_


def main():
    MAP = map.Map(4)
    MOVE = Move(4)

    MAP.setTestMap_2()
    MAP.printMap()
    # mapchange = MOVE.movedown(MAP)
    # mapchange = MOVE.moveright(MAP)
    # mapchange = MOVE.moveleft(MAP)
    mapchange = MOVE.moveup(MAP)
    MAP.printMap()
    print(mapchange)


if __name__ == '__main__':
    main()

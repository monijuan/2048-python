# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 17:33
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :move.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import map
import time
import copy

class Move():
    def __init__(self,size):
        self.size_ = size
        self.needmerge_ = []
        self.mergedmap_ = []
        self.ischange = False

    def merge(self):
        """
        去零->合并->去零->补零
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
        对每一列操作：
            准备一个列表放需要合并的一列
            获取这一列放到这个列表里
            合并
            放回
        """
        self.mergedmap_ = copy.deepcopy(map.map_)
        for col in range(self.size_):
            self.needmerge_.clear()
            for row in range(self.size_):
                self.needmerge_.append(map.map_[row][col])
            self.merge()
            for row in range(self.size_):
                map.map_[row][col] = self.needmerge_[row]
        self.ischange = self.mergedmap_ != map.map_
        return self.ischange

    def movedown(self,map):
        """
        参考up，修改获取时的索引和返回时的下标
        """
        self.mergedmap_ = copy.deepcopy(map.map_)
        for col in range(self.size_):
            self.needmerge_.clear()
            for row in range(self.size_-1,-1,-1):
                self.needmerge_.append(map.map_[row][col])
            self.merge()
            for row in range(self.size_):
                map.map_[self.size_-row-1][col] = self.needmerge_[row]
        self.ischange = self.mergedmap_ != map.map_
        return self.ischange

    def moveleft(self,map):
        """
        对每一行操作：
            获取一行
            合并
            放回
        """
        self.mergedmap_ = copy.deepcopy(map.map_)
        for row in range(self.size_):
            self.needmerge_=map.map_[row]
            self.merge()
            map.map_[row] = self.needmerge_.copy()
        self.ischange = self.mergedmap_ != map.map_
        return self.ischange

    def moveright(self,map):
        """
        对每一行操作：
            从右往左获取一行
            合并
            从右往左放回
        """
        self.mergedmap_ = copy.deepcopy(map.map_)
        for row in range(self.size_):
            self.needmerge_=map.map_[row][::-1]
            self.merge()
            map.map_[row] = self.needmerge_[::-1].copy()
        self.ischange = self.mergedmap_ != map.map_
        return self.ischange


def main():
    MAP = map.Map(4)
    MOVE = Move(4)

    # MAP.setTestMap()
    MAP.setTestMap_2()
    MAP.printMap()
    print('-'*30)

    # mapchange = MOVE.movedown(MAP)
    # mapchange = MOVE.moveright(MAP)
    # mapchange = MOVE.moveleft(MAP)
    mapchange = MOVE.moveup(MAP)
    MAP.printMap()
    print(mapchange)


if __name__ == '__main__':
    main()

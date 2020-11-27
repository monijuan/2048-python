# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 16:03
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :map.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
"""
class Map
    显示面板
    生成新数字
    判断当前面板还能否操作
"""
import random
import os

class Map:
    def __init__(self,size):
        self.size_=size
        self.map_=[[0 for _ in range(size)] for _ in range(size)]
        # self.map_=[[0]*size]*size
        self.addone()
        self.addone()

    def printMap(self):
        os.system('cls')
        print('\n\n\t\t+--------------------+')
        for row in self.map_:
            num_1 = row[0] if row[0]!=0 else ''
            num_2 = row[1] if row[1]!=0 else ''
            num_3 = row[2] if row[2]!=0 else ''
            num_4 = row[3] if row[3]!=0 else ''
            line = "\t\t|{:^5}{:^5}{:^5}{:^5}|\n\t\t|{:20}|"\
                .format(num_1,num_2,num_3,num_4,'')
            print(line)
        print('\t\t+--------------------+')

    def addone(self):
        """
        需求：
            移动之后map有变化才会进入此函数，因此肯定能添加
            当只剩一个位置的时候，返回False触发判断是否不可再操作
        思路：
            获取所有值为0的 row,col 保存到 zero_indexs
            从 zero_indexs 随机一个 [row,col] 添加数字
            0.1的概率生成4，0.9的概率生成2
        """
        zero_indexs = []
        for row in range(self.size_):
            for col in range(self.size_):
                if self.map_[row][col]==0:
                    zero_indexs.append([row,col])
        lastone = len(zero_indexs)==1
        [row,col] = zero_indexs[random.randint(0, len(zero_indexs)-1)]
        self.map_[row][col]=4 if random.random()<0.1 else 2
        return lastone

    def isend(self):
        """
        用于判断当前map还有没有办法操作
        当添加的数字是最后一个空的时候会调用这个函数
        """
        for row in range(self.size_):
            for col in range(self.size_):
                now   = self.map_[row][col]
                right = self.map_[row][col+1] if col+1<self.size_ else 1
                down  = self.map_[row+1][col] if row+1<self.size_ else 1
                if now==right or now==down:
                   return False
        return True


    def setTestMap(self):
        self.map_ = [
            [0,0,2,4],
            [2,2,0,4],
            [2,0,0,2],
            [2,2,2,2],
        ]

    def setTestMap_1(self):
        self.map_ = [
            [2,2,4,8],
            [128,64,32,16],
            [256,512,1024,2048],
            [8192,8192,8192,4096],
        ]

    def setTestMap_2(self):
        self.map_ = [
            [2,0,0,0],
            [4,0,0,0],
            [6,0,0,0],
            [8,8,0,0],
        ]


def main():
    map=Map(4)
    map.setTestMap()
    map.printMap()


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 16:03
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :map.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import random

class Map():
    def __init__(self,size):
        self.size_=size
        self.map_=[[0 for _ in range(size)] for _ in range(size)]
        # self.map_=[[0]*size]*size
        self.addone()
        self.addone()

    def printMap(self):
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
        zero_indexs = []
        for row in range(self.size_):
            for col in range(self.size_):
                if self.map_[row][col]==0:
                    zero_indexs.append([row,col])
        if len(zero_indexs)==0:
            return False
        else:
            index = random.randint(0, len(zero_indexs)-1)
            [row,col] = zero_indexs[index]
            # self.map_[row][col]=2
            self.map_[row][col]=4 if random.random()<0.1 else 2
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
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [2,8,16,0],
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

# -*- coding: utf-8 -*-
# @Auth      :Yin Zhijie
# @Time      :2020/11/26 16:03
# @Email     :yinzhijie@ilinkin.com.cn
# @File      :map.py
# @Software  :PyCharm
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

class Map():
    def __init__(self,size):
        self.map_=[['0']*size]*size
        #TODO add twice
        self.printMap()

    def printMap(self):
        for row in self.map_:
            for value in row:
                print(value,end='\t')
            print()


def main():
    map=Map(4)



if __name__ == '__main__':
    main()

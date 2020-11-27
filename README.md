![在这里插入图片描述](https://img-blog.csdnimg.cn/2020112717145212.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM0NDUxOTA5,size_16,color_FFFFFF,t_70)

GitHub：https://github.com/monijuan/2048-python

CSDN：https://blog.csdn.net/qq_34451909/article/details/110237769

## 一、介绍

一共五个.py文件，三个模块+两个辅助

- 【交互】control：获取键盘按键
- 【逻辑】move：根据移动的方向，修改map
- 【界面】map：显示面板、生成新数字、判断当前面板还能否操作

- core：启动游戏
- direction：一个枚举类，标记方向

直接在cmd中执行 `core.py` 即可启动2048.

## 二、代码

### 1.初始化

```python
import map
import control
import move

mapsize = 4                 # 定义尺寸4*4
MAP = map.Map(mapsize)      # 初始化【面板】
MOVE = move.Move(mapsize)   # 初始化【移动面板的工具】
CONTROL = control.Control() # 初始化【获取键盘的工具】
MAP.printMap()      # 显示初始面板
GAMEOVER = False
```

### 2.循环主体

```python
while GAMEOVER==False:  
    dir = CONTROL.getdir()              # 获取键盘方向
    ISCHANGE = MOVE.movemap(MAP,dir)    # 根据方向执行操作，返回【面板】是否有变化
    if ISCHANGE:                        # 如果【面板】有变化
        LASTONE = MAP.addone()          #   肯定可以添加，返回是不是最后一个空
        MAP.printMap()                  #   打印面板
        # 如果填充是最后一个空，则判断是否不能再操作
        GAMEOVER = MAP.isend() if LASTONE else False
```

### 3.Control

提供方法：获取键盘按键

详细说明参考：https://blog.csdn.net/qq_34451909/article/details/110233820

```python
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
```

### 4.Move

提供方法：根据移动的方向，修改map

#### movemap()

```python
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
```

moveup() 和 movedown() 差不多

moveleft() 和 moveright() 差不多

#### moveup()

```python
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
```

#### moveleft()

```python
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
```

#### merge()

```python
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
```

### 5.Map

显示面板、生成新数字、判断当前面板还能否操作

#### addone()

```python
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
```

#### isend()

```python
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
```

## 三、心得

看上去挺简单的游戏，实现起来还是会遇到一些问题的，比如说浅拷贝深拷贝、python的引用机制，还有一些小功能挺有意思的，比如随机生成新数字要用坐标，合并一行或一列的数据要四步走...

不过做完后发现其实还算简单，虽然逻辑是消除类游戏中算复杂的，但用来练手很合适
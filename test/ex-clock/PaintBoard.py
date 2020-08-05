from PyQt5.QtWidgets import QWidget
import sys, random, time, glob, os
from PyQt5.QtCore import Qt, QSize, QTimer
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QGridLayout, QLabel, QFrame)

class PaintBoard(QWidget):

    def __init__(self, Parent=None):
        super().__init__(Parent)
        self.__InitData()  # 先初始化数据，再初始化界面
        self.__InitView()

    def __InitData(self):  # 初始化数据
        self.__size = QSize(480, 460)  # 设置界面大小
        self.cell = dict()  # 储存全部像素点组件
        self.cells = list()  # 储存全部像素点
        self.arr = [(0, 0)]  # 用于选择坐标
        # 各生物初始值
        self.___GrassNum = 10
        self.___MacrophyteNum = 5
        self.___RabbitNum = 1
        self.___SnakeNum = 1
        self.___TigerNum = 1
        # 存储对象
        self.grassList = list()
        self.macrophyteList = list()
        self.rabbitList = list()
        self.snakeList = list()
        self.tigerList = list()

    def __InitView(self):  # 初始化界面
        self.timer = QTimer()  # 建立计时器
        #设置界面的尺寸为__size
        self.setFixedSize(self.__size)  # 限制窗口大小
        self.Floor = QHBoxLayout()
        self.Form = QFrame()
        # self.Form.setFrameShape(QFrame.Panel|QFrame.Plain)
        # self.Form.setFixedSize(465,445)
        self.Form.setFixedSize(465, 445)
        self.grid = QGridLayout()
        self.grid.setSpacing(1)
        self.Form.setLayout(self.grid)
        self.Floor.addWidget(self.Form)
        for row in range(10):  # 设置方格，每个方格代表一个生物
            for col in range(10):
                self.cell[(row, col)] = QLabel(self)
                self.cell[(row, col)].setStyleSheet(
                        'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')  # border-image:url(img/grass.png);
                # self.cell[(row,col)].setFixedSize(20,20)
                self.grid.addWidget(self.cell[(row, col)], row, col)
                self.cells.append((row, col))
        self.setLayout(self.Floor)

    # 清空界面
    def Clear(self):
        self.timer.stop()
        for row in range(10):
            for col in range(10):
                self.cell[(row, col)].setStyleSheet(
                        'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')

    # 改变数量
    def GrassNumChange(self, GrassNum=10):
        self.___GrassNum = GrassNum

    def MacrophyteNumChange(self, MacrophyteNum=5):
        self.___MacrophyteNum = MacrophyteNum

    def RabbitNumChange(self, RabbitNum=1):
        self.___RabbitNum = RabbitNum

    def SnakeNumChange(self, SnakeNum=1):
        self.___SnakeNum = SnakeNum

    def TigerNumChange(self, TigerNum=1):
        self.___TigerNum = TigerNum

    # 生成画面
    def Print(self):
        #小草
        i = 0
        while i < self.___GrassNum:
            grass = [1, 0, 0, 10]  # 存储小草信息
            tempdict = self.cells.copy()
            arr = random.choice(tempdict)
            grass[1] = arr[0]
            grass[2] = arr[1]
            self.grassList.append(grass)    #新对象加入到list中
            self.cells.remove(arr)
            self.cell[arr].setStyleSheet(
                    'QLabel{background-color:white;border-image:url(img/grass.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            i = i + 1

        # 大型植物
        i = 0
        while i < self.___MacrophyteNum:
            macrophyte = [2, 0, 0, 20]  # 存储大型植物信息
            tempdict = self.cells.copy()
            arr = random.choice(tempdict)
            macrophyte[1] = arr[0]
            macrophyte[2] = arr[1]
            self.macrophyteList.append(macrophyte)
            self.cells.remove(arr)
            self.cell[arr].setStyleSheet(
                    'QLabel{background-color:white;border-image:url(img/macrophyte.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            i = i + 1

        # 兔子
        i = 0
        while i < self.___RabbitNum:
            rabbit = [3, 0, 0, 30]  # 存储兔子信息
            tempdict = self.cells.copy()
            arr = random.choice(tempdict)
            rabbit[1] = arr[0]
            rabbit[2] = arr[1]
            self.rabbitList.append(rabbit)
            self.cells.remove(arr)
            self.cell[arr].setStyleSheet(
                    'QLabel{background-color:white;border-image:url(img/rabbit.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            i = i + 1

        # 蛇
        i = 0
        while i < self.___SnakeNum:
            snake = [4, 0, 0, 40]  # 存储蛇信息
            tempdict = self.cells.copy()
            arr = random.choice(tempdict)
            snake[1] = arr[0]
            snake[2] = arr[1]
            self.snakeList.append(snake)
            self.cells.remove(arr)
            self.cell[arr].setStyleSheet(
                    'QLabel{background-color:white;border-image:url(img/snake.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            i = i + 1

        # 老虎
        i = 0
        while i < self.___TigerNum:
            tiger = [5, 0, 0, 50]  # 存储老虎信息
            tempdict = self.cells.copy()
            arr = random.choice(tempdict)
            tiger[1] = arr[0]
            tiger[2] = arr[1]
            self.tigerList.append(tiger)
            self.cells.remove(arr)
            self.cell[arr].setStyleSheet(
                    'QLabel{background-color:white;border-image:url(img/tiger.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            i = i + 1

        self.timer.start()
        self.link()

    # 连接
    def link(self):
        self.timer.start(1000)  # 设置计时间隔并启动,间隔为1s=1000,2s=2000
        if len(self.cells) == 0:  # 满屏暂停
            self.timer.stop()
        else:
            self.timer.timeout.connect(self.Refresh)  # 计时结束更新画面

    # 更新界面
    def Refresh(self):
        # 生长和繁殖
        self.grassGrowth()  # 小草
        self.macrophyteGrowth()  # 大型植物
        self.rabbitGrowth()  # 兔子
        self.snakeGrowth()  # 蛇
        self.tigerGrowth()  # 老虎
        # 动物移动和捕食
        self.rabbitMove()  # 兔子移动
        self.snakeMove()  # 蛇移动
        self.tigerMove()  # 老虎移动
        print("该秒钟兔子的数量:%s" % self.___RabbitNum)


    # 生长和繁殖
    def grassGrowth(self):
        i = 0
        while i < self.___GrassNum:
            self.grass = [0, 0, 0, 0]
            self.grass = self.grassList.pop(0)  #list要先pop再append
            if self.grass[3] < 25:  #繁殖下限
                self.grass[3] = self.grass[3] + 2   #增加自身物质
                self.grassList.append(self.grass)
            else:  # 繁殖
                self.grass[3] = self.grass[3] - 8   #繁殖减少自身物质
                self.grassList.append(self.grass)
                self.grass = [1, 0, 0, 10]  #繁殖后的新对象
                tempdict = self.cells.copy()
                self.arr = random.choice(tempdict)
                self.grass[1] = self.arr[0]
                self.grass[2] = self.arr[1]
                self.grassList.append(self.grass)
                self.___GrassNum = self.___GrassNum + 1     #整体数量+1
                self.cells.remove(self.arr)
                self.cell[self.arr].setStyleSheet(
                        'QLabel{background-color:white;border-image:url(img/grass.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            i = i + 1

    def macrophyteGrowth(self):
        i = 0
        while i < self.___MacrophyteNum:
            self.macrophyte = [0, 0, 0, 0]
            self.macrophyte = self.macrophyteList.pop(0)
            if self.macrophyte[3] < 80:
                self.macrophyte[3] = self.macrophyte[3] + 4
                self.macrophyteList.append(self.macrophyte)
            else:  # 繁殖
                self.macrophyte[3] = self.macrophyte[3] - 16
                self.macrophyteList.append(self.macrophyte)
                self.macrophyte = [2, 0, 0, 20]  # 存储大型植物信息
                tempdict = self.cells.copy()
                self.arr = random.choice(tempdict)
                self.macrophyte[1] = self.arr[0]
                self.macrophyte[2] = self.arr[1]
                self.macrophyteList.append(self.macrophyte)
                self.___MacrophyteNum = self.___MacrophyteNum + 1
                self.cells.remove(self.arr)
                self.cell[self.arr].setStyleSheet(
                        'QLabel{background-color:white;border-image:url(img/macrophyte.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            i = i + 1

    def rabbitGrowth(self):
        i = 0
        while i < self.___RabbitNum:
            self.rabbit = [0, 0, 0, 0]
            self.rabbit = self.rabbitList.pop(0)
            if self.rabbit[3] < 120:
                self.rabbit[3] = self.rabbit[3] + 6
                self.rabbitList.append(self.rabbit)
            else:  # 繁殖
                self.rabbit[3] = self.rabbit[3] - 24
                self.rabbitList.append(self.rabbit)
                newrabbit = [3, 0, 0, 30]
                newrabbit[1] = self.rabbit[1]
                newrabbit[2] = self.rabbit[2]
                self.rabbitList.append(newrabbit)
                self.___RabbitNum = self.___RabbitNum + 1
            i = i + 1

    def snakeGrowth(self):
        i = 0
        while i < self.___SnakeNum:
            self.snake = [0, 0, 0, 0]
            self.snake = self.snakeList.pop(0)
            if self.snake[3] < 160:
                self.snake[3] = self.snake[3] + 8
                self.snakeList.append(self.snake)
            else:  # 繁殖
                self.snake[3] = self.snake[3] - 32
                self.snakeList.append(self.snake)
                newsnake = [4, 0, 0, 40]  # 存储蛇信息
                newsnake[1] = self.snake[1]
                newsnake[2] = self.snake[2]
                self.snakeList.append(newsnake)
                self.___SnakeNum = self.___SnakeNum + 1
            i = i + 1

    def tigerGrowth(self):
        i = 0
        while i < self.___TigerNum:
            self.tiger = [0, 0, 0, 0]
            self.tiger = self.tigerList.pop(0)
            if self.tiger[3] < 200:
                self.tiger[3] = self.tiger[3] + 10
                self.tigerList.append(self.tiger)
            else:  # 繁殖
                self.tiger[3] = self.tiger[3] - 40
                self.tigerList.append(self.tiger)
                newtiger = [5, 0, 0, 50]  # 存储小草信息
                newtiger[1] = self.tiger[1]
                newtiger[2] = self.tiger[2]
                self.tigerList.append(newtiger)
                self.___TigerNum = self.___TigerNum + 1

            i = i + 1

    # 移动和捕食
    def rabbitMove(self):
        i = 0
        while i < self.___RabbitNum:
            self.rabbit = [0, 0, 0, 0]  #获取该兔子对象的信息
            self.rabbit = self.rabbitList.pop(0)
            self.arr = (self.rabbit[1], self.rabbit[2])
            self.cells.append(self.arr) #先从list和界面中删掉
            self.cell[self.arr].setStyleSheet(
                    'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            self.moveChoose()   #选择移动方向
            flag = 0  # 0-没碰撞，1-被吃，2-吃其他

            j = 0
            while j < self.___GrassNum:
                self.grass = [0, 0, 0, 0]
                self.grass = self.grassList.pop(0)
                grassarr = (self.grass[1], self.grass[2])
                if self.arr[0] == grassarr[0] and self.arr[1] == grassarr[1]:  #吃草
                    self.rabbit[3] += self.grass[3] / 2     #获取草的物质
                    flag = 2
                else:
                    self.grassList.append(self.grass)
                j = j + 1
            self.___GrassNum = len(self.grassList)  #修改相应数量

            j = 0
            while j < self.___MacrophyteNum:
                self.macrophyte = [0, 0, 0, 0]
                self.macrophyte = self.macrophyteList.pop(0)
                macrophytearr = (self.macrophyte[1], self.macrophyte[2])
                if self.arr[0] == macrophytearr[0] and self.arr[1] == macrophytearr[1]:  # 吃大型植物
                    self.rabbit[3] += self.macrophyte[3] / 2
                    flag = 2
                else:
                    self.macrophyteList.append(self.macrophyte)
                j = j + 1
            self.___MacrophyteNum = len(self.macrophyteList)

            j = 0
            while j < self.___SnakeNum:
                self.snake = [0, 0, 0, 0]
                self.snake = self.snakeList.pop(0)
                snakearr = (self.snake[1], self.snake[2])
                if self.arr[0] == snakearr[0] and self.arr[1] == snakearr[1]:  #被蛇吃
                    self.snake[3] = self.snake[3] + self.rabbit[3] / 2
                    flag = 1
                    self.snakeList.append(self.snake)
                else:
                    self.snakeList.append(self.snake)
                j = j + 1
            self.___SnakeNum = len(self.snakeList)

            j = 0
            while j < self.___TigerNum:
                self.tiger = [0, 0, 0, 0]
                self.tiger = self.tigerList.pop(0)
                tigerarr = (self.tiger[1], self.tiger[2])
                if self.arr[0] == tigerarr[0] and self.arr[1] == tigerarr[1]:  # 被老虎吃
                    self.tiger[3] = self.tiger[3] + self.rabbit[3] / 2
                    flag = 1
                    self.tigerList.append(self.tiger)
                else:
                    self.tigerList.append(self.tiger)
                j = j + 1
            self.___TigerNum = len(self.tigerList)

            #根据flag判断有没有被吃或者吃掉其他
            if flag == 0 or flag == 2:
                self.cell[self.arr].setStyleSheet(
                        'QLabel{background-color:white;border-image:url(img/rabbit.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
                self.rabbit[1] = self.arr[0]
                self.rabbit[2] = self.arr[1]
                self.rabbitList.append(self.rabbit)
                if (self.arr in self.cells):
                    self.cells.remove(self.arr)
            i = i + 1
        self.___RabbitNum = len(self.rabbitList)
        #print("rabbit:%s" % self.___RabbitNum)

    def snakeMove(self):
        i = 0
        while i < self.___SnakeNum:
            self.snake = [0, 0, 0, 0]
            self.snake = self.snakeList.pop(0)
            self.arr = (self.snake[1], self.snake[2])
            self.cells.append(self.arr)
            self.cell[self.arr].setStyleSheet(
                    'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            self.moveChoose()
            flag = 0  # 0-没碰撞，1-被吃，2-吃其他

            j = 0
            while j < self.___GrassNum:
                self.grass = [0, 0, 0, 0]
                self.grass = self.grassList.pop(0)
                grassarr = (self.grass[1], self.grass[2])
                if self.arr[0] == grassarr[0] and self.arr[1] == grassarr[1]:  #吃草
                    self.snake[3] += self.grass[3] / 2
                    flag = 2
                else:
                    self.grassList.append(self.grass)
                j = j + 1
            self.___GrassNum = len(self.grassList)

            j = 0
            while j < self.___MacrophyteNum:
                self.macrophyte = [0, 0, 0, 0]
                self.macrophyte = self.macrophyteList.pop(0)
                macrophytearr = (self.macrophyte[1], self.macrophyte[2])
                if self.arr[0] == macrophytearr[0] and self.arr[1] == macrophytearr[1]:  #吃大型植物
                    self.snake[3] += self.macrophyte[3] / 2
                    flag = 2
                else:
                    self.macrophyteList.append(self.macrophyte)
                j = j + 1
            self.___MacrophyteNum = len(self.macrophyteList)

            j = 0
            while j < self.___RabbitNum:
                self.rabbit = [0, 0, 0, 0]
                self.rabbit = self.rabbitList.pop(0)
                rabbitarr = (self.rabbit[1], self.rabbit[2])
                if self.arr[0] == rabbitarr[0] and self.arr[1] == rabbitarr[1]:  #吃兔子
                    self.snake[3] += self.rabbit[3] / 2
                    flag = 2
                else:
                    self.rabbitList.append(self.rabbit)
                j = j + 1
            self.___RabbitNum = len(self.rabbitList)

            j = 0
            while j < self.___TigerNum:
                self.tiger = [0, 0, 0, 0]
                self.tiger = self.tigerList.pop(0)
                tigerarr = (self.tiger[1], self.tiger[2])
                if self.arr[0] == tigerarr[0] and self.arr[1] == tigerarr[1]:  # 被老虎吃
                    self.tiger[3] = self.tiger[3] + self.snake[3] / 2
                    flag = 1
                    self.tigerList.append(self.tiger)
                else:
                    self.tigerList.append(self.tiger)
                j = j + 1
            self.___TigerNum = len(self.tigerList)

            #根据flag判断有没有被吃或者吃掉其他
            if flag == 0 or flag == 2:
                self.cell[self.arr].setStyleSheet(
                        'QLabel{background-color:white;border-image:url(img/snake.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
                self.snake[1] = self.arr[0]
                self.snake[2] = self.arr[1]
                self.snakeList.append(self.snake)
                if (self.arr in self.cells):
                    self.cells.remove(self.arr)
            i = i + 1
        self.___SnakeNum = len(self.snakeList)
        #print("snake:%s" % self.___SnakeNum)

    def tigerMove(self):
        i = 0
        while i < self.___TigerNum:
            self.tiger = [0, 0, 0, 0]
            self.tiger = self.tigerList.pop(0)
            self.arr = (self.tiger[1], self.tiger[2])
            self.cells.append(self.arr)
            self.cell[self.arr].setStyleSheet(
                    'QLabel{background-color:white;border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
            self.moveChoose()
            flag = 0  # 0-没碰撞，1-被吃，2-吃植物
            j = 0
            while j < self.___GrassNum:
                self.grass = [0, 0, 0, 0]
                self.grass = self.grassList.pop(0)
                grassarr = (self.grass[1], self.grass[2])
                if self.arr[0] == grassarr[0] and self.arr[1] == grassarr[1]:  #吃草
                    self.tiger[3] += self.grass[3] / 2
                    flag = 2
                else:
                    self.grassList.append(self.grass)
                j = j + 1
            self.___GrassNum = len(self.grassList)
            j = 0
            while j < self.___MacrophyteNum:
                self.macrophyte = [0, 0, 0, 0]
                self.macrophyte = self.macrophyteList.pop(0)
                macrophytearr = (self.macrophyte[1], self.macrophyte[2])
                if self.arr[0] == macrophytearr[0] and self.arr[1] == macrophytearr[1]:  #吃大型植物
                    self.tiger[3] += self.macrophyte[3] / 2
                    flag = 2
                else:
                    self.macrophyteList.append(self.macrophyte)
                j = j + 1
            self.___MacrophyteNum = len(self.macrophyteList)
            j = 0
            while j < self.___RabbitNum:
                self.rabbit = [0, 0, 0, 0]
                self.rabbit = self.rabbitList.pop(0)
                rabbitarr = (self.rabbit[1], self.rabbit[2])
                if self.arr[0] == rabbitarr[0] and self.arr[1] == rabbitarr[1]:  #吃兔子
                    self.tiger[3] += self.rabbit[3] / 2
                    flag = 2
                else:
                    self.rabbitList.append(self.rabbit)
                j = j + 1
            self.___RabbitNum = len(self.rabbitList)

            j = 0
            while j < self.___SnakeNum:
                self.snake = [0, 0, 0, 0]
                self.snake = self.snakeList.pop(0)
                snakearr = (self.snake[1], self.snake[2])
                if self.arr[0] == snakearr[0] and self.arr[1] == snakearr[1]:  #吃蛇
                    self.tiger[3] += self.snake[3] / 2
                    flag = 2
                else:
                    self.snakeList.append(self.snake)
                j = j + 1
            self.___SnakeNum = len(self.snakeList)

            #根据flag判断有没有被吃或者吃掉其他
            if flag == 0 or flag == 2:
                self.cell[self.arr].setStyleSheet(
                        'QLabel{background-color:white;border-image:url(img/tiger.png);border-width:1px;border-style:solid;border-color:LightSteelBlue;}')
                self.tiger[1] = self.arr[0]
                self.tiger[2] = self.arr[1]
                self.tigerList.append(self.tiger)
                if (self.arr in self.cells):
                    self.cells.remove(self.arr)
            i = i + 1
        self.___TigerNum = len(self.tigerList)
        #print("tiger:%s" % self.___TigerNum)

    #选择移动方向
    def moveChoose(self):
        i = random.randint(1, 8)
        if self.arr[0] == 0:#在最左
            i = random.choice([1, 2, 3, 5, 6])
        if self.arr[0] == 9:#在最右
            i = random.choice([1, 2, 4, 7, 8])
        if self.arr[1] == 0:#在最上
            i = random.choice([1, 3, 4, 5, 7])
        if self.arr[1] == 9:#在最下
            i = random.choice([2, 3, 4, 6, 8])
        if self.arr[0] == 0 and self.arr[1] == 0:#在左上
            i = random.choice([1, 3, 5])
        if self.arr[0] == 0 and self.arr[1] == 9:#在左下
            i = random.choice([2, 3, 6])
        if self.arr[0] == 9 and self.arr[1] == 0:#在右上
            i = random.choice([1, 4, 7])
        if self.arr[0] == 9 and self.arr[1] == 9:#在右下
            i = random.choice([2, 4, 8])
        if i == 1:#向下
            self.arr = (self.arr[0], self.arr[1] + 1)
        if i == 2:#向上
            self.arr = (self.arr[0], self.arr[1] - 1)
        if i == 3:#向右
            self.arr = (self.arr[0] + 1, self.arr[1])
        if i == 4:#向左
            self.arr = (self.arr[0] - 1, self.arr[1])
        if i == 5:#右下
            self.arr = (self.arr[0] + 1, self.arr[1] + 1)
        if i == 6:#右上
            self.arr = (self.arr[0] + 1, self.arr[1] - 1)
        if i == 7:#左下
            self.arr = (self.arr[0] - 1, self.arr[1] + 1)
        if i == 8:#左上
            self.arr = (self.arr[0] - 1, self.arr[1] - 1)

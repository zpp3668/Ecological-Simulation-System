from PyQt5.Qt import QWidget, QColor, QPixmap, QIcon, QSize, QCheckBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QPushButton, QSplitter, \
    QComboBox, QLabel, QSpinBox, QFileDialog
from PaintBoard import PaintBoard

class MainWidget(QWidget):
    def __init__(self, Parent=None):
        super().__init__(Parent)
        self.__InitData()  # 先初始化数据，再初始化界面
        self.__InitView()

    # 初始化成员变量
    def __InitData(self):
        self.__paintBoard = PaintBoard(self)

    # 初始化界面
    def __InitView(self):
        self.setFixedSize(640, 480)
        self.setWindowTitle("生态模拟仿真系统")

        # 新建一个水平布局作为本窗体的主布局
        main_layout = QHBoxLayout(self)
        # 设置主布局内边距以及控件间距为10px
        main_layout.setSpacing(10)
        # 在主界面左侧放置动画显示界面
        main_layout.addWidget(self.__paintBoard)
        # 新建垂直子布局用于放置按键
        sub_layout = QVBoxLayout()
        # 设置此子布局和内部控件的间距为10px
        sub_layout.setContentsMargins(10, 10, 10, 10)

        # 添加文字和按钮
        # 设置小草数量
        self.__label_Grass = QLabel(self)
        self.__label_Grass.setText("小草数量")
        self.__label_Grass.setFixedHeight(20)
        sub_layout.addWidget(self.__label_Grass)  # 文字

        self.__spinBox_Grass = QSpinBox(self)
        self.__spinBox_Grass.setMaximum(35)  # 最大值为35
        self.__spinBox_Grass.setMinimum(2)  # 最小值为2
        self.__spinBox_Grass.setValue(10)  # 默认数值为10
        self.__spinBox_Grass.setSingleStep(2)  # 最小变化值为2
        self.__spinBox_Grass.valueChanged.connect(self.on_GrassNumChange)  # 关联spinBox值变化信号和函数on_GrassNumChange
        sub_layout.addWidget(self.__spinBox_Grass)  # 下拉选择框

        # 设置大型植物数量
        self.__label_Macrophyte = QLabel(self)
        self.__label_Macrophyte.setText("大型植物数量")
        self.__label_Macrophyte.setFixedHeight(20)
        sub_layout.addWidget(self.__label_Macrophyte)

        self.__spinBox_Macrophyte = QSpinBox(self)
        self.__spinBox_Macrophyte.setMaximum(25)#最大值为25
        self.__spinBox_Macrophyte.setMinimum(5)#最小值为5
        self.__spinBox_Macrophyte.setValue(5)  # 默认数值为5
        self.__spinBox_Macrophyte.setSingleStep(2)  # 最小变化值为2
        self.__spinBox_Macrophyte.valueChanged.connect(self.on_MacrophyteNumChange)
        sub_layout.addWidget(self.__spinBox_Macrophyte)

        # 设置兔子数量
        self.__label_Rabbit = QLabel(self)
        self.__label_Rabbit.setText("兔子数量")
        self.__label_Rabbit.setFixedHeight(20)
        sub_layout.addWidget(self.__label_Rabbit)

        self.__spinBox_Rabbit = QSpinBox(self)
        self.__spinBox_Rabbit.setMaximum(15)#最大值为15
        self.__spinBox_Rabbit.setMinimum(0)#最小值为0
        self.__spinBox_Rabbit.setValue(1)  # 默认数值为1
        self.__spinBox_Rabbit.setSingleStep(1)  # 最小变化值为1
        self.__spinBox_Rabbit.valueChanged.connect(self.on_RabbitNumChange)
        sub_layout.addWidget(self.__spinBox_Rabbit)

        # 设置蛇数量
        self.__label_Snake = QLabel(self)
        self.__label_Snake.setText("蛇数量")
        self.__label_Snake.setFixedHeight(20)
        sub_layout.addWidget(self.__label_Snake)

        self.__spinBox_Snake = QSpinBox(self)
        self.__spinBox_Snake.setMaximum(15)#最大值15
        self.__spinBox_Snake.setMinimum(0)#最小值0
        self.__spinBox_Snake.setValue(1)  # 默认数值为1
        self.__spinBox_Snake.setSingleStep(1)  # 最小变化值为1
        self.__spinBox_Snake.valueChanged.connect(self.on_SnakeNumChange)
        sub_layout.addWidget(self.__spinBox_Snake)

        # 设置老虎数量
        self.__label_Tiger = QLabel(self)
        self.__label_Tiger.setText("老虎数量")
        self.__label_Tiger.setFixedHeight(20)
        sub_layout.addWidget(self.__label_Tiger)

        self.__spinBox_Tiger = QSpinBox(self)
        self.__spinBox_Tiger.setMaximum(10)
        self.__spinBox_Tiger.setMinimum(0)
        self.__spinBox_Tiger.setValue(1)  # 默认数值为1
        self.__spinBox_Tiger.setSingleStep(1)  # 最小变化值为1
        self.__spinBox_Tiger.valueChanged.connect(self.on_TigerNumChange)
        sub_layout.addWidget(self.__spinBox_Tiger)

        # 确定按钮
        self.__btn_Sure = QPushButton("确定")
        self.__btn_Sure.setParent(self)  # 设置父对象为本界面
        self.__btn_Sure.clicked.connect(self.__paintBoard.Print)# 关联button点击事件和函数Print
        sub_layout.addWidget(self.__btn_Sure)

        # 清空按钮
        self.__btn_Clear = QPushButton("清空")
        self.__btn_Clear.setParent(self)  # 设置父对象为本界面
        self.__btn_Clear.clicked.connect(self.__paintBoard.Clear)
        sub_layout.addWidget(self.__btn_Clear)

        # 退出按钮
        self.__btn_Quit = QPushButton("退出")
        self.__btn_Quit.setParent(self)  # 设置父对象为本界面
        self.__btn_Quit.clicked.connect(self.Quit)
        sub_layout.addWidget(self.__btn_Quit)

        main_layout.addLayout(sub_layout)  # 将子布局加入主布局

    # 获取设置后的生物数量
    def on_GrassNumChange(self):
        GrassNum = self.__spinBox_Grass.value()
        self.__paintBoard.GrassNumChange(GrassNum)

    def on_MacrophyteNumChange(self):
        MacrophyteNum = self.__spinBox_Macrophyte.value()
        self.__paintBoard.MacrophyteNumChange(MacrophyteNum)

    def on_RabbitNumChange(self):
        RabbitNum = self.__spinBox_Rabbit.value()
        self.__paintBoard.RabbitNumChange(RabbitNum)

    def on_SnakeNumChange(self):
        SnakeNum = self.__spinBox_Snake.value()
        self.__paintBoard.SnakeNumChange(SnakeNum)

    def on_TigerNumChange(self):
        TigerNum = self.__spinBox_Tiger.value()
        self.__paintBoard.TigerNumChange(TigerNum)

    # 退出
    def Quit(self):
        self.close()

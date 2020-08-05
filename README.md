# Ecological-Simulation-System
生态模拟仿真系统

题目要求：
做一个模拟仿真系统，模拟自然界的生物生长与竞争：
    有至少三种生物（可以有更多种类）：
    生物可以移动，移动会消耗一定的身体；
    这些生物会随时时间，以相同的速率长大；
    至少有一种是类似食草动物：慢慢长大，不吃其它生物；
    至少有一种是类似食肉动物：吃其它生物；
    吃其它生物的情况下，捕食者可以获得被捕食者50%的物质，补充自己的身体（因此可以快速长大）
    身体长大到一定程度（这个阀值每种生物不一样），这些生物可以繁殖（有性繁殖、无性系列，随便）。繁殖要消耗一定的身份物质。后代与祖先有相同的繁殖阀值、生活习惯。
仿真系统一开始时，用户可以设置在“生活区域“中，有哪些位置有哪些生物；随后，就让那些生活自己移动、长大、捕食、繁殖。
可以用你喜欢的方式展现这个生态系统中的生物（字符式、二维式、三维式、方块式、图片式）
技术准备：
		绘图技术

技术与环境：
pycharm+pyqt5


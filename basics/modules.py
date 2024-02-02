# import random   # 直接引用整个库
from random import shuffle  # 只引用库中的一个函数

data = [1, 2, 3, 4, 5, 6]
shuffle(data)  # 顺序随机打乱
print(data)

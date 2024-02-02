# 集合 {}
data6 = {23, 45, 67, 78, 90}
data7 = {23, 45, 68, 79, 91}
print(type(data6))
# 增删查
data6.add(9)
print(data6)
data6.remove(23)
print(data6)
print(9 in data6)
# 集合之间的运算，交集，并集，减法
print(data6.intersection(data7))
print(data6.union(data7))
print(data6.difference())

#  集合（Set）是Python中的一种无序且不重复的数据结构。你可以使用集合来存储一组唯一的元素。
#  下面是一些集合的基本操作和示例：

# 创建一个集合
my_set = {1, 2, 3, 4, 5}

# 添加元素到集合
my_set.add(6)
print(my_set)  # 输出: {1, 2, 3, 4, 5, 6}

# 从集合中移除元素
my_set.remove(3)
print(my_set)  # 输出: {1, 2, 4, 5, 6}

# 检查元素是否在集合中
print(2 in my_set)  # 输出: True
print(7 in my_set)  # 输出: False

# 遍历集合
for num in my_set:
    print(num)

# 集合的数学运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # 输出: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # 输出: {3}

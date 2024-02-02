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
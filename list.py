# 7.列表
l = [1, 2, 3, 4, 5]
l[1] = 3.12
l[2] = 4
print(l)
print(type(l))
# 在结尾添加项
l.append(3)
print(l)
# 在任意位置插入数据
l.insert(0, 11)
print(l)
# 删除
del l[0]
print(l)
# 或者
l.pop(0)
print(l)
# 删除值
l.remove(4)  # 不是删除所有的4
# l.remove(4)
print(len(l))
# 列表中的数据类型不需要相同, 但不推荐这么写
data1 = [1, 2, [3, 4], "ni hao", 7.99]
print(data1)
print(data1[2][1])

# 7.1 把data2中的数据由小到大排列
data2 = [11, 42, 43, 45, 656, 12, 232, 34, 5, 676, 23, 34569, 56, 78, 98]
data2.sort()  # 从小到大
print(data2)
data2.sort(reverse=True)  # 由大到小
print(data2)
# 切片 这个区间是左闭右开的 >> data2[2:6]
data3 = data2[2:6]  # 表示将data2[2]、data[3]、data[4]、data[5] 四个元素赋值给data3
print(data3)
data4 = data2[2:7:2]  # 隔一个取一个
print(data4)

# 判断数据是否存在
print(45 in data2)
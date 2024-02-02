# 元组 即不能被修改的列表,内部""数据地址""不能被修改
data5 = (1, 2, 3, 4, 5, 6)
print(type(data5))
print(4 in data5)
print(len(data5))

# 元组是Python中的一种数据结构，用于存储一组有序的元素。
# 元组使用圆括号 () 来表示，其中的元素可以是任意数据类型，包括数字、字符串、列表、甚至其他元组。


# 创建一个包含不同数据类型的元组
my_tuple = [1, "hello", [3, 4, 5]]
print(my_tuple)  # 输出: (1, 'hello', [3, 4, 5])

# 访问元组中的元素
print(my_tuple[0])  # 输出: 1
print(my_tuple[1])  # 输出: hello

# 元组的解构赋值
a, b, c = my_tuple
print(a)  # 输出: 1
print(b)  # 输出: hello
print(c)  # 输出: [3, 4, 5]

# 元组的不可变性  即不能被修改的列表,内部""数据地址""不能被修改
my_tuple[0] = 2
print(my_tuple)

d = 3
my_tuple[0] = d
print(my_tuple)

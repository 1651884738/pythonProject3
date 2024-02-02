# 1.print 打印
print("hello world")
print("123")

# 2.四个基本的数据类型：整数（int）、小数（float）、布尔值（bool）、字符串（str）
a = 5
b = 8.8
c = True
d = "hello"
print("a+b = ", a + b)
print(id(a))  # 打印内存地址
print(id(b))
print(id(c))
print(id(d))
# 打印出类型
print(type(a)), print(type(b)), print(type(c)), print(type(d))
print(a > b)

# 3.基本运算
# 加 减 乘 除 取模 取余 幂运算 括号
# +  -  * /   //  %    **   ()
print(57 + 28)
print(12 - 9)
print(4 * 3)
print(36 / 9)
print(100 // 13)
print(100 % 13)
print(2 ** 4)
print(2 ** (3 + 1))

# 4.变量的命名，推荐驼峰命名法
你好 = 12  # 虽然汉字也能作为变量，但是不建议
print(你好)

# 5.逻辑运算符
# 与（and） 或（or） 非（not）
print(not 1)
print(0 and 1)
print(0 or 1)

# 5.if语句
x = 5
if x == 1:
    print("s1")
elif x == 2:
    print("s2")
else:
    print("s3")

# 6.循环
# while 表达式:
#     代码1
#     代码2

# for item in iterable:
#     # 执行循环体

if x < 10:
    x = 11

while x > 5:
    print("x is ", x)
    if x % 2:
        x -= 1
    else:
        x -= 2
# 6.1 计算 1! - 2! + 3! - 4! + ... + 49! - 50!
result = 0
count = 50
count_t = count
temp = 1

while count_t:
    if (count_t % 2) == 0:
        print("count is ", count_t)
        while count:
            temp *= count
            count -= 1
        result -= temp
        temp = 1
        count_t -= 1
        count = count_t
    else:
        while count:
            temp *= count
            count -= 1
        result += temp
        temp = 1
        count_t -= 1
        count = count_t

print("result is ", result)

count = 5
temp = 1
while count:
    temp *= count
    count -= 1
print("temp is ", temp)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = 0
for i in range(1, 51):
    if i % 2 == 0:
        result -= factorial(i)
    else:
        result += factorial(i)

print(result)


# 6.2 计算100以内的所有素数和
def prime_filter(n):
    if n == 2 or n == 1:
        return n
    for j in range(2, n):
        if (n % j) == 0:
            return 0
    return n


# 数学规定 1不是素数
sum2 = 0
for i in range(2, 100):
    sum2 += prime_filter(i)
print("100以内的所有素数和是：", sum2)

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

# 元组 即不能被修改的列表,内部""数据地址""不能被修改
data5 = (1, 2, 3, 4, 5, 6)
print(type(data5))
print(4 in data5)
print(len(data5))

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

# 8.字典 键值对
info = {"第一组": {"上": 23, "中": 34, "下": 89}, "第二组": {"上": 23, "中": 34, "下": 89}}
print(info["第二组"]["上"])
for w in info:
    print(w)

for w in info["第一组"]:
    print(w)  # 打印 key

for w in info["第一组"].values():
    print(w)  # 打印 value

for w in info["第一组"].items():
    print(w)  # 打印整体

# 9.字符串
# 定义一个字符串有三种方式：
str1 = '这是一个字符串'
str2 = "这是一个字符串"
str3 = """ 
这是
一个
分行的
字符串
"""
print(str1)
print(str2)
print(str3)

# 字符串的一些操作  类似于列表
print(len(str1))  # 取长度
print(str1[-1])  # 打印末尾，每一个字符都有其对应的下标
print(str1[:3])

# 修改
str4 = str1.replace("这是", "哈哈哈")
print(str4)
# find 查找字符， split 分割

# 字符串的加法和乘法
str5 = str1 + str2 + "加法"
print(str5)

str6 = "你好" * 6
print(str6)

# 格式化字符串
# 占位符法 : %d %s %f
name = "Mr.Wang"
haoma = 23
str_1 = "你好%s,您的号码是%d" % ("Mr.Wang", 23)
print(str_1)
# format 式
str_2 = "你好{},您的号码是{}".format(name, haoma)
print(str_2)
# f-string 式
str_3 = f"你好{name},您的号码是{haoma}"
print(str_3)

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        k = i * j
        print(f"{i} * {j} = {k}", end="\t")
    print("\r\n")

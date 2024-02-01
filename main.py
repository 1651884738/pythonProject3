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
l.remove(4) # 不是删除所有的4
# l.remove(4)
print(len(l))
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
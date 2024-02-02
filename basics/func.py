# 函数
def add1(n, m):
    return n + m


# 重新 增加注解
# 声明一个函数 add ，它有两个int类型的参数，返回值也是int类型
def add2(n: int, m: int) -> int:
    return n + m


print(add2(4, 5))

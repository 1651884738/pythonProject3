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


# 判断一个数是否为水仙花数
# 如 153 = 1*1*1 + 5*5*5 + 3*3*3

def test1(n: int):
    if n > 999 or n < 99:
        return 0
    a: int = n % 10
    b: int = ((n % 100) / 10).__int__()
    c: int = (n / 100).__int__()
    num = a ** 3 + b ** 3 + c ** 3
    if num == n:
        return n
    else:
        return 0


for i in range(1, 1000):
    num = test1(i)
    if num != 0:
        print("这是一个水仙花数：", num)

# 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        k = i * j
        print(f"{i} * {j} = {k}", end="\t")
    print("\r\n")

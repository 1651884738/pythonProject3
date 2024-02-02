# 8.字典 键值对
info = {"第一组": {"上": 23, "中": 34, "下": 89}, "第二组": {"上": 23, "中": 34, "下": 89}}
print(info["第二组"]["上"])

print(type(info))

for w in info:
    print(w)

for w in info["第一组"]:
    print(w)  # 打印 key

for w in info["第一组"].values():
    print(w)  # 打印 value

for w in info["第一组"].items():
    print(w)  # 打印整体

# 创建一个字典
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# 访问字典中的值
print(person["name"])  # 输出: Alice
print(person["age"])  # 输出: 25

# 修改字典中的值
person["age"] = 26
print(person["age"])  # 输出: 26

# 添加新的键-值对
person["gender"] = "female"
print(person)  # 输出: {'name': 'Alice', 'age': 26, 'city': 'New York', 'gender': 'female'}

# 删除键-值对
del person["city"]
print(person)  # 输出: {'name': 'Alice', 'age': 26, 'gender': 'female'}

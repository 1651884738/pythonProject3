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

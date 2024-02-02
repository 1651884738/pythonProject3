# 类 相当于是对象的模板
# 在Python中，class是一种用于创建对象的蓝图或模板。它定义了对象的属性（也称为实例变量）和方法（也称为实例函数）。

class People:
    def __init__(self, name, age):
        print("你调用了 __init__")
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says 666!")

    def test(self, string):
        print(f"{self.name} says %s" % string)


a = People("niko", 25)

print(a.age)
print(a.name)

a.bark()
a.test("ni hao")

# TODO: 封装和多态、类的属性、classmethod装饰器、装饰器的原理、自定义模块与__main__、文件读写、with的原理

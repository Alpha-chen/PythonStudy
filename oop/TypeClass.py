#!/usr/bin/env python3
# -*- coding:utf-8 -*-  
'使用元类type()创建对象'
__author__ = 'click'
__date__ = '2018/7/13 下午5:27'


# type方法的三个参数
# 1.生成类的名字
# 2.类继承的对象,多继承特性,
# 3.将已经书写完成的方法绑定到相应的对象上

class Hello(object):

    def __init__(self, name):
        self.name = name

    def hello(self):
        print("您好%s" % (self.name))


if __name__ == '__main__':
    hello = Hello("小明")
    print(hello.hello())


def fn(self, name='world'):
    print("Hellos %s" % (name))


# 使用type()方法生成一个Hellos对象
# 与class Hello生成的对象一直,只是type()方法为动态生成
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来
# ，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同
# ，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现
# ，本质上都是动态编译，会非常复杂。
Hellos = type('Hellos', (object,), dict(hellos=fn))

h = Hellos()
print(h.hellos())

# 查看Hellos 类型
print(type(Hellos))
# 查看Hellos方法中hellos类型
print(type(h.hellos))
# 查看Hellos实例h的类型
print(type(h))

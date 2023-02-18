#!python3.x
# -*- coding: utf-8 -*-


#例1:
#创建类
class Foo:  #class是关键字, Foo是类名称
    name = 'Tom'    #类变量,name是类属性
    
    def __init__(self):     #构造函数
        self.School = 'HangJin'     #实例变量
        self.Grade = 3
        # self.teacher = 'Mr Wang'
        
    def __delete__(self):   #当类结束的时候自动执行此函数
        pass
    
    #创建类中的函数,称为类的方法;
    def bar(self):      #self特殊参数,必填
        self.teacher = 'Mr Wang'      #这地方定义的self.teacher, 只有bar这个方法不调用后,类中的其他函数才可以调用self.teacher;
        print('Bar')
    
    def hello(self,name):
        print('I am {}'.format(name))
        # print(self.teacher)
        print('Sex:',self.sex)

# obj = Foo()         #根据Foo创建对象,注意有括号(), 叫类的实例化
# obj2 = Foo()
# 类的属性调用:
# print(Foo.name)     #用类名直接调用,Foo.School是不可以的,因为School不是类的属性,而是类实例化对象的属性;
# print(obj.name)     #用类的实例化对象调用;
# obj.bar()
# obj.sex = 'Male'      #给类实例添加属性
# print(obj.hello('Tom'))


# 类的方法调用
# obj.bar()             #通过类的实例化对象调用
# Foo().bar()           #通过函数名调用,注意类名称后面有括号
# obj.hello('Tom')    #执行hello方法

# obj.name = 'Lyli'       #通过类实例化对象赋值,不是修改
# Foo.name = 'Lyli'       #用类名,是对类变量的修改,会修改所有实例化对象的name属性
# print(obj.name)         #结果是Lyli, 不管是用 obj.name = 'Lyli' 还是 Foo.name = 'Lyli';
# print(obj2.name)         #只有是Foo.name = 'Lyli'时候,结果会是Lyli, 否则还是Tom;

# print(obj.School)        #通过类实例化对象调用,实例变量
# print(Foo().School)        #通类名称(带括号)调用,实例变量

'''
ps: 类中的函数第一个参数必须是self
    类中定义的函数叫"方法"
'''

#例2:类的属性调用:直接调用和间接调用

class Foo:          #创建类
    def __init__(self,name,age):    #构造函数,类实例化是自动执行
        '''初始化实例属性'''
        self.name = name
        self.age = age
    def detail(self):               #间接调用类实例化对象属性
        print("self.name:",self.name)
        print("self.age:",self.age)

#根据类Foo创建对象, 自动执行Foo类的__init__方法
# obj2 = Foo('Tom',18)
# print("obj2.name:",obj2.name)        #直接调用obj2对象的name属性
# print("obj2.age:",obj2.age)         #直接调用obj2对象的age属性
# obj2.detail()           #间接:Python默认会将obj2传给self参数,即obj2.detail(obj2),所以,此时方法内部的self = obj2. 即:self.name是Tom, self.age = 18

# obj3 = Foo('Lily',19)
# print("obj3.name:",obj3.name)
# print("obj3.age:",obj3.age)
# obj3.detail()

#例3:继承: 子继承父的内容(属性)
'''
例如：
　　猫可以：喵喵叫、吃、喝、拉、撒
　　狗可以：汪汪叫、吃、喝、拉、撒
如果我们要分别为猫和狗创建一个类，那么就需要为 猫 和 狗 实现他们所有的功能,
不难看出，吃、喝、拉、撒是猫和狗都具有的功能，而我们却分别的猫和狗的类中编写了两次。如果使用 继承 的思想，如下实现：

　　动物：吃、喝、拉、撒
　　   猫：喵喵叫（猫继承动物的功能）
　　   狗：汪汪叫（狗继承动物的功能）
'''
class animal:
    mm = 'cat'
    ww = 'dog'
    gg = 'duck'
    jj = 'chick'
    
    def __init__(self):
        self.pro = 'Animal'
        
    def eat(self):
        print('{} likes Eating'.format(self.name))
    
    def drink(self):
        print('{} likes Drinking'.format(self.name))
    
    def stoop():
        print('{} is Stooling'.format(self.name))
    
    def urinate(self):
        print('{} is Urinating'.format(self.name))
        
class cat(animal):          #在类后面的括号内写入另一个类,表示当前类继承另一个类,这个类就有了另一个类的所有属性和方法
    def __init__(self,name):
        self.name = name
        
    def MM(self):
        print('MiaoMiao')

class dog(animal):
    def __init__(self,name):
        self.name = name
        
    def WW(self):
        print('WangWang')
        
C = cat('小花')
# C.eat()     #cat()类对象就有了animal类的所有属性和方法了
# print(C.ww)   #类的属性也被继承了

# D = dog('小黑')
# D.drink()

#例4 python的类可以继承多个类, python3只有新式类(即广度优先的查找顺序)
class D:

    def bar(self):
        print('D.bar')

class C(D):

    def bar(self):
        print('C.bar')

class B(D):

    def bar(self):
        print('B.bar')

class A(B, C):

    def bar(self):
        print('A.bar')

# a = A()
# a.bar()   #查找顺序是A -> B -> C -> D


#例5: 多态,Animal是父类默认移动动作是'跑',子类可以继承,如果这个动作不适用子类,那么子类可以在自己的领域重新定义;
class Animal(object):
    def move(self,name):
        print("{} is running".format(name))
class dog(Animal):
    def talk(self):
        print("Wangwang")
class wolf(Animal):
    def talk(self):
        print("Wong...")
class rabit(Animal):
    #重写父类方法
    def move(self,name):
        print('{} is Jumping'.format(name))
    def talk(self):
        print('Mute...')
class action(object):
    def move_way(self,way,name):
        #传入不同的对象，执行不同的代码，即不同的move函数
        way.move(name)
 
# a = dog()
# b = wolf()
# c = rabit()
# d = action()
 
# d.move_way(a,'dog')
# d.move_way(b,'wolf')
# d.move_way(c,'rabit')
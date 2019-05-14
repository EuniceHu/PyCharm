a=9
class People():#创建类
    b=7
    def __init__(self,name='za',sex='nan'):#类的初始化参数
        self.tizh=50
        self.sg=177
        self.__age=18
    def eat(self):#创建方法
        print('正在吃饭')
        print(self.b)
    def run(self):
        print('正在跑步')
    def show(self):
        self.eat()
        self.run()
    def getage(self):
        age = 12
        return age
    def __ga(self):
        print('这是一个私有方法')
    def add(self,a,b):
        return a+b
    def getshow(self,name='zs',sex='nv',age=18):#默认值参数
        print('姓名是%s性别是%s年龄是%s'%(name,sex,age))

if __name__=='__main__':
    zs=People()#创建一个实例，创建一个队形
    zs.eat()
    zs.run()
    ls=People()
    ls.show()
    print(ls.getage())
    ls.tizh=80
    print(ls.tizh)

    s=People('zs','nv')
    s.tizh=90
    s.eat()
    print(a)
    print(s._People__age)#调用私有的属性
    s._People__ga()#调用私有的方法

    print(s.add(3,5))#调用有参数的方法
    print(s.add(45,90))

    s.getshow('zs','nv')
    s.getshow()
    s.getshow(name='lisi')
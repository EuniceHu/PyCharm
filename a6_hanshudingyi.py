#函数定义

def fun1():
    print('这是函数')
#函数的调用
fun1()

#参数的方法
# def y(a):
#     a = int(input('请输入年份：'))
#     if (a%4==0 and a%100!=0) or (a%400==0):
#         print('闰年')
#     else:
#         print('平年')
# y(2008)


def add(a,b):
    '''

    :param a: 加数1
    :param b: 加数2
    :return: a b的和
    '''
#     return a+b
# c = add(2,5)
# print(c)
# print(add.__doc__)
# print(range.__doc__)
#
#
# def showinfo(name,f,sex='nnn'):
#     print('姓名是%s性别是%s年龄是%s'%(name,sex,f))
# showinfo('李四',26)
# showinfo(sex='nn',f=18,name='wangw')


#递归函数，求阶乘
def dec(n):
    if n==1:
        return 1
    else:
        return n*dec(n-1)

print(dec(6))





def ac(a):
    return a*2
list1 = [1,3,5,7,8,9]
print (list(map(ac,list1)))

def af(x):
    if x%2==1:
        return x#保留奇数
list3=[1,23,45,56,8,9,64,90,7]
print(list(filter(af,list3)))#过滤掉偶数


for x in [1,2,34,5]:
    print(x)



t=8
def aa():
    global t
    print(t)
    t=2
    print(t)
aa()



def getmax(x,y):
    max1 = x
    if x>y:
        return x
    else:
        return y
print(getmax(8,7))




def getmax3(x,y,z,h):
    m1 = getmax(x,y)
    m2 = getmax(z,h)
    if m1>m2:
        return m1
    else:
        return m2
print(getmax3(1,23,57,68))



def funx(x):
    def funy(y):
        return x*y
    return funy
print(funx(7)(8))

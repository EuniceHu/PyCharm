# tup1 = (12,32,4,345,'aa')
# print(type(tup1))
# print(tup1[3])
# print(tup1[::-1])
#
# for x in tup1:
#     print(x)
#
# dict1 = {'name':'张三','age':12,'tel':123456}#字典的定义
# print(dict1['age'])#对字典的访问
# print(dict1['tel'])
# dict1['age'] = 22 #对字典的修改
# print(dict1)
# # del dict1['tel']#对字典的元素删除
# print(dict1)
# # del dict1#删除字典的定义
# print(dict1)
# # dict1.clear()#清空字段的内容
# print(dict1)
# print(dict1.pop('name'))#删除某个键值对 并且返回该键的值
# print(dict1)
# dict1['yy']='kk'#对字典新增一个元素
# print(dict1)
#
# y = ('name','age','hu')
# h = ['zs',12,'hui']
# d = {}
# dict3 = {'name':'zs','age':12,"kec":'yw'}
# dict3.update(ah=dict3.pop('name'))
# print(dict3)
#
# dict3.update(ah1='tu')#新增修改
# print(dict3)


# dict4= {'name':'zs','age':12,"kec":'yw'}
# dict4.update(dict5)#把5 加到4里面 键相同时取5的值
# print(dict4)


# dict6 = {'name':'zs','age':78,"add":'hb'}
# print('名字是%s'%dict6.get('name'))
#
# print('性别是%s'%dict6.get('sex'))
#
#
# dict7 = dict6.copy()
# print(dict7)
#
#
jian = ('name','age','sex')
di1 = {}
di1 = di1.fromkeys(jian,'abc')
print(di1)
print(di1.items())#遍历字典
for keys,values in di1.items():
    print(keys,values)


print(di1.keys())#输出字典里面所有的键
print(di1.values())#输出字典里面所有的值


ss = [123,'sdf']
print(type(ss))#判断数据类型
print(isinstance(ss,list))#判断数据类型
#数据类型转换
#int str list tuple dict
b = int('666')
print(type(b))

a = list((78,'aw',12,'try'))
print(type(a))
print(a)


# j = ('na','sex','add')
# z = ['za','ss',12]
# n = zip(j,z)
# aa = dict(n)
# print(aa)



import random
print(random.random())
print(random.randint(0,11))#生成0到10之间的随机整数
print(random.uniform(10,20))#生成10到20之间的随机小数


for i in range(10):#生成0到10之间的数据
    print(i)
i = [1,2,3,4,5,6]
random.shuffle(i)#列表里面的值随机打乱
print(i)

















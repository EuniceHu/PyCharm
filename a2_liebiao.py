#列表

# list1= ['abc','hu','sd','tu','nihao',78]#列表的定义
# #对列表的访问，截取，切片
# print(list1[1])
# print(list1[1:3])
# print(list1[:6:2])
# print(list1[::-1])
# list2 = ['abc','cd',[12,'a','b','aa'],78,'ff']
# print(list2[2])
# print(list2[2][3])
# print(list2[2][2][1])
# list2.append('88')#对列表的追加，只在列表的最后追加
# print(list2)
# list2[1] = 'abc'#对列表的修改
# print(list2)
# del list2[1]#删除列表指定索引的元素
# print(list2)
# list2.remove('cd')#移除列表中第一个匹配的元素
# print(list2)
# print(list2)
# print(len(list2))#求长度
# print(list2*3)#列表的元素被复制3次
# print('abc' in list2)#查看元素是否存在列表里面
#
#
# for x in  list2:#对列表的迭代
#     print(x)


# print(list2[-2])#取倒数第二个元素


li1 = ['abc','bn','aa','ss',78]
li2 = ['bc','hn','kl','lo']
# # print(li1.count('aa'))#求列表中某个元素的个数
li2.extend(li1)#列表的扩展
print(li2)
# # print(li1.index('aa'))
# # li1.insert(2,'cc')#在指定的索引位置插入元素
# # print(li1)
# print(li1.pop())#pop有返回值，把移除掉的元素返回来 默认移除
# print(li1)
# print(li1.pop(3))#移除指定索引的元素
# print(li1)
# li1.reverse()#列表的反转 等同于li1[::-1]
# print(li1)


# li3 = ['aa','jk','ssds']
# li3.sort()#从小到大排序  升序
# print(li3)
#
# li3.sort(reverse=True)#降序排列
# print(li3)
#
# li4 = [12,34,'aa','cc',[12,'hh']]
# li5 = li4#把li4的值给li5，列表的复制
# print(li5)
#
# import copy
# li7 = copy.copy(li4)
# print(li7)#把li4的值给li7，列表的复制


# li8 = copy.deepcopy(li4)#把li4的值给li8，列表的复制
# print(li8)#原列表元素色值改变，新列表值不会改变
#
# li4[3]= 'ddd'
# print(li5)
# print(li7)
# print(li8)
# li4[4][0]=22
# print(li4)
# print(li8)
# print(li7)
# print(li5)#li5 li7不管有没有嵌套，列表中的值都会改变
# li4[3]='uj'
# print(li4)
# print(li8)
# print(li7)
# print(li5)
#
#
# a = input('请输入你的年龄')
# print('你的年龄是%s' %a )
#
# b = input('请输入你的姓名')
# print('你的姓名是%s'%b)
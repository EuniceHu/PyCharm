# y = int(input('请输入年份：'))
# # print(y)
# if ((y%4==0 and y%100!=0) or (y%400 == 0)):
#     print(y,'是闰年')
# else:
#     print(y,'不是闰年')



# s = int(input('请输入分数：'))
# if s < 60:
#     print('不及格')
# elif 60 < s <= 70:
#     print('一般')
# elif 70 < s <= 80:
#     print('良好')
# elif 80 < s <= 90:
#     print('非常好')
# else:
#     print('优秀')



# i = 1
# while i<11:
#     print('我%s要好好学习'%i)
#     i+=2



# i2= 1
# while i2<11:
#     print(i2)
#     i2+=1
#
# c = 9
# while c < 5:
#     print(c)
#     c+=1
# else:
#     print(c)

#
# f = 1
# while f < 11:
#     f += 1#f=2
#     if f%2==0:
#         continue
#     else:
#         print(f)



list1 = [12,34,56,'ab','323']
for x in list1:
    print(x)


for x in range(1,11):
    if x%2==0:
        print('偶数是%d'%x)
    else:
        print(x)
        
sum = 0
for x in range(1,11):
    if x%2==0:
        sum+=x
print(sum)
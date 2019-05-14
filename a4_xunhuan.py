# print(9/2)
# print(9.0//2.0)
#
# print(9.0%2.0)
#
#
# print(7>9)
# print(7<9)
#
# b = 9
# b += 6
# print(b)
#
#
# print(13>6 and 6<4)
# print(13>6 or 6<4)
# print(not 6<4)
#
#
# print(id(4))
#
# print(id('4'))
#
# print(4 is not '4')




# d = 89
# if d<100:
#     print('d小于100')
# else:
#     print('d大于100')
#
#
#
# s = 90
# if s>90:
#     print('优秀')
# elif s>85:
#     print('良好')
# elif s>70:
#     print('一般')
# elif s>60:
#     print('及格')
# else:
#     print('不及格')
#
#
#
#
# if d>80 or s>95:
#     print('奖励一台iphone')
# else:
#     print('继续努力')
#平年闰年的判断  年份接收控制台输出
#猜数字游戏  生成一个1到10的随机数  判断猜的数和随机产生的数
#对学生成绩的判断 60  60~70  70~80  80~90  90~100  小于60
import random
a = random.randint(1,100)
for i in range(1,10):
    b = input('请输入一个数字')
    if b.isdigit():
        b = int(b)
    if a == b:
        print('猜对了')
        break
    elif a > b:
        print('大了')
    elif a < b:
        print('小了')
else:
    print('你输入的不是整数')
i+=1
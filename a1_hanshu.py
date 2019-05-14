# print('你好')
# a = '你好'
# b = "nihaoma"
# print(a)
# print(b[2])#访问字符串某一个值，通过下标
# #切片
# print(b[2:4])#前闭区间 后开区间，不包含4
# print(b[2:6:2])#2代表每隔一个取值
# print(b[0::2])#第二个冒号代表取到最后所有
# print(b[:6:2])#第一个冒号代表从0开始取
# print(b[::-1])#字符串的反转
# print(b[::-2])

"""
sname = '小明'
sage = 18
shengao = 1.88
print('姓名是%s年龄是%d身高是%f'%(sname,sage,shengao))
print('姓名是{}'.format(sname))

"""
# """
# f = """
# sdffhjnbmm
# jkhgdnms
# uyhjsn
# """
# print(f)
# """
# s = 'today is friday'
# print(s.isalnum())
# print(s.isalpha())#是否为纯字母
# print(s.isdigit())#是否为纯数字
# print(s.islower())#是否是纯小写
# print(s.isupper())#是否是纯大写
# print(s.istitle())#是否是标题
# print(s.isspace())#是否是空格
#
#
# print(len(s))
#
# print(s*2)

s = 'sdhnkxugehnmxj'
print(s.lower())#全部变为小写
print(s.upper())#变大写
print(s.replace("k","M"))#把f替换成M
print(s.split())#默认用空格来分割
print(s.split("n"))#用n分割
print(s.split('h',2))#用h分割，只分割前2个
print(s.count('n'))
print(s.count('n',3,10))#索引在[3,10]n出现的次数
print(s.endswith('xj'))#统计以什么结束
print(s.find('n'))#如果不存在 返回-1
print(s.find('n',2,8))#在索引[2.8]范围内，找n的索引
print(s.rfind('n',2,8))









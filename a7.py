try:
    a=1/0
    print(a)
except ZeroDivisionError:
    print('0不能作为被除数')
else:
    print(a)


try:
    f = open('ac.txt')
except IOError:
    print('没有该文件')
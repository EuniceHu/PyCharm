

# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i != k) and (i != j) and (k != j):
#                 print(i,j,k)

num = float(input("输入一个数字："))
if num >= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")
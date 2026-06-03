# count = 1;
# while count < 5:
#     print("hello world")
#     count += 1
#
#
# row = 1
#
# while row <= 3:
#     column = 1
#     while column <= 4:
#         print(f"第{row}排第{column}列", end = "\t")
#         column += 1
#     print()
#     row += 1
#
# # 迭代遍历
# s = "asdfghjkl"
#
# for i in s:
#     print(i, end = " ")
#
# print()
#
# # 相当于c语言里面的 for(int i = 11; i < 44; i += 3)
# for i in range(11,44,3):
#     print(i, end = " ")
from itertools import count

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j} * {i} = {i * j}", end = "\t")
#     print()


# for i in range(0, 5):
#     print(i)
#     if i == 3:
#         print("打印到 3 了")
#         break

for i in range(1, 4):
    if i == 2:
        print("这个 2 有问题")
        continue
    print(i)



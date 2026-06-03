# # 数据只要使用一次，就直接使用（没必要定义变量，这样反而占用内存）
# print(['aaa', 'bbb', 'ccc', 45, 42.5])
# print(type(['aaa', 'bbb', 'ccc', 45, 42.5]))
#
# li = ['aaa', 'bbb', 'ccc', 45, 42.5, 48]
# print(li, type(li))
#
# for i in range(0, 6):
#     print(li[i], end = "\t")
#
# print()
#
# lis = [0, 1, 2, 3, 4, 5, 6, 7, "yyy"]
# # 包前不包后
# print(lis[:5])      # 指定结束索引
#
# # 就是第一个直接取，然后在数 n 数到 n 就取
# print(lis[::2])
# print(lis[::-2])
#
# lis[8] = "nnn"
# print(lis)
#
#
#
# grades = [[90, 99], [58, 60], [66, 99]]
# print(grades[2][1])

# nums = [1.2, 2.6, 8.9]
#
# nums.append(100)
# print(nums)
#
# nums.extend("abcd")
# # nums.extend(123456) # 这个要为可迭代对象就是可以循坏的
# print(nums)
#
# # 前面指定索引 后面是添加的 数据
# nums.insert(1,9)
# print(nums)
#
# print(nums.index(9))
# # print(nums.index(88)) # 不存在就直接报错
#
#
# print(nums.count(9))
# print(nums.count(88))
#
#
#
# nums.remove(9)
# # nums.remove(99) # 不存在的话直接报错
# print(nums)



num = [1, 8, 9, 22, 10, 2, 1]
# 倒序排列
# num.sort(reverse = True)

# 直接反转
num.reverse()

# 根据 ASCII 编码排序
li = ['r', 'a', 't', 'b']
li.sort(reverse = True)
print(li)




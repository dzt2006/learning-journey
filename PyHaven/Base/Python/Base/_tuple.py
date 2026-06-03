# # 元素的顺序是固定的，一旦创建，就不能修改、删除或添加里面的元素
# tup = (1,)
# # 如果只有一个元素一定要加逗号，不然就不是元组了
# tups = (1)
# print(tup, type(tup))
# print(tups, type(tups))

# 索引与切片还是一样的
tup = (0, 1, 2, 3, 4, 5, 6, 7)
print(tup[0:7:3])
print(tup[0:8:3])
print(tup[-1:-8:-3])
print(tup[-1:-9:-3])
# 结束索引那要 +1 才可以覆盖到所有元素
tups =(0, 1, 2, 3)
print(tups[0:4])
print(tups[-1:-5:-1])
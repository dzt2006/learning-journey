# # 集合会自动去重
# s = {'a', 'b', 'c', 'a'}
# print(s, type(s))
#
# # 这个是字典
# data = {}
# print(data, type(data))
#
# # 这才是 空 集合
# datas = set()
# print(datas, type(datas))
#
# s.add('dzt')
# print(s)
#
# # 依旧要是要 可迭代对象
# s.update('dzt')
# print(s)
#
# s.remove('z')
# # 删除不存在的会报错
# # s.remove(88)
# s.discard(88)  # 这个就不会报错
#
# # 全部清除
# s.clear()
# print(s)

# 交集和并集
s1 = {1, 5, 6, 9, 8, 7}
s2 = {1, 5, 15, 55, 8, 88}
s3 = {18, 58, 155, 555, 85, 885}

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2 | s3)
print(s1.union(s2, s3))

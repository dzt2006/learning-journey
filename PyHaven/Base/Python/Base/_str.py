# name = "dzt"
# print("d" in name)
# print("dt" in name)
# print("dzt" not in name)
#
# print(name[0])
# print(name[1],end="-")
# print(name[2])
#
# print(name[-3])
# print(name[-2])
# print(name[-1])

""" 
str(start:stop:step)
start	起始索引
stop	结束索引
step	步长
"""

# 切片
# mystring = "hello world,dzt"
# print(mystring[:])
# print(mystring[2:])
#
# # 五步一走 正数从左往右。负数反之
# print(mystring[::5])
# print(mystring[::-5])
#
# # \t	制表符
# print("dzt\t" + "p")
# print("dzttt\t" + "p")
#
# # \n	换行符
# print("d\nz\nt\n")
#
# # \\两个反斜杠表示一个
# print("C:\\abc\\er")
# print(r"C:\abc\er")

# name = "dzt"
# age = 20
# print(f"name:{name}, age:{age}")
#
# pi = 3.1415926535
# print(f"保留 15 位小数：{pi:.15f}")
# # 四舍五入
# print(f"保留 3 位小数：{pi:.3f}")

# name = "haizi"
# # 后面补满 20 个字符 默认左对齐
# print(f"{name:20}")
#
# # 右对齐
# print(f"{name:>20}")
#
# # 居中对齐（填充符号）
# print(f"{name:@^20}")



names = "aaaasdfghjkl"
namees = "aa aa\nsdfgh jkl"
tr = "  hello Python   "
trs = "xxxhello pythonxxx"
tres = "ABC"

# find(sub)	查找子串位置	返回索引 / -1
print(names.find("g"))
print(names.find("v"))

# index(sub) 查找子串位置	返回索引 / 报错
print(names.index("g"))
# print(names.index("v")) # 直接报错

# count(sub) 统计出现次数	专门用于计数	返回 非负整数 (0 表示无)
print(names.count("g"))
print(names.count("v"))

print(names.replace("a", "vq")) # 全部替换
print(names.replace("a", "vq",1)) # 替换一次

print(namees.split())
print(namees.split(" ",1))  # 分割一次

print(tr.strip())  #  去掉两边的空格，中间的不行
print(trs.strip("x"))

print(trs.upper())  # 转大写
print(tres.lower()) # 转小写

name = "dengzeting"
print(name.startswith("deng"))
print(name.startswith("e"))

print(name.endswith("ting"))
print(name.endswith("in"))

print(name.islower())
print(name.isupper())

st = "今天好好玩"
print(st.encode())

# 字节前面不要加引号
b1 = b'\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa5\xbd\xe5\xa5\xbd\xe7\x8e\xa9'
print(b1.decode())


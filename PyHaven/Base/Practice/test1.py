name = input("请输入你的名称：")
age = input("请输入你的年龄：")
print("你好" + name + "，你今年" + age + "岁，" + "欢迎学习Python")

print(f"你好{name}，你今年{age}岁，欢迎学习python")

w = float(input("请输入你的体重（单位：kg）："))
h = float(input("请输入你的身高（单位：m ）："))
BIM = w + h**2
print("你的BIM为：" + str(BIM))
print(f"你的BIM为：{BIM}" )

# int: 用于储存整数 如 -2 0 3等 精度不会丢失

# float: 用于储存小鼠 如 -2.6，3.14等 当位数超过17位后精度会丢失很严重

# str: 用于储存文本，要用‘’或者""包起来  不能直接进行数学运算，可以拼接，截取


print("姓名：" + name + "，年龄：" + str(age) + "，身高：" + str(w) + "kg，身高：" + str(h) + "m")
print(f"姓名：{name}，年龄：{age}，体重：{w:.2f}kg，身高：{h:.2f}m")



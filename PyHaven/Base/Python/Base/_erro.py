# 尝试打印一个没有定义的变量
# print(name)     # NameError: name 'name' is not defined

# 处理异常
# try:
#     num = int(input("请输入一个数字："))
#     print(num)
# except Exception:       # 所有非语法异常捕获的父类
#     print("输入错误")


# try:
#     num = int(input("请输入一个数字："))
# except ValueError:       # 只捕获 值 错误
#     print("传入有问题")

# try:
#     print(1 / 0)
# except (ValueError, ZeroDivisionError):
#     print("有问题")



# try:
#     print("1" > 1)
# except ValueError:
#     print("有问题")
# except ZeroDivisionError:
#     print("除数不能为零")
# except TypeError:
#     print("类型错误")
#
#
#
# try:
#     print("1" > 1)
# except TypeError as e:
#     print(e)    # 打印异常具体描述信息



# try:
#     num = int(input("请输入一个数字："))
# except ValueError as e:
#     print(e)
# else:
#     print(num, type(num))
# finally:
#     print("一定会执行")



e = Exception("余额不足")
raise e


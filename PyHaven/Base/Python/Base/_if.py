# num = 16
#
# if num % 2 == 0:
#     print("他是偶数")
#
# user = input("请输入用户名：")
# pwd = input("请输入密码：")
#
# # and 且 与
# if user == "dzt" and pwd == "123456":
#     print("登陆成功",end="")
#
# # or 或
# fruit = input("请输入水果名：")
#
# if fruit == "苹果" or fruit == "香蕉":
#     print("是常见水果",end="")




# # not 非
# num = int(input("请输入一个整数："))
#
# # 实则就是c语言中的 if(num != 0)
# if not num == 0:
#     print("不为 0 ")


# 非零非空的整数为 true 繁殖为 false
#
score = int(input("Enter your score: "))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")
#
# print("及格" if score >= 60 else "不及格")


# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 60:
#     print("合格")
# else:
#     print("不合格")




is_member = input("是否为会员（y/n）：").lower()

if is_member == "y":
    print("是会员")
else:
    print("不是会员")
    money = float(input("请输入消费的额度"))
    if money >= 200:
        print("注册会员")
    elif money >= 100:
        print("再买一些")
    else:
        print("下次光临")



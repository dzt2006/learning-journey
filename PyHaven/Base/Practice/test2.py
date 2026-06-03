# a.输入0-100之间的考试分数，通过分支判断输出等级：90分及以上为优秀，80-89分为良好，60-79分为及格，60分以下为不及格（35分）
score = float(input("请输入你的成绩（必须在0-100的范围内）: "))
if score > 100 or score < 0:
    print("输入不合法")
else:
    if score >= 90:
        print("优秀")
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")

# b.输入任意整数，判断该数字是奇数还是偶数，输出对应结果（30分）
num = int(input("输入一个整数: "))
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")


# c.输入任意年份，编写程序判断该年份是否为闰年（判断规则：能被4整除但不能被100整除，或能被400整除）（35分）
year = int(input("输入任意年份："))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")


# •拓展选做题：结合多条件判断，实现输入月份，判断对应季节（3-5月春季，6-8月夏季，9-11月秋季，12-2月冬季）
month = int(input("输入月份（只能为1-12月）："))
if month > 12 or month <= 0:
    print("输入不合法")
else:
    if 3 <= month <= 5 :
        print(f"{month}为春季")
    elif 6 <= month <= 8:
        print(f"{month}为夏季")
    elif 9 <= month <= 11:
        print(f"{month}为秋季")
    else:
        print(f"{month}为冬季")
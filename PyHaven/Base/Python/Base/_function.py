# 默认参数要放在后面 如果你不传值的话他会报错
def fun1(num, a = 1):
    print(a)
fun1('a')

# 可变参数 可以接收任意多个参数
def sum_(*numbers):
    res = 0
    for num in numbers:
        res += num
    print(res)

sum_(100, 200, 300)



# 关键字可变参数
def create_user(username, **kwargs):
    print("可选参数", kwargs)

create_user("李素", age = 18, sex = '男')

# 默认返回 none

def calc(a, b):
    sum_ab = a + b
    sul_ab = a * b
    return sum_ab, sul_ab

res = calc(1,5)
print(res, type(res))





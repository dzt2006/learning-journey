# Python 学习笔记

> 底层原理见 [数据结构学习笔记](./数据结构学习笔记.md) ｜ 数值计算见 [Numpy学习笔记](./Numpy学习笔记.md)

## 目录
- [变量与数据类型](#变量与数据类型)
- [输入输出](#输入输出)
- [条件判断](#条件判断)
- [循环语句](#循环语句)
- [函数](#函数)
- [字符串](#字符串)
- [列表](#列表)
- [元组、集合与字典](#元组集合与字典)
- [异常处理](#异常处理)
- [类与对象](#类与对象)

---

## 变量与数据类型

### 变量的定义和使用

变量就像一个小盒子，用来存放各种数据。你可以随时给这个盒子换不同的东西。

```python
# 定义一个变量，存放数字40
num1 = 40
print(num1)

# 同时定义多个变量，一次性给它们都赋值
num2, num3, num4 = 20, 30, 40
print(num1, num2, num3, num4)

# 变量可以重新赋值，就像盒子里换东西
num1 = 60
print(num1)
```

**执行结果：**
```
40
40 20 30 40
60
```

**局限性分析**：

- 变量名不能以数字开头
- 变量名不能使用Python的关键字

---

### Python 中等号（=）的空格规则

Python 里等号加不加空格，这样记就行：

**赋值的时候加空格，定义默认参数和指名传参的时候不加空格。**

```python
# 赋值：加空格
x = 5
name = "hello"

# 默认参数：不加空格
def greet(name="world"):
    print(name)

# 指名传参：不加空格
greet(name="小明")
```

---

### 基本数据类型

#### 整数类型（int）

整数就是没有小数点的数字，正数负数都行。它的精度不会丢失，可以放心使用。

```python
# 存放一个整数
money = 1000000
print(money)
print(type(money))
```

**执行结果：**
```
1000000
<class 'int'>
```

#### 浮点数类型（float）

浮点数就是带小数点的数字。但要注意，如果小数位数超过17位，精度就会丢失很严重。

```python
# 存放圆周率的近似值
pi = 3.14
print(pi)
print(type(pi))
```

**执行结果：**
```
3.14
<class 'float'>
```

#### 布尔类型（bool）

布尔类型只有两个值：真（True）和假（False）。通常用来做判断。

```python
# 定义一个布尔变量
is_member = True
print(is_member)
print(type(is_member))

# 可以重新赋值
is_member = False
print(is_member)
print(type(is_member))
```

**执行结果：**
```
True
<class 'bool'>
False
<class 'bool'>
```

#### 字符串类型（str）

字符串就是文本内容，要用单引号或者双引号包起来。不能直接做数学运算，但可以拼接和截取。

```python
# 定义一个字符串
greeting = "hello world"
print(greeting)
print(type(greeting))
```

**执行结果：**
```
hello world
<class 'str'>
```

#### 空值类型（NoneType）

None表示什么都没有，是空的意思。

```python
# 定义一个空值
data = None
print(data)
print(type(data))
```

**执行结果：**
```
None
<class 'NoneType'>
```

---

#### 复数类型（complex）

复数由实部和虚部组成，格式为 `实部 + 虚部j`。

```python
C = 2 + 2j
print(type(C))
```

**执行结果：**
```
<class 'complex'>
```

---

#### Python 中的真假值

在 Python 中，以下值被认为是"假"（False）：
- 数字 0
- 空字符串 ""

其他值一般被认为是"真"（True）。

```python
data = 0
print(data, type(data))

data1 = ""
print(data1, type(data1))
```

**执行结果：**
```
0 <class 'int'>
 <class 'str'>
```

---

## 输入输出

### 输出函数 print()

print() 是 Python 内置函数，用来把你想显示的内容打印到屏幕上。

参数说明：
- sep：多个内容之间用什么隔开，默认是空格
- end：打印完之后用什么结尾，默认是换行

```python
# 打印一句问候语
print("hello world")

# 打印一个数字
print(1)

# 打印多个数字，中间用空格隔开
print(1, 2, 3)

# 打印多个数字，中间用字母q隔开
print(1, 2, 3, sep="q")

# 打印完不换行，用逗号和空格结尾
print(1, 2, 3, end=", ")
print(1, 2, 3)

# 数学运算会先算完再打印，先乘除后加减
print(2 + 2 * 3 / 4)

# 打印多行内容
print("""你好，
python
我来学习了""")
```

**执行结果：**
```
hello world
1
1 2 3
1q2q3
1 2 3, 1 2 3
3.5
你好，
python
我来学习了
```

---

### 输入函数 input()

input() 是 Python 内置函数，用来让用户在键盘上输入内容。默认接收到的都是字符串类型。

参数说明：
- 提示信息：可以写一段文字，告诉用户需要输入什么

```python
# 获取用户输入的姓名
name = input("请输入姓名：")
print(name)

# 获取用户输入的年龄
age = input("请输入年龄：")
print(type(age))

# 把输入的内容转成整数再用
num1 = int(input("请输入第一整数："))
num2 = input("请输入第二整数：")
print(num1 + int(num2))
```

**执行结果（示例）：**
```
请输入姓名：张三
张三
请输入年龄：20
<class 'str'>
请输入第一整数：10
请输入第二整数：20
30
```

---

## 条件判断

### if 语句

if就是如果的意思，如果条件满足，就执行里面的代码。

```python
# 判断一个数是不是偶数
num = 16
if num % 2 == 0:
    print("他是偶数")
```

**执行结果：**
```
他是偶数
```

---

### if-else 语句

if-else就是二选一，如果满足条件就做这个，不满足就做那个。

```python
# 判断考试是否及格
score = int(input("Enter your score: "))
if score >= 60:
    print("及格")
else:
    print("不及格")
```

**执行结果（示例）：**
```
Enter your score: 75
及格
```

---

### if-elif-else 语句

if-elif-else就是多选一，按顺序判断，满足哪个就执行哪个。

```python
# 根据分数判断等级
score = int(input("Enter your score: "))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("合格")
else:
    print("不合格")
```

**执行结果（示例）：**
```
Enter your score: 85
良好
```

---

### 嵌套条件判断

条件判断可以嵌套使用，即在某个条件分支内部再进行条件判断。

```python
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
```

**执行结果（示例1）：**
```
是否为会员（y/n）：y
是会员
```

**执行结果（示例2）：**
```
是否为会员（y/n）：n
不是会员
请输入消费的额度150
再买一些
```

---

### 逻辑运算符

#### and（且）

and就是并且的意思，所有条件都满足才算满足。

```python
# 验证用户名和密码
user = input("请输入用户名：")
pwd = input("请输入密码：")
if user == "dzt" and pwd == "123456":
    print("登陆成功", end="")
```

#### or（或）

or就是或者的意思，只要有一个条件满足就算满足。

```python
# 判断是不是常见水果
fruit = input("请输入水果名：")
if fruit == "苹果" or fruit == "香蕉":
    print("是常见水果", end="")
```

#### not（非）

not就是反过来的意思，原来满足的变成不满足，不满足的变成满足。

```python
# 判断数字是不是不为0
num = int(input("请输入一个整数："))
if not num == 0:
    print("不为 0 ")
```

---

## 循环语句

### while 循环

while就是当的意思，当条件满足时，就反复执行里面的代码。

```python
# 打印5遍hello world
count = 1
while count < 5:
    print("hello world")
    count += 1
```

**执行结果：**
```
hello world
hello world
hello world
hello world
```

---

### for 循环

for循环就是把一堆东西一个一个拿出来处理，适合知道循环次数或者要遍历内容的场景。

```python
# 遍历字符串的每个字符
s = "asdfghjkl"
for i in s:
    print(i, end=" ")
print()

# 使用range()生成数字序列
# range(开始, 结束, 步长)，包前不包后
for i in range(11, 44, 3):
    print(i, end=" ")
```

**执行结果：**
```
a s d f g h j k l 
11 14 17 20 23 26 29 32 35 38 41 
```

#### range() 是 Python 内置函数，用来生成连续整数序列，基本都配合 for 循环使用。
遵循规则：取开头，不取结尾。
参数说明：
- start（第一个参数）：序列开始的数字，可不写，默认从 0 开始
- stop（第二个参数）：序列结束边界，取不到这个数本身，必须写
- step（第三个参数）：每次跳动的间隔（步长），可不写，默认固定 + 1；写负数就能倒着数

**整数序列**就是一串按顺序排列的整数。

---

### break和continue

#### break

break就是打断的意思，直接跳出整个循环，后面不执行了。

```python
# 打印到3就停止
for i in range(0, 5):
    print(i)
    if i == 3:
        print("打印到 3 了")
        break
```

**执行结果：**
```
0
1
2
3
打印到 3 了
```

#### continue

continue就是继续的意思，跳过当前这一次，直接进入下一次循环。

```python
# 遇到2就跳过
for i in range(1, 4):
    if i == 2:
        print("这个 2 有问题")
        continue
    print(i)
```

**执行结果：**
```
1
这个 2 有问题
3
```

---

### 嵌套循环

嵌套循环就是循环里面还有循环，外层循环执行一次，内层循环执行完整一遍。

```python
# 打印座位表
row = 1
while row <= 3:
    column = 1
    while column <= 4:
        print(f"第{row}排第{column}列", end="\t")
        column += 1
    print()
    row += 1
```

**执行结果：**
```
第1排第1列	第1排第2列	第1排第3列	第1排第4列	
第2排第1列	第2排第2列	第2排第3列	第2排第4列	
第3排第1列	第3排第2列	第3排第3列	第3排第4列	
```

---

### 九九乘法表

使用嵌套循环可以打印九九乘法表。

```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()
```

**执行结果：**
```
1 * 1 = 1	
1 * 2 = 2	2 * 2 = 4	
1 * 3 = 3	2 * 3 = 6	3 * 3 = 9	
1 * 4 = 4	2 * 4 = 8	3 * 4 = 12	4 * 4 = 16	
1 * 5 = 5	2 * 5 = 10	3 * 5 = 15	4 * 5 = 20	5 * 5 = 25	
1 * 6 = 6	2 * 6 = 12	3 * 6 = 18	4 * 6 = 24	5 * 6 = 30	6 * 6 = 36	
1 * 7 = 7	2 * 7 = 14	3 * 7 = 21	4 * 7 = 28	5 * 7 = 35	6 * 7 = 42	7 * 7 = 49	
1 * 8 = 8	2 * 8 = 16	3 * 8 = 24	4 * 8 = 32	5 * 8 = 40	6 * 8 = 48	7 * 8 = 56	8 * 8 = 64	
1 * 9 = 9	2 * 9 = 18	3 * 9 = 27	4 * 9 = 36	5 * 9 = 45	6 * 9 = 54	7 * 9 = 63	8 * 9 = 72	9 * 9 = 81	
```

---

### 水仙花数判断程序

#### 什么是水仙花数

水仙花数是一个三位数，每个位上的数字的立方和等于它本身。比如153就是水仙花数，因为1³+5³+3³=153。

```python
while True:
    # 获取用户输入
    input_str = input("请输入一个三位数（输入q退出）：")
    
    # 检查是否退出
    if input_str.lower() == 'q':
        print("程序结束")
        break
    
    # 验证输入是否为数字
    if not input_str.isdigit():
        print("输入错误！请输入数字。")
        continue
    
    # 转换为整数
    num = int(input_str)
    
    # 验证是否为三位数
    if num < 100 or num > 999:
        print("输入错误！请输入100-999之间的三位数。")
        continue
    
    # 提取百位、十位、个位
    hundreds = num // 100
    tens = (num // 10) % 10
    units = num % 10
    
    # 计算立方和
    sum_cubes = hundreds ** 3 + tens ** 3 + units ** 3
    
    # 判断是否为水仙花数
    if sum_cubes == num:
        print(f"{num} 是水仙花数！")
    else:
        print(f"{num} 不是水仙花数。")
```

**执行结果（示例）：**
```
请输入一个三位数（输入q退出）：153
153 是水仙花数！
请输入一个三位数（输入q退出）：abc
输入错误！请输入数字。
请输入一个三位数（输入q退出）：99
输入错误！请输入100-999之间的三位数。
请输入一个三位数（输入q退出）：123
123 不是水仙花数。
请输入一个三位数（输入q退出）：q
程序结束
```

---

## 函数

### 函数的定义和调用

函数就是把一段代码打包起来，给它起个名字，以后想用的时候直接叫名字就行，不用重复写。

```python
# 定义一个简单函数
def greet():
    print("你好！")

# 调用函数
greet()
```

**执行结果：**
```
你好！
```

---

### 函数参数

#### 默认参数

默认参数就是给参数一个默认值，调用时如果不传这个参数，就用默认值。

注意事项：默认参数一定要放在后面。

```python
# 定义带默认参数的函数
def fun1(num, a=1):
    print(a)

# 只传一个参数，a用默认值
fun1('a')
```

**执行结果：**
```
1
```

---

### 可变参数 *args

使用 `*` 可以接收任意多个参数，把它们打包成一个元组。

```python
def sum_(*numbers):
    res = 0
    for num in numbers:
        res += num
    print(res)

sum_(100, 200, 300)
```

**执行结果：**
```
600
```

---

### 关键字可变参数 **kwargs

使用 `**` 可以接收任意多个关键字参数，把它们打包成一个字典。

```python
def create_user(username, **kwargs):
    print("可选参数", kwargs)

create_user("李素", age=18, sex='男')
```

**执行结果：**
```
可选参数 {'age': 18, 'sex': '男'}
```

---

### 函数返回值

函数可以返回多个值，实际上返回的是一个元组。

```python
def calc(a, b):
    sum_ab = a + b
    mul_ab = a * b
    return sum_ab, mul_ab

res = calc(1, 5)
print(res, type(res))
```

**执行结果：**
```
(6, 5) <class 'tuple'>
```

---

## 字符串

### 字符串索引

字符串里的每个字符都有编号，从0开始。也可以用负数从后往前数，-1就是最后一个。

```python
name = "dzt"
print(name[0])
print(name[1], end="-")
print(name[2])

# 负数索引
print(name[-3])
print(name[-2])
print(name[-1])
```

**执行结果：**
```
d
z-t
d
z
t
```

---

### 字符串切片

切片就是从字符串里截取一段出来。格式是[开始:结束:步长]，包前不包后。

```python
mystring = "hello world,dzt"
print(mystring[:])
print(mystring[2:])
print(mystring[::5])
print(mystring[::-5])
```

**执行结果：**
```
hello world,dzt
llo world,dzt
hwd!
t,owh
```

---

### 字符串常用方法

#### find() 和 index() - 查找子串

`find()` 和 `index()` 都用于查找子串位置，返回子串的起始索引。区别是找不到时 `find()` 返回 -1，而 `index()` 会报错。

```python
names = "aaaasdfghjkl"

# find() 找不到返回 -1
print(names.find("g"))
print(names.find("v"))

# index() 找不到会报错
print(names.index("g"))
```

**执行结果：**
```
8
-1
8
```

---

#### count() - 统计出现次数

统计子串在字符串中出现的次数。

```python
names = "aaaasdfghjkl"

print(names.count("g"))
print(names.count("v"))
```

**执行结果：**
```
1
0
```

---

#### replace() - 替换子串

将字符串中的子串替换为新的内容，可指定替换次数。

```python
names = "aaaasdfghjkl"

# 全部替换
print(names.replace("a", "vq"))

# 只替换一次
print(names.replace("a", "vq", 1))
```

**执行结果：**
```
vvvqvqsdvqfghjkl
vaaasdfghjkl
```

---

#### split() - 分割字符串

将字符串按照指定分隔符分割成列表，默认按空白字符分割。

```python
namees = "aa aa\nsdfgh jkl"

# 默认按空白字符分割
print(namees.split())

# 按空格分割，限制分割次数
print(namees.split(" ", 1))
```

**执行结果：**
```
['aa', 'aa', 'sdfgh', 'jkl']
['aa', 'aa\nsdfgh jkl']
```

---

#### strip() - 去除空白字符

去除字符串两端的空白字符。

```python
tr = "  hello Python   "
trs = "xxxhello pythonxxx"

# 去除两端空格
print(tr.strip())

# 去除两端指定字符
print(trs.strip("x"))
```

**执行结果：**
```
  hello Python
hello python
```

---

#### upper() 和 lower() - 大小写转换

`upper()` 转大写，`lower()` 转小写。

```python
trs = "xxxhello pythonxxx"
tres = "ABC"

print(trs.upper())
print(tres.lower())
```

**执行结果：**
```
XXXHELLO PYTHONXXX
abc
```

---

#### startswith() 和 endswith() - 判断前缀后缀

判断字符串是否以指定内容开头或结尾。

```python
name = "dengzeting"

print(name.startswith("deng"))
print(name.startswith("e"))

print(name.endswith("ting"))
print(name.endswith("in"))
```

**执行结果：**
```
True
False
True
False
```

---

#### islower() 和 isupper() - 判断大小写

判断字符串是否全为小写或全为大写。

```python
name = "dengzeting"
name_upper = "ABC"

print(name.islower())
print(name.isupper())
print(name_upper.isupper())
```

**执行结果：**
```
True
False
True
```

---

#### encode() 和 decode() - 编码转换

`encode()` 将字符串转为字节，`decode()` 将字节转回字符串。

```python
st = "今天好好玩"

# 字符串转字节
print(st.encode())

# 字节转字符串
b1 = b'\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa5\xbd\xe5\xa5\xbd\xe7\x8e\xa9'
print(b1.decode())
```

**执行结果：**
```
b'\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa5\xbd\xe5\xa5\xbd\xe7\x8e\xa9'
今天好好玩
```

---

## 列表

### 列表基础

列表就是一个容器，可以放各种东西，数字、字符串、甚至另一个列表都行，而且可以随时修改。

```python
# 定义一个列表
li = ['aaa', 'bbb', 'ccc', 45, 42.5, 48]
print(li, type(li))

# 索引访问
for i in range(0, 6):
    print(li[i], end="\t")
print()

# 切片
lis = [0, 1, 2, 3, 4, 5, 6, 7, "yyy"]
print(lis[:5])
print(lis[::2])
print(lis[::-2])

# 修改元素
lis[8] = "nnn"
print(lis)

# 二维列表
grades = [[90, 99], [58, 60], [66, 99]]
print(grades[2][1])
```

**执行结果：**
```
['aaa', 'bbb', 'ccc', 45, 42.5, 48] <class 'list'>
aaa	bbb	ccc	45	42.5	48	
[0, 1, 2, 3, 4]
[0, 2, 4, 6, 'yyy']
['yyy', 5, 3, 1]
[0, 1, 2, 3, 4, 5, 6, 7, 'nnn']
99
```

---

### 列表常用方法

#### append() 方法

append()就是在列表末尾添加一个元素。

```python
nums = [1.2, 2.6, 8.9]
nums.append(100)
print(nums)
```

**执行结果：**
```
[1.2, 2.6, 8.9, 100]
```

---

### reverse() 倒序排列

将列表中的元素顺序反转。

```python
num = [1, 8, 9, 22, 10, 2, 1]

# 直接反转
num.reverse()
print(num)
```

**执行结果：**
```
[1, 2, 10, 22, 9, 8, 1]
```

---

### sort() 排序

对列表进行排序，默认升序。`reverse=True` 表示降序。

```python
li = ['r', 'a', 't', 'b']

# 根据 ASCII 编码降序排序
li.sort(reverse=True)
print(li)
```

**执行结果：**
```
['t', 'r', 'b', 'a']
```

---

## 元组、集合与字典

### 元组

元组和列表很像，但元组一旦创建就不能修改、删除或添加元素。注意如果元组只有一个元素，一定要加逗号。

```python
# 定义元组
tup = (1,)
tups = (1)
print(tup, type(tup))
print(tups, type(tups))

# 索引与切片
tup = (0, 1, 2, 3, 4, 5, 6, 7)
print(tup[0:7:3])
print(tup[0:8:3])
print(tup[-1:-8:-3])
print(tup[-1:-9:-3])
```

**执行结果：**
```
(1,) <class 'tuple'>
1 <class 'int'>
(0, 3, 6)
(0, 3, 6)
(7, 4, 1)
(7, 4, 1)
```

---

### 元组切片补充说明

结束索引要 +1 才可以覆盖到所有元素。

```python
tups = (0, 1, 2, 3)
print(tups[0:4])
print(tups[-1:-5:-1])
```

**执行结果：**
```
(0, 1, 2, 3)
(3, 2, 1, 0)
```

---

### 集合

集合最大的特点就是自动去重，而且里面的元素是无序的。

```python
# 定义集合
s = {'a', 'b', 'c', 'a'}
print(s, type(s))

# 空集合要用set()，不能用{}（{}是空字典）
data = {}
datas = set()
print(data, type(data))
print(datas, type(datas))
```

**执行结果：**
```
{'a', 'c', 'b'} <class 'set'>
{} <class 'dict'>
set() <class 'set'>
```

---

### 交集和并集

集合支持交集（两个集合的共同元素）和并集（两个集合所有元素去重合并）操作。

```python
s1 = {1, 5, 6, 9, 8, 7}
s2 = {1, 5, 15, 55, 8, 88}
s3 = {18, 58, 155, 555, 85, 885}

# 交集：使用 & 运算符
print(s1 & s2)

# 交集：使用 intersection() 方法
print(s1.intersection(s2))

# 并集：使用 | 运算符
print(s1 | s2 | s3)

# 并集：使用 union() 方法
print(s1.union(s2, s3))
```

**执行结果：**
```
{1, 8, 5}
{1, 8, 5}
{1, 5, 6, 7, 8, 9, 15, 18, 55, 58, 85, 88, 155, 555, 885}
{1, 5, 6, 7, 8, 9, 15, 18, 55, 58, 85, 88, 155, 555, 885}
```

---

### 字典

字典就是键值对存储，通过键找值，速度很快。

```python
# 定义字典
info = {
    "name": "dzt",
    "python": 98
}
print(info, type(info))

# 通过键访问值
print(info["python"])

# 用get()方法安全访问，找不到不会报错
print(info.get("语文"))
print(info.get("语文", "键名不存在"))

# 添加或修改
info["age"] = 20
info["python"] = 99
print(info)

# 删除
info.pop("age")
print(info)
```

**执行结果：**
```
{'name': 'dzt', 'python': 98} <class 'dict'>
98
None
键名不存在
{'name': 'dzt', 'python': 99, 'age': 20}
{'name': 'dzt', 'python': 99}
```

---

### 字典常用操作

#### get() 方法安全访问

用 `get()` 方法访问字典比直接用键名安全，因为找不到不会报错，还可以自定义找不到时的返回值。

```python
info = {
    "name": "dzt",
    "python": 98
}

# 直接访问键名，找不到会报错
# print(info["语文"])  # 报错：KeyError

# 使用 get() 访问，找不到返回 None
print(info.get("语文"))  # None

# 找不到时返回自定义值
print(info.get("语文", "键名不存在"))  # 键名不存在
```

**执行结果：**
```
None
键名不存在
```

---

#### 添加和修改元素

字典的键名不存在时是添加，存在时是修改。

```python
info = {
    "name": "dzt",
    "python": 98
}

# 键名不存在，添加新元素
info["age"] = 20

# 键名存在，修改原有值
info["python"] = 99

print(info)
```

**执行结果：**
```
{'name': 'dzt', 'python': 99, 'age': 20}
```

---

#### 删除元素

使用 `pop()` 方法删除指定键名的元素，删除不存在的键会报错，但可以设置默认值避免报错。

```python
info = {
    "name": "dzt",
    "python": 99,
    "age": 20
}

# 删除指定键名的元素
info.pop("age")
print(info)

# 删除不存在的键时，设置默认值避免报错
info.pop("语文", "不存在")
print(info)
```

**执行结果：**
```
{'name': 'dzt', 'python': 99}
{'name': 'dzt', 'python': 99}
```

---

#### keys()、values()、items() 方法

这三个方法分别用来获取字典的所有键、所有值、所有键值对。

```python
info = {
    "name": "dzt",
    "python": 98
}

# 获取所有键
print(info.keys())

# 获取所有值
print(info.values())

# 获取所有键值对，每一对是一个元组
print(info.items())
```

**执行结果：**
```
dict_keys(['name', 'python'])
dict_values([98])
dict_items([('name', 'dzt'), ('python', 98)])
```

---

## 异常处理

### 基本异常处理

异常处理就是程序出错时，我们捕获这个错误，不让程序崩溃，而是按我们的方式处理。

```python
# 捕获所有异常
try:
    num = int(input("请输入一个数字："))
    print(num)
except Exception:
    print("输入错误")
```

**执行结果（示例）：**
```
请输入一个数字：abc
输入错误
```

---

### 捕获特定类型的异常

可以针对不同类型的错误使用不同的 except 分支来处理。

```python
try:
    print("1" > 1)
except TypeError:
    print("类型错误")
except ZeroDivisionError:
    print("除数不能为零")
except ValueError:
    print("数值错误")
```

---

### 捕获异常的具体信息

使用 `as` 关键字可以获取异常的具体描述信息，方便调试。

```python
try:
    num = int(input("请输入一个数字："))
except ValueError as e:
    print(e)
```

**执行结果（示例）：**
```
请输入一个数字：abc
invalid literal for int() with base 10: 'abc'
```

---

### else 和 finally

- `else`：只有在 try 块中没有发生异常时才会执行
- `finally`：无论是否发生异常，都会执行

```python
try:
    num = int(input("请输入一个数字："))
except ValueError as e:
    print(e)
else:
    print(num, type(num))
finally:
    print("一定会执行")
```

**执行结果（示例）：**
```
请输入一个数字：123
123 <class 'int'>
一定会执行
```

---

### raise 主动抛出异常

使用 `raise` 关键字可以主动抛出异常。

```python
e = Exception("余额不足")
raise e
```

**执行结果：**
```
Traceback (most recent call last):
    ...
Exception: 余额不足
```

---

## 类与对象

### 类的定义

类就是一个模板，对象就是根据这个模板创建出来的具体东西。

```python
# 最简单的类
class Car:
    pass

car1 = Car()
print(car1)
```

---

### 构造方法 __init__

__init__就是创建对象时自动调用的方法，通常用来初始化属性。

```python
class Car:
    wheel_count = 4
    
    def __init__(self):
        print("我是__init__方法")
        self.color = "红色"
        self.brand = "保时捷"
    
    def start(self):
        print(f"{self.color} 的 {self.brand} 启动了！")

car1 = Car()
car1.start()
```

**执行结果：**
```
我是__init__方法
红色 的 保时捷 启动了！
```

---

### 析构方法 __del__

__del__就是对象被销毁时自动执行的方法，当后面的代码不再使用这个类时，程序就会执行这样的操作。

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __del__(self):
        print(f"{self.brand} 被销毁了")

car1 = Car("保时捷")
```

**执行结果：**
```
保时捷 被销毁了
```

---

### 私有属性

在属性名前面加两个下划线 `__`，就成了私有属性，外面不能直接访问。如果非要访问，可以用 `_类名__属性名` 强制拿到，但不推荐这样做。

```python
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def check_balance(self):
        print(f"{self.name}   余额 {self.__balance}")

account = BankAccount("dzt", 147258)
account.check_balance()

# 尝试访问私有属性会报错
# print(account.__balance)

# 强制访问私有属性（不推荐）
print(account._BankAccount__balance)
```

**执行结果：**
```
dzt   余额 147258
147258
```

---

### 继承

继承就是子类可以直接拥有父类的属性和方法，不用重新写。子类还能加自己的新功能。继承还可以多层传递，子类能用到爷爷类的属性和方法。

```python
# 父类的父类：生物（所有生物的共性）
class LivingThing():
    feature = "有生命"

    def breathe(self):
        print("有呼吸")

# 父类：动物
class Animal(LivingThing):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} 在吃东西")

    def sleep(self):
        print(f"{self.name} 在睡觉")

# 子类：狗类，继承动物类
class Dog(Animal):
    def bark(self):
        print("小狗哇哇叫")

dog1 = Dog("旺财", 2)

# 继承了父类的公有属性
print(dog1.name)

dog1.eat()
dog1.bark()

# 访问间接继承自父类的属性和方法
print(dog1.feature)
dog1.breathe()
```

**执行结果：**
```
旺财
旺财 在吃东西
小狗哇哇叫
有生命
有呼吸
```

---

### 方法重写与 super()

子类可以重写父类的方法，也就是重新定义一个同名方法。如果想在重写的同时还保留父类的逻辑，就用 `super()` 来调用父类的方法。

```python
class Animal:
    def make_sound(self):
        print("动物发出声音")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("喵喵喵")

cat = Cat()
cat.make_sound()
```

**执行结果：**
```
动物发出声音
喵喵喵
```

---

### 多继承

一个子类可以同时继承多个父类，这样就能同时拥有多个父类的功能。

```python
# 父类1：手表类
class Watch:
    def show_time(self):
        print("当前时间：15:00")

# 父类2：健康设备类
class HeathDevice:
    def check_heart_rate(self):
        print("心率检测：75次/秒")

# 子类：智能手表类，继承两个父类
class SmartWatch(Watch, HeathDevice):
    pass

smartWatch = SmartWatch()
smartWatch.show_time()
smartWatch.check_heart_rate()
```

**执行结果：**
```
当前时间：15:00
心率检测：75次/秒
```

---

### 多继承的调用顺序

当多个父类有同名方法时，子类会优先调用排在最前面的父类的方法。也可以通过 `父类名.方法(对象)` 的方式指定调用哪个父类的方法。

```python
class Phone:
    def take_photo(self):
        print("手机拍照：普通画质")

class Camera:
    def take_photo(self):
        print("相机拍照：高清画质")

class CameraPhone(Phone, Camera):
    pass

# 优先执行最前面参数的父类
cp = CameraPhone()
cp.take_photo()
Camera.take_photo(cp)
```

**执行结果：**
```
手机拍照：普通画质
相机拍照：高清画质
```

---

## 常用内置函数

### type() 函数

type() 是 Python 内置函数，用来查看数据是什么类型的。

参数说明：
- 数据：你想要查看类型的数据

```python
print(type(123))
print(type("hello"))
```

**执行结果：**
```
<class 'int'>
<class 'str'>
```

---

### int() 函数

int() 是 Python 内置函数，用来把其他类型转成整数。

参数说明：
- 数据：你想要转换的数据

```python
print(int("123"))
print(int(3.14))
```

**执行结果：**
```
123
3
```

---

### str() 函数

str() 是 Python 内置函数，用来把其他类型转成字符串。

参数说明：
- 数据：你想要转换的数据

```python
print(str(123))
print(str(3.14))
```

**执行结果：**
```
123
3.14
```

---

### len() 函数

len() 是 Python 内置函数，用来计算长度，字符串、列表、元组、字典等都能用。

参数说明：
- 数据：你想要计算长度的数据

```python
print(len("hello"))
print(len([1, 2, 3]))
```

**执行结果：**
```
5
3
```

---

### max() 和 min() 函数

max() 是 Python 内置函数，用来找最大值。
min() 是 Python 内置函数，用来找最小值。

```python
print(max(1, 5, 3, 9, 2))
print(min(1, 5, 3, 9, 2))
```

**执行结果：**
```
9
1
```

---

### sum() 函数

sum() 是 Python 内置函数，用来求和。

参数说明：
- 可迭代对象：比如列表、元组等

```python
print(sum([1, 2, 3, 4, 5]))
```

**执行结果：**
```
15
```

---


# Pandas 学习笔记

> 底层基于 [Numpy学习笔记](./Numpy学习笔记.md) ｜ 基础语法见 [Python学习笔记](./Python学习笔记.md)

## 目录

- [Series 的创建](#series-的创建)
  - [从列表创建](#从列表创建)
  - [自定义索引](#自定义索引)
  - [指定 name](#指定-name)
  - [从字典创建](#从字典创建)
- [Series 的属性](#series-的属性)
- [Series 的索引与访问](#series-的索引与访问)
  - [显式索引 loc / at](#显式索引-loc--at)
  - [隐式索引 iloc / iat](#隐式索引-iloc--iat)
  - [直接索引](#直接索引)
  - [布尔索引](#布尔索引)
- [Series 的统计函数](#series-的统计函数)
- [Series 的排序](#series-的排序)
- [Series 的去重](#series-的去重)
- [DataFrame 的创建](#dataframe-的创建)
  - [从 Series 字典创建](#从-series-字典创建)
  - [从字典创建](#从字典创建)
  - [用 date_range 生成日期索引](#用-date_range-生成日期索引)
- [DataFrame 的属性](#dataframe-的属性)
- [DataFrame 的索引与访问](#dataframe-的索引与访问)
  - [获取行 loc / iloc](#获取行-loc--iloc)
  - [获取列](#获取列)
  - [获取单个元素 at / iat](#获取单个元素-at--iat)
  - [布尔索引](#dataframe-的布尔索引)
- [通用查看方法](#通用查看方法)
- [通用缺失值与成员检查](#通用缺失值与成员检查)
- [通用统计函数](#通用统计函数)
- [DataFrame 的列操作](#dataframe-的列操作)
- [DataFrame 的累计函数](#dataframe-的累计函数)
- [DataFrame 的函数应用](#dataframe-的函数应用)
- [DataFrame 的分组聚合](#dataframe-的分组聚合)
- [通用排序](#通用排序)
- [通用去重与替换](#通用去重与替换)
- [DataFrame 的数据转换](#dataframe-的数据转换)

---

## Series 的创建

Series 是 Pandas 中最基本的一维数据结构，可以理解为一个带索引的数组。

### 从列表创建

最简单的方式是用 `pd.Series()` 把 Python 列表转成 Series，默认索引从 0 开始。

```python
import pandas as pd
import numpy as np

s = pd.Series([10, 2, 3, 4, 5])
print(s)
```

**执行结果：**
```
0    10
1     2
2     3
3     4
4     5
dtype: int64
```

---

### 自定义索引

可以通过 `index` 参数给每个元素指定一个标签索引，方便按名称访问。

```python
s = pd.Series([10, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
```

**执行结果：**
```
a    10
b     2
c     3
d     4
e     5
dtype: int64
```

---

### 指定 name

`name` 参数可以给 Series 起个名字，在 DataFrame 中会变成列名。

```python
s = pd.Series([10, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'], name='月')
print(s)
```

**执行结果：**
```
a    10
b     2
c     3
d     4
e     5
Name: 月, dtype: int64
```

---

### 从字典创建

用字典创建 Series 时，字典的 key 会自动变成索引，value 变成数据。还可以通过 `index` 参数筛选想要的键。

```python
s = pd.Series({
    "a": 1,
    "b": 8,
    "c": 4,
})
print(s)
```

**执行结果：**
```
a    1
b    8
c    4
dtype: int64
```

```python
s1 = pd.Series(s, index=["a", "c"])
print(s1)
```

**执行结果：**
```
a    1
c    4
dtype: int64
```

---

## Series 的属性

每个 Series 都有一些常用属性，可以帮我们了解数据的基本信息。

| 属性 | 说明 |
|------|------|
| index | Series 的索引 |
| values | Series 的值（返回 ndarray） |
| dtype | 元素的数据类型 |
| name | Series 的名称 |
| shape | 形状，一维 Series 返回 (n,) |
| ndim | 维度数，Series 固定为 1 |
| size | 元素的总个数 |

```python
print(s)
print(s.index, s.values)
s.name = 'test'
print(s.dtype, s.name)
print(s.shape, s.ndim, s.size)
```

**执行结果：**
```
a    1
b    8
c    4
dtype: int64
Index(['a', 'b', 'c'], dtype='object') [1 8 4]
int64 test
(3,) 1 3
```

---

## Series 的索引与访问

Series 支持两种索引方式：显式索引（用标签）和隐式索引（用位置），推荐使用 `loc` 和 `iloc` 来明确区分。

### 显式索引 loc / at

`loc` 用标签索引，支持切片；`at` 用标签取单个值，不支持切片。

```python
print(s.loc['a':'b'])
print(s.at['a'])
```

**执行结果：**
```
a    1
b    8
Name: test, dtype: int64
4
```

---

### 隐式索引 iloc / iat

`iloc` 用位置索引，和 Python 列表的索引一样；`iat` 用位置取单个值，不支持切片。

```python
print(s.iloc[2])
print(s.iat[2])
```

**执行结果：**
```
4
4
```

---

### 直接索引

可以直接用标签索引访问元素，但用整数位置索引会报警告，推荐用 `loc` / `iloc`。

```python
print(s['a'])
```

**执行结果：**
```
1
```

---

### 布尔索引

和 Numpy 类似，可以用条件表达式筛选满足条件的元素。

```python
print(s[s < 5])
```

**执行结果：**
```
a    1
c    4
Name: test, dtype: int64
```

---

## Series 的统计函数

Series 提供了丰富的统计函数，和 Numpy 类似，但会自动忽略缺失值。

### keys() / index

`keys()` 方法和 `index` 属性都可以获取 Series 的索引。

```python
s = pd.Series([1, np.nan, None, 9, 6, 10], index=['A', 'B', 'C', 'D', 'E', 'F'], name="test")
print(s.keys())
print(s.index)
```

**执行结果：**
```
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
```

---

### 常用统计量

```python
print(s.mean(), s.max(), s.min())
print(s.sum(), s.median())
print(s.std(), s.var())
```

**执行结果：**
```
6.5 10.0 1.0
26.0 7.5
4.041451884327381 16.333333333333332
```

---

### 分位数 quantile()

`quantile()` 计算指定分位数的值，参数是 0 到 1 之间的小数。

```python
s.quantile(0.75)
```

**执行结果：**
```
9.25
```

---

### 众数 mode()

`mode()` 返回出现次数最多的值，可能有多个众数。

```python
s['G'] = 10
print(s.mode())
```

**执行结果：**
```
0    10.0
Name: test, dtype: float64
```

---

## Series 的排序

### 按值排序 sort_values()

`sort_values()` 按元素的值排序，缺失值默认排在最后。

```python
s.sort_values()
```

**执行结果：**
```
A     1.0
E     6.0
D     9.0
F    10.0
B     NaN
C     NaN
Name: test, dtype: float64
```

---

### 按索引排序 sort_index()

`sort_index()` 按索引标签排序。

```python
s.sort_index()
```

**执行结果：**
```
A     1.0
B     NaN
C     NaN
D     9.0
E     6.0
F    10.0
G    10.0
Name: test, dtype: float64
```

---

## Series 的去重

### unique()

`unique()` 返回去重后的值数组（ndarray），包含 NaN。

```python
s.unique()
```

**执行结果：**
```
array([ 1., nan,  9.,  6., 10.])
```

---

### nunique()

`nunique()` 返回唯一值的个数，默认不统计 NaN。

```python
print(s.nunique())
```

**执行结果：**
```
4
```

---

## DataFrame 的创建

DataFrame 是 Pandas 中最核心的二维数据结构，可以理解为一个表格，有行索引和列标签。

### 从 Series 字典创建

把多个 Series 放进字典，每个 Series 变成一列，字典的 key 变成列名。

```python
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([6, 7, 8, 9, 10])

pd.DataFrame({
    "第一列": s1,
    "第二列": s2,
})
```

**执行结果：**
```
   第一列  第二列
0    1    6
1    2    7
2    3    8
3    4    9
4    5   10
```

---

### 从字典创建

用字典创建 DataFrame，字典的 key 是列名，value 是该列的数据。可以通过 `index` 指定行索引，`columns` 指定列顺序。

```python
df = pd.DataFrame({
    "name": ['tom', 'tom', 'sse', 'srr', 'dd', 're'],
    "age": [15, 15, 18, 18, 19, 20],
    "score": [52.3, 52.3, 60.2, 85, 42.5, 55]
}, index=[1, 2, 3, 4, 5, 6], columns=["name", "score", "age"])
df
```

**执行结果：**
```
  name  score  age
1  tom   52.3   15
2  tom   52.3   15
3  sse   60.2   18
4  srr   85.0   18
5   dd   42.5   19
6   re   55.0   20
```

注意：`columns` 参数不仅指定了列的顺序，还可以筛选列。

---

### 用 date_range 生成日期索引

`pd.date_range()` 可以快速生成一段连续的日期序列，常用于创建时间相关的 DataFrame。参数 `start` 和 `end` 指定起止日期，也可以用 `periods` 指定个数。

```python
dates = pd.date_range("2026-01-01", "2026-01-05")
print(dates)
```

**执行结果：**
```
DatetimeIndex(['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04',
               '2026-01-05'],
              dtype='datetime64[ns]', freq='D')
```

用生成的日期作为行索引创建 DataFrame：

```python
df_dates = pd.DataFrame({
    "气温": [3, 5, 8, 6, 4],
    "天气": ["晴", "多云", "晴", "阴", "雨"]
}, index=dates)
df_dates
```

**执行结果：**
```
            气温  天气
2026-01-01   3   晴
2026-01-02   5  多云
2026-01-03   8   晴
2026-01-04   6   阴
2026-01-05   4   雨
```

---

## DataFrame 的属性

每个 DataFrame 都有一些常用属性，帮我们了解表格的基本信息。

| 属性 | 说明 |
|------|------|
| index | 行索引 |
| columns | 列标签 |
| values | 所有值（返回 ndarray） |
| ndim | 维度数，DataFrame 固定为 2 |
| shape | 形状，(行数, 列数) |
| size | 元素的总个数（行数 × 列数） |
| dtypes | 每列的数据类型 |
| T | 转置（行变列，列变行） |

```python
print("行索引：")
print(df.index)
print("列标签：")
print(df.columns)
print("值")
print(df.values)
```

**执行结果：**
```
行索引：
Index([1, 2, 3, 4, 5, 6], dtype='int64')
列标签：
Index(['name', 'score', 'age'], dtype='object')
值
[['tom' 52.3 15]
 ['tom' 52.3 15]
 ['sse' 60.2 18]
 ['srr' 85.0 18]
 ['dd' 42.5 19]
 ['re' 55.0 20]]
```

```python
print("维度：", df.ndim)
print("形状:", df.shape)
print("元素个数:", df.size)
print("数据类型：", df.dtypes)
```

**执行结果：**
```
维度： 2
形状: (6, 3)
元素个数: 18
数据类型： name      object
score    float64
age        int64
dtype: object
```

---

### tolist()

`tolist()` 可以将行索引或列标签从 Index 对象转为 Python 列表，方便后续遍历或判断。

```python
print(df.columns.tolist())
print(df.index.tolist())
```

**执行结果：**
```
['name', 'score', 'age']
[1, 2, 3, 4, 5, 6]
```

---

## DataFrame 的索引与访问

DataFrame 支持按行、按列、按元素访问，同样区分显式索引和隐式索引。

### 获取行 loc / iloc

`loc` 用标签索引获取行，`iloc` 用位置索引获取行。

```python
print(df.loc[4])
print(df.iloc[3])
```

**执行结果：**
```
name      srr
score    85.0
age        18
Name: 4, dtype: object
name      srr
score    85.0
age        18
Name: 4, dtype: object
```

---

### 获取列

获取单列有两种方式：`df['列名']` 和 `df.列名`，返回的都是 Series。

```python
print(df['name'])
print(type(df['name']))
```

**执行结果：**
```
1    tom
2    tom
3    sse
4    srr
5     dd
6     re
Name: name, dtype: object
<class 'pandas.core.series.Series'>
```

用 `df[['列名']]`（双层括号）获取的是 DataFrame，不是 Series：

```python
print(df[['name']])
print(type(df[['name']]))
```

**执行结果：**
```
  name
1  tom
2  tom
3  sse
4  srr
5   dd
6   re
<class 'pandas.core.frame.DataFrame'>
```

也可以一次获取多列：

```python
df[['name', 'score']]
```

**执行结果：**
```
  name  score
1  tom   52.3
2  tom   52.3
3  sse   60.2
4  srr   85.0
5   dd   42.5
6   re   55.0
```

用 `loc` / `iloc` 也可以获取列：

```python
print(df.loc[:, 'name'])
print(df.iloc[:, 0])
```

**执行结果：**
```
1    tom
2    tom
3    sse
4    srr
5     dd
6     re
Name: name, dtype: object
1    tom
2    tom
3    sse
4    srr
5     dd
6     re
Name: name, dtype: object
```

---

### 获取单个元素 at / iat

`at` 用标签取单个值，`iat` 用位置取单个值。`loc` 和 `iloc` 也能取单个值，但 `at` / `iat` 速度更快。

```python
print(df.at[3, 'score'])
print(df.iat[2, 1])
print(df.loc[3, 'score'])
print(df.iloc[2, 1])
```

**执行结果：**
```
60.2
60.2
60.2
60.2
```

---

### DataFrame 的布尔索引

和 Numpy 类似，DataFrame 也支持布尔索引筛选数据。

#### 单条件筛选

```python
df[df.score > 55]
```

**执行结果：**
```
  name  score  age
3  sse   60.2   18
4  srr   85.0   18
```

---

#### 多条件筛选

多条件用 `&`（与）或 `|`（或）连接，每个条件要加括号。

```python
df[(df.score > 60) & (df.age < 40)]
```

**执行结果：**
```
  name  score  age
3  sse   60.2   18
4  srr   85.0   18
```

---

## 通用查看方法

以下方法 Series 和 DataFrame 都支持，用法一致。

### info()

`info()` 打印数据概览信息，包括行数、列名、每列非空值个数和数据类型，以及内存占用。是拿到数据后第一步最常用的方法。

```python
df.info()
```

**执行结果：**
```
<class 'pandas.core.frame.DataFrame'>
Index: 6 entries, 1 to 6
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    6 non-null      object
 1   score   6 non-null      float64
 2   age     6 non-null      int64
dtypes: float64(1), int64(1), object(1)
memory usage: 192.0+ bytes
```

---

### head() / tail()

`head()` 查看前几行，`tail()` 查看后几行，默认 5 行。Series 和 DataFrame 都可用。

```python
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8])
print(s.head(3))
```

**执行结果：**
```
0    1
1    2
2    3
dtype: int64
```

```python
print(df.head(2))
print(df.tail(2))
```

**执行结果：**
```
  name  score  age
1  tom   52.3   15
2  tom   52.3   15
  name  score  age
5   dd   42.5   19
6   re   55.0   20
```

---

### sample()

`sample()` 随机抽取指定行数的数据，用于随机抽样。

```python
df.sample(3)
```

**执行结果：**
```
  name  score  age
2  tom   52.3   15
5   dd   42.5   19
1  tom   52.3   15
```

---

## 通用缺失值与成员检查

以下方法 Series 和 DataFrame 都支持，Series 返回布尔 Series，DataFrame 返回布尔 DataFrame。

### isna()

`isna()` 逐个检查元素是否为缺失值。

**Series 用法：**

```python
s = pd.Series([1, np.nan, None, 9, 6, 10], index=['A', 'B', 'C', 'D', 'E', 'F'], name="test")
s.isna()
```

**执行结果：**
```
A    False
B     True
C     True
D    False
E    False
F    False
Name: test, dtype: bool
```

**DataFrame 用法：**

```python
print(df.isna())
```

**执行结果：**
```
    name  score    age
1  False  False  False
2  False  False  False
3  False  False  False
4  False  False  False
5  False  False  False
6  False  False  False
```

---

### isna().sum() 统计缺失值个数

`isna()` 返回布尔结果，再对每列求 `sum()` 就能统计每列有多少个缺失值，是数据清洗时最常用的组合。

```python
df_na = pd.DataFrame({
    "A": [1, np.nan, 3],
    "B": [np.nan, np.nan, 6],
    "C": [7, 8, 9]
})
print(df_na.isna().sum())
```

**执行结果：**
```
A    1
B    2
C    0
dtype: int64
```

---

### isin()

`isin()` 检查每个元素是否在给定的集合中。

**Series 用法：**

```python
s.isin([12, 4, 9, 10])
```

**执行结果：**
```
A    False
B    False
C    False
D     True
E    False
F     True
Name: test, dtype: bool
```

**DataFrame 用法：**

```python
print(df.isin(['jack', 20]))
```

**执行结果：**
```
    name  score    age
1  False  False  False
2  False  False  False
3  False  False  False
4  False  False  False
5  False  False  False
6  False  False   True
```

---

## 通用统计函数

以下方法 Series 和 DataFrame 都支持。DataFrame 默认按列计算，可通过 `axis` 参数切换。

> **axis 参数说明：** `axis=0`（默认）按列方向计算（每列一个结果），`axis=1` 按行方向计算（每行一个结果）。

### describe()

`describe()` 一次性查看描述性统计信息，包括计数、均值、标准差、最值和分位数。缺失值不参与统计。

**Series 用法：**

```python
s.describe()
```

**执行结果：**
```
count     4.000000
mean      6.500000
std       4.041452
min       1.000000
25%       4.750000
50%       7.500000
75%       9.250000
max      10.000000
Name: test, dtype: float64
```

**DataFrame 用法：**

```python
print(df.describe())
```

**执行结果：**
```
           score        age
count   6.000000   6.000000
mean   57.883333  17.500000
std    14.477488   2.073644
min    42.500000  15.000000
25%    52.300000  15.750000
50%    53.650000  18.000000
75%    58.900000  18.750000
max    85.000000  20.000000
```

---

### count()

`count()` 返回非缺失值的个数。Series 返回一个整数，DataFrame 返回每列的计数。

**Series 用法：**

```python
print(s.count())
```

**执行结果：**
```
4
```

**DataFrame 用法：**

```python
print(df.count())
```

**执行结果：**
```
name     6
score    6
age      6
dtype: int64
```

---

### value_counts()

`value_counts()` 统计每个值出现的次数，缺失值会被忽略。

**Series 用法：**

```python
print(s.value_counts())
```

**执行结果：**
```
test
10.0    2
1.0     1
9.0     1
6.0     1
Name: count, dtype: int64
```

**DataFrame 用法：**

DataFrame 的 `value_counts()` 统计每行出现的次数，按所有列组合去重。

```python
print(df.value_counts())
```

**执行结果：**
```
name  score  age
tom   52.3   15     2
dd    42.5   19     1
re    55.0   20     1
srr   85.0   18     1
sse   60.2   18     1
Name: count, dtype: int64
```

---

### agg() 聚合多个统计量

`agg()` 可以同时对一列或多列应用多个聚合函数，比单独调用更简洁。传入函数名的列表即可。

```python
df3 = pd.DataFrame({
    "语文": [80, 75, 90, 65, 88],
    "数学": [85, 92, 78, 70, 95]
}, index=['甲', '乙', '丙', '丁', '戊'])

df3[['语文', '数学']].agg(['mean', 'max', 'min'])
```

**执行结果：**
```
      语文   数学
mean  79.6  84.0
max   90.0  95.0
min   65.0  70.0
```

还可以对不同的列应用不同的聚合函数，用字典指定：

```python
df3.agg({'语文': ['mean', 'max'], '数学': 'sum'})
```

**执行结果：**
```
         语文   数学
mean   79.6  NaN
max    90.0  NaN
sum     NaN  420
```

---

### round() 四舍五入

`round()` 对数值进行四舍五入，参数指定保留的小数位数。可以作用于 Series 和 DataFrame。

```python
s_r = pd.Series([3.14159, 2.71828, 1.41421])
print(s_r.round(2))
```

**执行结果：**
```
0    3.14
1    2.72
2    1.41
dtype: float64
```

DataFrame 也可以按列指定不同的小数位数：

```python
df3.round({'语文': 1, '数学': 0})
```

**执行结果：**
```
    语文   数学
甲  80.0  85.0
乙  75.0  92.0
丙  90.0  78.0
丁  65.0  70.0
戊  88.0  95.0
```

---

## DataFrame 的列操作

### 新增列

直接用 `df['新列名'] = ...` 就可以添加新列，右边可以是标量、列表、Series 或表达式计算结果。

```python
df['score_100'] = df['score'] * 100 / 100
df['pass'] = df['score'] >= 60
df
```

**执行结果：**
```
  name  score  age  score_100   pass
1  tom   52.3   15       52.3  False
2  tom   52.3   15       52.3  False
3  sse   60.2   18       60.2   True
4  srr   85.0   18       85.0   True
5   dd   42.5   19       42.5  False
6   re   55.0   20       55.0  False
```

多列组合计算也很常见，比如计算两科成绩的平均分和总分：

```python
df2 = pd.DataFrame({
    "语文": [80, 75, 90],
    "数学": [85, 92, 78]
}, index=['甲', '乙', '丙'])
df2['平均分'] = df2[['语文', '数学']].mean(axis=1).round(1)
df2['总分'] = df2[['语文', '数学']].sum(axis=1)
df2
```

**执行结果：**
```
   语文  数学  平均分   总分
甲  80  85  82.5  165
乙  75  92  83.5  167
丙  90  78  84.0  168
```

---

### 删除列 drop()

`drop()` 可以删除指定列，`columns` 参数指定要删除的列名，`inplace=True` 时原地修改。

```python
df2.drop(columns=['总分'])
```

**执行结果：**
```
   语文  数学  平均分
甲  80  85  82.5
乙  75  92  83.5
丙  90  78  84.0
```

---

## DataFrame 的累计函数

### 累计和 cumsum()

`cumsum()` 从上到下逐行累加，字符串列会拼接。

```python
df[['name', 'score', 'age']].cumsum()
```

**执行结果：**
```
               name  score  age
1               tom   52.3   15
2            tomtom  104.6   30
3         tomtomsse  164.8   48
4      tomtomssesrr  249.8   66
5    tomtomssesrrdd  292.3   85
6  tomtomssesrrddre  347.3  105
```

---

### 累计最大值 cummax()

`cummax()` 从上到下逐行取当前最大值。

```python
df[['score', 'age']].cummax()
```

**执行结果：**
```
   score  age
1   52.3   15
2   52.3   15
3   60.2   18
4   85.0   18
5   85.0   19
6   85.0   20
```

---

### 累计最小值 cummin()

`cummin()` 从上到下逐行取当前最小值，可以通过 `axis` 参数指定按行或按列。

```python
df[['score', 'age']].cummin(axis=0)
```

**执行结果：**
```
   score  age
1   52.3   15
2   52.3   15
3   52.3   15
4   52.3   15
5   42.5   15
6   42.5   15
```

---

## DataFrame 的函数应用

### apply()

`apply()` 可以对 Series 或 DataFrame 的每一列（或每一行）应用一个自定义函数，非常灵活。

#### 对 Series 使用 apply

对 Series 使用时，函数作用于每个元素：

```python
def grade(score):
    if score >= 90:
        return '优秀'
    elif score >= 80:
        return '良好'
    elif score >= 60:
        return '及格'
    else:
        return '不及格'

s_app = pd.Series([95, 82, 73, 55, 88])
print(s_app.apply(grade))
```

**执行结果：**
```
0    优秀
1    良好
2    及格
3    不及格
4    良好
dtype: object
```

也可以用 lambda 表达式简化：

```python
print(s_app.apply(lambda x: '高分' if x >= 80 else '低分'))
```

**执行结果：**
```
0    高分
1    高分
2    低分
3    低分
4    高分
dtype: object
```

---

#### 对 DataFrame 使用 apply

对 DataFrame 使用时，默认按列（`axis=0`）将每列传给函数；设置 `axis=1` 则按行传入。

```python
df4 = pd.DataFrame({
    "语文": [80, 75, 90],
    "数学": [85, 92, 78]
}, index=['甲', '乙', '丙'])

print(df4.apply(lambda col: col.max() - col.min(), axis=0))
```

**执行结果：**
```
语文    15
数学    14
dtype: int64
```

```python
print(df4.apply(lambda row: f"语文{row['语文']}/数学{row['数学']}", axis=1))
```

**执行结果：**
```
甲    语文80/数学85
乙    语文75/数学92
丙    语文90/数学78
dtype: object
```

---

## DataFrame 的分组聚合

### groupby()

`groupby()` 按某列的值将数据分组，然后对每组分别进行聚合运算。这是数据分析中最核心的操作之一。

基本流程：**拆分（split）→ 应用（apply）→ 合并（combine）**

```python
df5 = pd.DataFrame({
    "班级": ["A", "A", "B", "B", "A", "B"],
    "姓名": ["甲", "乙", "丙", "丁", "戊", "己"],
    "语文": [80, 75, 90, 65, 88, 72],
    "数学": [85, 92, 78, 70, 95, 88]
})

df5.groupby("班级")["语文"].mean()
```

**执行结果：**
```
班级
A    81.0
B    81.0
Name: 语文, dtype: float64
```

---

### groupby() + agg() 命名聚合

`groupby()` 配合 `agg()` 可以同时计算多个统计量，并用命名聚合给结果列起名字，格式为 `新列名=('原列名', '函数名')`。

```python
df5.groupby("班级").agg(
    语文均分=('语文', 'mean'),
    语文最高=('语文', 'max'),
    数学总分=('数学', 'sum'),
    数学均分=('数学', 'mean')
).round(1)
```

**执行结果：**
```
    语文均分  语文最高  数学总分  数学均分
班级
A    81.0     88    272   90.7
B    81.0     90    236   78.7
```

---

### groupby() + 多种聚合

也可以用列表形式对多列同时应用多种聚合函数：

```python
df5.groupby("班级")[["语文", "数学"]].agg(["mean", "max", "min"])
```

**执行结果：**
```
       语文                  数学
      mean  max min   mean  max min
班级
A    81.0   88  75   90.7   95  85
B    81.0   90  65   78.7   88  70
```

---

### reset_index()

`groupby()` 之后，分组列会变成索引。`reset_index()` 可以把索引重新变回普通列，方便后续处理。

```python
result = df5.groupby("班级")["语文"].mean()
print(result)
print("---")
print(result.reset_index())
```

**执行结果：**
```
班级
A    81.0
B    81.0
Name: 语文, dtype: float64
---
  班级    语文
0  A  81.0
1  B  81.0
```

---

## 通用排序

以下方法 Series 和 DataFrame 都支持。

### 按索引排序 sort_index()

`sort_index()` 按行索引排序，`ascending=False` 降序。

```python
print(df.sort_index(ascending=False))
```

**执行结果：**
```
  name  score  age
6   re   55.0   20
5   dd   42.5   19
4  srr   85.0   18
3  sse   60.2   18
2  tom   52.3   15
1  tom   52.3   15
```

---

### 按值排序 sort_values()

`sort_values()` 按指定列的值排序，`by` 参数指定排序列，`ascending` 参数指定升序或降序。

**Series 用法：**

```python
s.sort_values()
```

**执行结果：**
```
A     1.0
E     6.0
D     9.0
F    10.0
B     NaN
C     NaN
Name: test, dtype: float64
```

**DataFrame 用法：**

```python
print(df.sort_values(by=['score', 'age'], ascending=[True, False]))
```

**执行结果：**
```
  name  score  age
5   dd   42.5   19
1  tom   52.3   15
2  tom   52.3   15
6   re   55.0   20
3  sse   60.2   18
4  srr   85.0   18
```

---

### nlargest() / nsmallest()

`nlargest()` 获取指定列值最大的 n 行，`nsmallest()` 获取最小的 n 行。

```python
df.nlargest(2, columns=['score', 'age'])
```

**执行结果：**
```
  name  score  age
4  srr   85.0   18
3  sse   60.2   18
```

```python
df.nsmallest(2, columns=['score', 'age'])
```

**执行结果：**
```
  name  score  age
5   dd   42.5   19
1  tom   52.3   15
```

---

## 通用去重与替换

以下方法 Series 和 DataFrame 都支持。

### drop_duplicates()

`drop_duplicates()` 去除重复值/行，保留第一次出现的。

**Series 用法：**

```python
s.drop_duplicates()
```

**执行结果：**
```
A     1.0
B     NaN
D     9.0
E     6.0
F    10.0
Name: test, dtype: float64
```

**DataFrame 用法：**

```python
print(df.drop_duplicates())
```

**执行结果：**
```
  name  score  age
1  tom   52.3   15
3  sse   60.2   18
4  srr   85.0   18
5   dd   42.5   19
6   re   55.0   20
```

---

### duplicated()

`duplicated()` 返回布尔 Series，标记每行是否是重复行。

```python
print(df.duplicated())
```

**执行结果：**
```
1    False
2     True
3    False
4    False
5    False
6    False
dtype: bool
```

---

### replace()

`replace()` 将指定值替换为新值，不修改原数据。

```python
print(df.score.replace(52.3, 10))
```

**执行结果：**
```
1    10.0
2    10.0
3    60.2
4    85.0
5    42.5
6    55.0
Name: score, dtype: float64
```

---

## DataFrame 的数据转换

### to_dict()

`to_dict()` 将 DataFrame 转换为 Python 字典，通过 `orient` 参数控制转换方式。

| orient 值 | 说明 |
|-----------|------|
| `'dict'` | 默认，`{列名: {行索引: 值}}` |
| `'list'` | `{列名: [值列表]}`，最常用 |
| `'records'` | `[{列名: 值}, ...]`，每行一个字典 |

#### orient='list'（按列转）

```python
df6 = pd.DataFrame({
    "城市": ["北京", "上海", "广州"],
    "人口": [2189, 2487, 1868]
})
print(df6.to_dict(orient='list'))
```

**执行结果：**
```
{'城市': ['北京', '上海', '广州'], '人口': [2189, 2487, 1868]}
```

---

#### orient='records'（按行转）

```python
print(df6.to_dict(orient='records'))
```

**执行结果：**
```
[{'城市': '北京', '人口': 2189}, {'城市': '上海', '人口': 2487}, {'城市': '广州', '人口': 1868}]
```

---

> **暂更说明**
>
> 这场 Pandas 学习之旅，就陪你走到这里了。笔记暂歇，但探索不止——往后日子里，该练的练，该想的想。等哪天心里又攒了些新东西想说，再回来续写。不急不赶，来日方长。

import pandas as pd
import numpy as np

# 1. 加载原始数据
data = {
    "客户ID":[1001,1002,1003,1002,1004,1005,1001,1006,np.nan,1007],
    "客户姓名":["张三","李四","王五","李四","赵六","钱七","张三","孙八","周九","吴十"],
    "消费日期":["2026-05-01","2026-05-02","2026-05-01","2026-05-02","2026-05-03",
              "2026-05-01","2026-05-04","2026-05-03",np.nan,"2026-05-05"],
    "消费金额":[289,560,1200,560,890,3500,450,720,980,15000],
    "支付方式":["微信","支付宝","微信","支付宝","银行卡","微信","支付宝",np.nan,"微信","支付宝"]
}
df = pd.DataFrame(data)
print("原始数据形状：", df.shape)

# ======================
# 1. 数据清洗（缺失值+重复值+异常值）
# ======================
# 1.1 删除重复行（整行完全相同）
df = df.drop_duplicates()
print("删除重复后形状：", df.shape)

# 1.2 处理缺失值
# 关键列（客户ID、消费日期）缺失直接删除；支付方式用众数填充
df = df.dropna(subset=['客户ID', '消费日期'])
df['支付方式'] = df['支付方式'].fillna(df['支付方式'].mode()[0])
print("处理缺失后形状：", df.shape)

# 1.3 处理异常值（消费金额用IQR四分位数法）
Q1 = df['消费金额'].quantile(0.25)
Q3 = df['消费金额'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# 过滤掉异常值（这里15000明显超出范围，会被删除）
df = df[(df['消费金额'] >= lower_bound) & (df['消费金额'] <= upper_bound)]
print("处理异常后形状：", df.shape)

# ======================
# 2. 日期处理与特征工程
# ======================
# 转换为datetime类型
df['消费日期'] = pd.to_datetime(df['消费日期'])
# 添加月份列
df['月份'] = df['消费日期'].dt.month
# 添加星期列（时段）
df['星期'] = df['消费日期'].dt.day_name()
# 添加是否周末列（可选，更实用）
df['是否周末'] = df['消费日期'].dt.weekday >= 5

print("\n清洗后数据预览：")
print(df.head())

# ======================
# 3. 按支付方式分组统计
# ======================
payment_stats = df.groupby('支付方式').agg(
    消费次数=('消费金额', 'count'),
    总消费金额=('消费金额', 'sum'),
    平均消费金额=('消费金额', 'mean')
).round(2).reset_index()

print("\n3. 支付方式统计：")
print(payment_stats)

# ======================
# 4. 客户与每日消费统计
# ======================
# 4.1 消费金额前三的客户
customer_stats = df.groupby(['客户ID', '客户姓名'])['消费金额'].sum().reset_index()
top3_customers = customer_stats.sort_values('消费金额', ascending=False).head(3).reset_index(drop=True)

print("\n4.1 消费前三客户：")
print(top3_customers)

# 4.2 每日消费统计
daily_stats = df.groupby('消费日期')['消费金额'].agg(
    每日总消费='sum',
    每日消费次数='count'
).reset_index()

print("\n4.2 每日消费统计：")
print(daily_stats)

# ======================
# 5. 保存结果
# ======================
# 保存清洗后的数据
df.to_csv('清洗后消费数据.csv', index=False, encoding='utf-8-sig')
# 保存所有统计结果
payment_stats.to_csv('Test/支付方式统计.csv', index=False, encoding='utf-8-sig')
top3_customers.to_csv('Test/消费前三客户.csv', index=False, encoding='utf-8-sig')
daily_stats.to_csv('Test/每日消费统计.csv', index=False, encoding='utf-8-sig')

print("\n所有文件已保存成功！")
# MySQL 学习笔记 — 综合练习

> 基于 mall 商城数据库，涵盖单表查询、多表连接、子查询、事务四大阶段实战

---


## 环境准备（建库建表）

```sql
-- 1. 创建数据库
CREATE DATABASE IF NOT EXISTS mall
DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE mall;

-- 2. 用户表
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID，主键，自增',
    username VARCHAR(50) NOT NULL UNIQUE COMMENT '用户名，不可重复',
    reg_date DATE NOT NULL COMMENT '注册日期',
    vip_level TINYINT DEFAULT 0 COMMENT '会员等级：0-普通，1-银卡，2-金卡',
    balance DECIMAL(10,2) DEFAULT 0.00 COMMENT '账户余额（元）'
);

INSERT INTO users (username, reg_date, vip_level, balance) VALUES
('张三', '2025-01-10', 0, 5000.00),
('李四', '2025-03-15', 1, 3000.00),
('王五', '2024-12-01', 2, 8000.00),
('赵六', '2025-06-20', 0, 1500.00),
('孙七', '2025-02-28', 0, 10000.00),
('周八', '2025-04-10', 0, 3000.00),   -- 补充用户
('吴九', '2025-05-20', 1, 8000.00);   -- 补充用户

-- 3. 商品分类表
CREATE TABLE categories (
    cate_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '分类ID，主键，自增',
    cate_name VARCHAR(50) NOT NULL COMMENT '分类名称',
    parent_id INT DEFAULT NULL COMMENT '上级分类ID，为NULL表示顶级分类，自关联用'
);

INSERT INTO categories (cate_id, cate_name, parent_id) VALUES
(1, '手机数码', NULL),
(2, '家用电器', NULL),
(3, '图书音像', NULL),
(4, '智能手机', 1),    -- 子分类，父分类是"手机数码"
(5, '厨房电器', 2);   -- 子分类，父分类是"家用电器"

-- 4. 商品表
CREATE TABLE products (
    prod_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '商品ID，主键，自增',
    prod_name VARCHAR(100) NOT NULL COMMENT '商品名称',
    price DECIMAL(10,2) NOT NULL COMMENT '商品单价（元）',
    cate_id INT COMMENT '所属分类ID，关联categories表',
    FOREIGN KEY (cate_id) REFERENCES categories(cate_id)
);

INSERT INTO products (prod_name, price, cate_id) VALUES
('智能手机X', 3999.00, 4),
('蓝牙耳机', 299.00, 1),
('电饭煲', 459.00, 5),
('微波炉', 899.00, 2),
('Java核心技术', 108.00, 3),
('三体全集', 85.00, 3),
('智能手表', 1299.00, 1),
('高配智能手机Y', 4999.00, 4),       -- 补充商品
('普通蓝牙音箱', 199.00, 1),         -- 补充商品
('高端微波炉', 1299.00, 2),          -- 补充商品
('经济电饭煲', 199.00, 5),           -- 补充商品
('Python编程入门', 69.00, 3);        -- 补充商品

-- 5. 库存表
CREATE TABLE inventory (
    prod_id INT PRIMARY KEY COMMENT '商品ID，与products表一一对应',
    stock INT NOT NULL DEFAULT 0 COMMENT '当前库存数量',
    FOREIGN KEY (prod_id) REFERENCES products(prod_id)
);

INSERT INTO inventory (prod_id, stock) VALUES
(1, 100), (2, 200), (3, 5), (4, 50), (5, 10), (6, 3), (7, 30),
(8, 50),   -- 高配智能手机Y
(9, 30),   -- 普通蓝牙音箱
(10, 20),  -- 高端微波炉
(11, 15),  -- 经济电饭煲
(12, 40);  -- Python编程入门

-- 6. 订单表
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '订单ID，主键，自增',
    user_id INT NOT NULL COMMENT '下单用户ID，关联users表',
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '订单创建时间',
    total_amount DECIMAL(12,2) NOT NULL COMMENT '订单总金额（元）',
    status TINYINT DEFAULT 1 COMMENT '订单状态：1-待付款，2-已付款，3-已取消',
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO orders (order_id, user_id, order_date, total_amount, status) VALUES
(1, 1, '2025-07-01 10:30:00', 3999.00, 2),
(2, 1, '2025-07-02 14:00:00', 108.00, 2),
(3, 2, '2025-07-03 09:15:00', 1358.00, 2),
(4, 3, '2025-07-01 11:00:00', 299.00, 2),
(5, 4, '2025-07-04 16:40:00', 85.00, 2),    -- 改为已付款，让赵六有消费记录
(6, 5, '2025-07-05 08:20:00', 459.00, 2),
(7, 6, '2025-08-01 12:00:00', 1299.00, 2),  -- 周八
(8, 7, '2025-08-02 15:30:00', 4107.00, 2),  -- 吴九
(9, 5, '2025-08-03 10:00:00', 1758.00, 2),  -- 孙七第二单，多件商品
(10, 3, '2025-08-04 09:00:00', 1299.00, 2); -- 王五第二单

-- 7. 订单明细表
CREATE TABLE order_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT COMMENT '明细ID，主键，自增',
    order_id INT NOT NULL COMMENT '所属订单ID，关联orders表',
    prod_id INT NOT NULL COMMENT '商品ID，关联products表',
    quantity INT NOT NULL COMMENT '该商品购买数量',
    unit_price DECIMAL(10,2) NOT NULL COMMENT '购买时的商品单价（元）',
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (prod_id) REFERENCES products(prod_id)
);

INSERT INTO order_items (order_id, prod_id, quantity, unit_price) VALUES
-- 原始订单明细
(1, 1, 1, 3999.00),            -- 张三买智能手机X
(2, 5, 1, 108.00),             -- 张三买Java核心技术
(3, 3, 1, 459.00),             -- 李四买电饭煲
(3, 4, 1, 899.00),             -- 李四买微波炉（订单3有两个商品，件数>=2）
(4, 2, 1, 299.00),             -- 王五买蓝牙耳机
(5, 6, 1, 85.00),              -- 赵六买三体全集
(6, 3, 1, 459.00),             -- 孙七买电饭煲
-- 补充订单明细
(7, 7, 1, 1299.00),            -- 周八买智能手表
(8, 1, 1, 3999.00),            -- 吴九买智能手机X
(8, 5, 1, 108.00),             -- 吴九买Java核心技术
(9, 10, 1, 1299.00),           -- 孙七买高端微波炉
(9, 3, 1, 459.00),             -- 孙七买电饭煲（订单9有两个商品）
(10, 7, 1, 1299.00);           -- 王五买智能手表

-- 补充数据：新用户及订单
INSERT INTO users (username, reg_date, vip_level, balance) VALUES
('郑十', '2025-01-10', 0, 5000.00);

INSERT INTO orders (user_id, order_date, total_amount, status) VALUES
(4, '2025-08-05 10:00:00', 100.00, 1);   -- 赵六一个待付款订单

-- 李四再次购买智能手机X（第二个订单）
INSERT INTO orders (user_id, order_date, total_amount, status)
VALUES (2, '2025-08-10 11:00:00', 3999.00, 2);

INSERT INTO order_items (order_id, prod_id, quantity, unit_price)
VALUES (
    (SELECT order_id FROM orders WHERE user_id = 2 AND total_amount = 3999.00 ORDER BY order_id DESC LIMIT 1),
    1,   -- 智能手机X
    1,
    3999.00
);

-- 给李四新增一笔已付款订单，再次购买智能手机X
INSERT INTO orders (user_id, order_date, total_amount, status)
VALUES (2, '2025-08-15 14:00:00', 3999.00, 2);

-- 对应订单明细：同款商品 prod_id=1
INSERT INTO order_items (order_id, prod_id, quantity, unit_price)
VALUES (LAST_INSERT_ID(), 1, 1, 3999.00);
```

---

## 阶段一：单表查询强化

### 1. 指定列与别名

查询所有用户，只显示用户名和注册日期，列别名分别为"姓名"、"注册时间"。

> **提示：** `select 列名 as 别名`

```sql
select username as '姓名', reg_date as '注册时间' from users;
```

---

### 2. 条件 >

找出所有账户余额大于 3000 的用户。

> **提示：** `where balance > 3000`

```sql
select * from users where balance > 3000;
```

---

### 3. or 与 in

查询属于"手机数码"或"图书音像"分类的所有商品（用 or 和 in 各写一版）。

> **提示：** `where category = '手机数码' or category = '图书音像'`；`where category in ('手机数码','图书音像')`

```sql
-- 用子查询实现
select * from products where cate_id
in (select cate_id from categories where cate_name in ('手机数码', '图书音像'));

-- p.* 就是只有 p 这个表的字段
select p.* from products p
inner join categories c
on p.cate_id = c.cate_id
where cate_name = '手机数码' or cate_name = '图书音像';
```

---

### 4. 模糊查询 like

找出商品名称中包含"电"字的商品。

> **提示：** `where name like '%电%'`

```sql
select * from products where prod_name like '%电%';
```

---

### 5. between and + 排序

查询单价在 100 到 1000 元之间的所有商品，按价格降序排列。

> **提示：** `where price between 100 and 1000 order by price desc`

```sql
select * from products where price between 100 and 1000 order by price desc;
```

---

### 6. 分组统计 + having

按会员等级统计人数，只显示人数、等级。

```sql
select
    case vip_level
      when 0 then '普通'
      when 1 then '银卡'
      when 2 then '金卡'
    end as '会员等级',
    count(*)
from users
group by vip_level;
```

---

### 7. 分页 limit

查询商品表，每页显示 3 条记录，写出获取第 2 页数据的 SQL。

> **提示：** `limit 3 offset 3` 或 `limit 3,3`

```sql
select * from products limit 2, 3;
```

---

### 8. 字符串函数

将每个用户的用户名转为大写，并拼接上 `_VIP` 后缀作为新列显示。

> **提示：** `concat(upper(username), '_VIP')`

```sql
select concat(upper(username), '_VIP') from users;
```

---

### 9. 日期函数 + 条件

计算每个订单的下单日期距离今天过了多少天，并只显示最近 7 天内的订单。

> **提示：** `datediff(curdate(), order_date)`，并用 where 过滤差值 <= 7

```sql
select *, datediff('2025-07-09', order_date) as order_count from orders having order_count <= 7;
```

---

### 10. 流程函数

查询用户表，根据余额显示评价：余额 > 5000 显示"高净值"，否则显示"普通"（用 if 或 case when 实现）。

> **提示：** `if(balance>5000,'高净值','普通')`；或 `case when balance>5000 then '高净值' else '普通' end`

```sql
select *, (
    case
        when balance > 5000 then '高净值'
        else '低净值'
    end
) as `余额状态` from users;
```

---

## 阶段二：多表连接

### 1. 内连接

查询所有订单的订单编号、下单时间、下单用户姓名（显式 join 写法）。

> **提示：** `orders inner join users on orders.user_id = users.id`

```sql
select o.order_id, u.username, o.order_date from users u
inner join orders o
on u.user_id = o.user_id;
```

---

### 2. 左连接 + 分组

查询所有用户及其历史总消费金额（没有下过单的用户总消费显示 0）。

> **提示：** left join 后按用户分组，对金额 sum，用 `coalesce(sum(amount),0)` 处理 null

```sql
select u.username, coalesce(sum(total_amount), 0) from users u
left join orders o on u.user_id = o.user_id
group by u.username;
```

---

### 3. 自连接

查询每个商品分类的名字，同时显示出它的上级分类名称（categories 表通过 parent_id 自关联）。

> **提示：** `from categories c left join categories p on c.parent_id = p.id`

```sql
select c.cate_name, p.prod_name from categories c
left join products p
on p.cate_id = c.cate_id;
```

---

### 4. 联合查询

将"手机数码"分类下的商品和"图书音像"分类下的商品，合并成一张列表（商品名、价格），用 union all 实现。

> **提示：** 两个 select 语句用 union all 连接，列数和类型需一致

```sql
-- 方式一：用子查询
select prod_name, price from products where cate_id in
(select cate_id from categories where cate_name in ('手机数码', '图书音像'));

-- 方式二：用 union all
select prod_name, price from products where cate_id = 1
union all
select prod_name, price from products where cate_id = 3;
```

---

### 5. 连接库存表

查询每个商品的名称、价格以及对应的库存数量。

> **提示：** `products join inventory on products.id = inventory.product_id`，选择合适的连接类型

```sql
select p.prod_name, v.stock, price from products p
inner join inventory v
on p.prod_id = v.prod_id;
```

---

## 阶段三：子查询专项突破

### 3-1 标量子查询

#### 1. 高于平均价格的商品

查询价格高于所有商品平均价格的商品名称和价格。

> **提示：** `where price > (select avg(price) from products)`

```sql
select * from products where price > (select avg(price) from products);
```

---

#### 2. 余额最多的用户

找出账户余额最多的用户姓名和余额（必须用标量子查询，不能直接排序取第一条）。

> **提示：** `where balance = (select max(balance) from users)`

```sql
select * from users where balance = (select max(balance) from users);
```

---

### 3-2 列子查询（in / not in / any / all）

#### 3. 下过订单的用户

查询下过订单的所有用户姓名。

> **提示：** `where id in (select distinct user_id from orders)`

```sql
-- distinct 去重
select username from users where user_id in (select distinct user_id from orders);
```

---

#### 4. 从未下过订单的用户

查询从未下过订单的用户，分别用 not in 和 not exists 写出两个版本。

> **提示：** not in 版本需注意子查询不要返回 null；not exists 使用关联子查询

```sql
-- 假设内部的查询有一个还是多个 null 查到的结果就会是空的
select username from users where user_id not in (select distinct user_id from orders);

-- 开发中一般就是用 not exists
select username from users where not exists(
    select 1 from orders where orders.user_id = users.user_id
);
```

---

#### 5. 进阶验证：not in vs not exists 的 null 陷阱

执行 `update orders set user_id = null where order_id = 5;` 后，重新运行第4题的两个版本，解释结果为何不同。

> **提示：** 当子查询结果含 null 时，not in 会返回空集；not exists 不受影响

```sql
-- 模拟
alter table orders modify user_id int null;

insert into users (username, reg_date, vip_level, balance) values
('周八', '2025-08-01', 0, 2000.00);

update orders set user_id = null where order_id = 5;

-- 复原
delete from users where user_id = 6;

update orders set user_id = 4 where order_id = 5;

alter table orders modify user_id int not null;
```

---

#### 6. 比"家用电器"所有商品都贵的商品

> **提示：** `where price > all (select price from products where category='家用电器')`

```sql
select * from products
where price > all(
    select price from products p left join categories c on c.cate_id = p.cate_id
    where cate_name = '家用电器'
    or c.parent_id = (select cate_id from categories where cate_name = '家用电器')
);
```

---

#### 7. 比"手机数码"任意一个商品便宜的商品

> **提示：** `where price < any (select price from products where category='手机数码')`

```sql
select * from products
where price < any(
    select price from products p left join categories c on c.cate_id = p.cate_id
    where cate_name = '手机数码'
    or c.parent_id = (select cate_id from categories where cate_name = '手机数码')
);
```

---

### 3-3 行子查询

#### 8. 查询与"张三"同天注册且余额相同的其他用户

> **提示：** `where (reg_date, balance) = (select reg_date, balance from users where name='张三') and name <> '张三'`

```sql
select username, balance from users where (reg_date, balance) = (
    select reg_date, balance from users where username = '张三')
and username <> '张三';
```

---

### 3-4 表子查询（派生表）

#### 9. 消费高于平均的用户

先构建"每个用户的总消费金额"派生表，再查询消费总额高于所有用户平均消费总额的用户。

> **提示：** 子查询先 group by user_id 求总消费，外层 `where total > (select avg(total) from 派生表)`

```sql
-- 派生表方式
select u.username, balance, t.uta from users u
inner join
(select user_id, sum(total_amount) as uta
from orders
where status = 2
group by user_id) t
on u.user_id = t.user_id
where t.uta > (
    select avg(uta) from (
        select user_id, sum(total_amount) as uta
        from orders
        where status = 2
        group by user_id
    ) avg_t
);

-- CTE 风格（推荐）
with user_total as(
    select user_id, sum(total_amount) as uta
    from orders
    where status = 2
    group by user_id
)

select u.username, u.balance, ut.uta
from users u
inner join user_total ut
on u.user_id = ut.user_id
where ut.uta > (
    select avg(uta) from user_total
);
```

---

#### 10. 多件商品订单

在订单明细表中，将订单商品件数 >= 2 的订单做成派生表，关联订单主表，显示订单编号和总金额。

> **提示：** `from orders join (select order_id from order_items group by order_id having sum(quantity) >= 2) as t on orders.id = t.order_id`

```sql
-- CTE 风格
with order_quantity as(
    select order_id from order_items
    group by order_id
    having sum(quantity) >= 2
)

select o.order_id, o.total_amount from orders o
inner join order_quantity oq
on o.order_id = oq.order_id;

-- 派生表风格
select o.order_id, o.total_amount from orders o
inner join(
    select order_id from order_items group by order_id
    having sum(quantity) >= 2
) t
on o.order_id = t.order_id;
```

---

### 3-5 关联子查询（核心能力）

#### 11. 高于分类均价的商品

查询每个商品分类中，价格高于该分类平均价格的商品（商品名、价格、分类名），必须用相关子查询。

> **提示：** `where price > (select avg(price) from products p2 where p2.category_id = p1.category_id)`

```sql
select c.cate_name, p.prod_name, p.price from categories c
inner join products p
on c.cate_id = p.cate_id
where p.price > (
    select avg(p1.price) from products p1
    where p.cate_id = p1.cate_id
);
```

---

#### 12. 用 exists 查询购买过高单价商品的用户

查询那些至少购买过一次单价超过 1000 元商品的用户。

> **提示：** `where exists (select 1 from orders join order_items on ... where orders.user_id = users.id and price > 1000)`

```sql
select username from users
where exists(
    select 1 from orders o
    inner join order_items oi
    on o.order_id = oi.order_id
    where unit_price > 1000
);
```

---

#### 13. 与"张三"购买过同款商品的其他用户

查询与"张三"购买过同款商品的其他用户（需显示用户id、用户名及相同商品名，排除张三自己）。

> **提示：** 用 exists 或 in 在订单明细中匹配张三购买过的 product_id，且用户不是张三

```sql
with opi as(
    select u.user_id, u.username, p.prod_name, p.prod_id
    from users u
    inner join orders o on u.user_id = o.user_id
    inner join order_items oi on o.order_id = oi.order_id
    inner join products p on p.prod_id = oi.prod_id)

select distinct * from opi where prod_id in (select prod_id from opi where username = '张三')
and username <> '张三';
```

---

## 阶段四：事务

### 1. 转账事务原子性

从"张三"账户转 500 元到"李四"账户。在事务中故意插入一句错误 SQL，验证回滚后双方余额是否恢复原值。

> **提示：** `start transaction; update ...; 错误语句; rollback;` 检查值未变

```sql
start transaction;

update users set balance = balance - 500 where username = '张三';
update users set balance = balance + 500 where username = '李四';

select * from users;

-- rollback;

commit;
```

---

### 2. 下单扣库存事务

模拟用户"王五"购买 2 个"电饭煲"：查询库存 → 判断充足 → 扣减库存 → 创建订单 → 插入明细。任一步失败则全部回滚。

> **提示：** 整个流程包裹在事务中，任一失败触发 rollback，成功则 commit

- 王五 user_id = 3
- 电饭煲 prod_id = 3

```sql
start transaction;

-- 查询库存
select stock from inventory where prod_id = 3;

-- 扣减库存
update inventory set stock = stock - 2 where prod_id = 3;

-- 创建订单
insert into orders values(null, 3, now(), 918, 2);

-- last_insert_id() 获取最近一次 insert 语句生成的自增主键值
insert into order_items values(null, last_insert_id(), 3, 2, 459);

-- 扣减余额
update users set balance = balance - 918 where username = '王五';

-- rollback;

commit;
```

---

> **知识点部分** → 请打开 [`MySQL学习笔记-知识点.md`](MySQL学习笔记-知识点.md)
>
> **返回总目录** → 请打开 [`MySQL学习笔记.md`](MySQL学习笔记.md)

---

> **暂更说明**
>
> 中途停笔，暂告一段落。此版为基础篇，供学习与复习。过几天更新。保持期待

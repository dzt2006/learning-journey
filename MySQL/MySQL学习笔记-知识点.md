# MySQL 学习笔记 — 知识点

> 涵盖数据库操作、表操作、DML、DQL、DCL、函数、约束、多表查询、子查询、事务等核心知识点

---


## 一、数据库操作

### 查看所有数据库

```sql
show databases;
```

### 创建

```sql
create database if not exists shangguan
default charset utf8mb4                  -- 字符集
collate utf8mb4_unicode_ci;              -- 排序规则
```

### 使用

```sql
use shangguan;
```

### 查询当前数据库

```sql
select database();
```

### 删除

```sql
drop database if exists wangzhe;
```

---

## 二、表操作

### 创建表

```sql
-- 创建test表
create table test (
    id int primary key auto_increment comment '主键自增id',
    name varchar(50) not null comment '姓名',
    age tinyint comment '年龄',
    email varchar(100) unique comment '邮箱',
    create_time datetime default current_timestamp comment '创建时间'
);
```

### 修改表

#### 添加字段

```sql
alter table user
add sex tinyint not null default 0
comment '1男 2女 0未知(默认)';
```

#### 修改数据类型

```sql
alter table user modify username varchar(250);
```

#### 修改字段名与类型

```sql
alter table user change username names varchar(50) default 'lihua' comment '把username改为names长度为50';
```

#### 删除字段

```sql
alter table user drop sex;
```

#### 修改表名

```sql
alter table user rename to users;
```

### 删除表

#### 删除表

```sql
drop table if exists test;
```

#### 清空表（保留结构）

```sql
-- 删除指定表，并重新创建该表(先删除整张表，再按原表结构重新创建一张空表)
truncate table test;
```

### 查看表信息

```sql
-- 查询当前数据库所有表
show tables;

-- 查询表结构
desc user;

-- 查询指定表的建表语句
show create table user;
```

---

## 三、数据操作（DML）

### 插入数据

```sql
-- 给指定字段添加数据
insert into test (name, age) values ('小明', 20);

-- 给全部字段添加数据
insert into test values (null, '小红', 22, 'xiaohong@qq.com', now());

-- 批量插入多条数据
INSERT INTO test (name, age, email)
VALUES
('张三', 22, 'zhangsan@163.com'),
('李四', 25, 'lisi@qq.com'),
('王五', 19, 'wangwu@gmail.com'),
('赵六', 28, 'zhaoliu@outlook.com');
```

### 修改数据

```sql
-- 修改数据
update test set name = '小蓝', age = 18 where name = '小红';
```

### 删除数据

```sql
-- 删除表内指定数据
delete from test where name = '小蓝';
```

---

## 四、数据查询（DQL）

### 基础查询

```sql
-- 查询所有字段数据
select * from test;

-- 查询指定字段
select name, age, email from test;

-- 查询指定字段(加别名)
select name as '名字', age as '年龄' from test;

-- 去除重复记录
select distinct age from test;
```

### 条件查询

#### 比较运算符

```sql
-- 不等于
select * from test where age != 22;
select * from test where age <> 22;
```

#### 范围查询

```sql
-- 符合里面条件的
select * from test where age in(20,22,25);

-- 不符合里面条件的
select * from test where age not in(20,22,25);

-- 开区间
select * from test where age between 18 and 25;
```

#### 模糊查询

`_` 匹配单个字符，`%` 匹配任意字符。

```sql
-- 模糊查询(_单个字符、% 任意字符)
select * from test where name like '%小%';
select * from test where name like '张_';
```

#### 逻辑运算

```sql
-- 逻辑
select * from test where age = 20 or name = '李四';
select * from test where age = 25 and name = '李四';

-- 取反
select * from test where not name = '张三';
```

#### 判空

```sql
-- 判空
select * from test where email is null;
select * from test where email is not null;
```

### 聚合函数

```sql
-- 聚合函数
select count(*), max(age), min(age), sum(age), round(avg(age),2) from test;
```

### 分组查询

```sql
-- 分组查询
select age, count(*) as 人数 from test where age >= 18
group by age having count(*) > 1;
```

> **执行顺序：** 先拿表 → 筛原始行 → 分组 → 筛分组结果 → 选字段起别名 → 排序 → 分页截取

### 排序查询

先按左边字段排，左边值一样，才用右边字段微调顺序。

```sql
-- 排序查询(先按左边字段排，左边值一样，才用右边字段微调顺序)
select name, age, id from test order by age desc, id asc;    -- 升序、降序
```

### 分页查询

```sql
-- 分页查询
select * from test limit 3;

select name, age from test limit 1, 2;    -- 前面是页数，后面是条数
```

---

## 五、DCL 数据控制语言

### 用户管理

```sql
-- 查询用户
use mysql;
select * from user;

-- 创建用户
create user 'dzt'@'localhost' identified by '123456';

-- 修改用户密码
alter user 'dzt'@'localhost' identified with mysql_native_password by '147258';

-- 删除用户
drop user 'dzt'@'localhost';
```

### 权限管理

```sql
-- 查询权限
show grants for 'dzt'@'localhost';

-- 授予权限
grant all privileges on *.* to 'dzt'@'localhost';

-- 撤销权限
revoke all privileges on *.* from 'dzt'@'localhost';
```

---

## 六、常用函数

### 字符串函数

```sql
-- concat 拼接
select concat('dzt','-','123456');

-- lower转小写
select lower('DZT');

-- upper转大写
select upper('dzt');

-- 左填充
select lpad('666',5,'*');

-- 右填充
select rpad('666',5,'*');

-- trim 去除首尾空格
select trim('        test      ');

-- substring 字符串截取
select substring('abcdefg',2,4);
```

### 数值函数

```sql
-- ceil 向上取整
select ceil(2.1), ceil(2.9), ceil(-3.5);

-- floor 向下取整
select floor(2.1), floor(2.9), floor(-3.5);

-- mod 取模
select mod(5,3), mod(10,3), mod(9,3);

-- round 四舍五入
select round(1.45), round(3.5), round(4.5);
```

#### 生成随机数

```sql
-- 生成 [min,max)
select floor(rand() * 100) + 1;
```

### 日期函数

```sql
-- 获取当前时间
select curdate();             -- 2026-06-22
select curtime();             -- 11:43:17
select now();                 -- 2026-06-22 11:43:17

-- 提取年月日
select year('2026-06-22'), month('2026-06-22'), day('2026-06-22');

-- 日期加法
select date_add(curdate(), interval 1 hour);
select date_add(curdate(), interval 2 day);
select date_add(curdate(), interval 3 month);

-- 日期减法
select date_sub(curdate(), interval 1 hour);
select date_sub(curdate(), interval 2 day);
select date_sub(curdate(), interval 3 month);

-- 天数差
select datediff('2026-06-30','2026-06-22');
```

### 流程函数

先建立演示用的表：

```sql
-- 建立表展示
create table Department(
    dept_id int primary key comment '部门主键',
    dept_name varchar(50) comment '部门名称'
) comment '演示外键关联的测试表';

create table Employee(
    id int auto_increment primary key,
    `name` varchar(50) not null unique,
    salary decimal(10,2) default 0.00,
    bonus decimal(10,2),
    score int default 1,
    dept_id int,
    check(score >= 0 and score <= 100),
    foreign key(dept_id) references Department(dept_id)
) comment '员工信息测试表';

insert into Employee (name, salary, bonus, score) values
('张大鹏', 8000.00, 1000.00, 95),
('李小华', 4500.00, null, 72),
('王小明', 6000.00, null, 55);
```

#### if — 条件判断

```sql
-- if 条件判断
select `name`, salary, if(salary > 5000, '高薪', '普通') as 薪资等级 from Employee;
```

#### ifnull — 空值处理

```sql
-- ifnull 空值处理
select `name`, bonus, ifnull(bonus, 0) as 实际奖金 from Employee;
```

#### case when — 多条件范围判断

```sql
-- case when 多条件范围判断
select `name`, score,
    case
        when score >= 90 then '优秀'
        when score >= 70 then '良好'
        else '不及格'
    end as 成绩评级
from Employee;
```

---

## 七、约束

先创建测试表：

```sql
-- 测试表
create table classes (
    class_id int comment '班级编号',
    class_name varchar(50) comment '班级名称'
);

create table students (
    student_id int comment '学号',
    `name` varchar(50) comment '姓名',
    age int comment '年龄',
    class_id int comment '所属班级编号'
);
```

### 主键约束

```sql
-- primary key 添加主键约束
alter table classes add primary key (class_id);
alter table students add primary key (student_id);
```

### 外键约束

```sql
-- foreign key 添加外键约束(子表放前)
alter table students add constraint fk1 foreign key
(class_id) references classes (class_id);

-- 删除外键 fk1
alter table students drop foreign key fk1;
```

### 检查约束

```sql
-- 给表加字段
alter table students add column score int;

-- check 添加检查约束
alter table students add constraint ck1 check(score >=0 and score <= 150);
```

### 外键行为

> **restrict：** 立即检查，发现子表有数据立刻报错。
> **no action：** 延迟到事务提交时检查（一般不用）。

#### no action（无动作）

只要子表有关联数据，禁止删除/修改父表。

```sql
-- 行为：no action (无动作)
-- 只要子表有关联数据，禁止删除/修改父表
alter table students add constraint fk1 foreign key
(class_id) references classes (class_id)
on delete no action on update no action;
```

#### restrict（保护限制）

只要子表里还有关联数据，禁止删除/修改父表记录。

```sql
-- 行为：restrict (保护限制)
-- 只要子表里还有关联数据，禁止删除/修改父表记录
alter table students add constraint fk1 foreign key
(class_id) references classes (class_id)
on delete restrict on update restrict;
```

#### cascade（级联删除/更新）

当父表数据被删除或修改时，子表中的关联数据也会跟着被删掉或跟着修改。

```sql
-- 行为：cascade (级联删除/更新)
-- 当父表数据被删除或修改时，子表中的关联数据也会跟着被删掉或跟着修改
alter table students add constraint fk1 foreign key
(class_id) references classes (class_id)
on delete cascade on update cascade;
```

#### set null（置空）

当父表数据被删除时，子表关联数据的外键字段会变成 null。注意：前提条件是子表的外键字段必须允许为 null。

```sql
-- 行为：set null (置空)
-- 当父表数据被删除时，子表关联数据的外键字段会变成 null
-- 注意：前提条件是子表的外键字段必须允许为 null
alter table students add constraint fk1 foreign key
(class_id) references classes (class_id)
on delete set null on update set null;
```

---

## 八、多表查询

先创建演示用的部门表和员工表：

```sql
-- 创建部门表 (父表)
create table dept (
    id int auto_increment primary key comment '部门id',
    name varchar(50) comment '部门名称'
) comment '部门信息表';

-- 创建员工表 (子表)
create table emp (
    id int auto_increment primary key comment '员工id',
    `name` varchar(50) comment '姓名',
    age int comment '年龄',
    salary decimal(10,2) comment '薪资',
    dept_id int comment '所属部门id',
    manager_id int comment '直属上级id'
) comment '员工信息表';

alter table emp add foreign key (dept_id) references dept(id);
alter table emp add foreign key (manager_id) references emp(id);

insert into dept (id, `name`) values
(1, '研发部'),
(2, '市场部'),
(3, '销售部'),
(4, '财务部'),
(5, '后勤部');

insert into emp (id, `name`, age, salary, dept_id, manager_id) values
(1, '张大鹏', 25, 10000.00, 1, null),   -- 研发部老大
(2, '李小华', 28, 8000.00, 1, 1),       -- 张大鹏的下属
(3, '王小明', 22, 6000.00, 1, 1),       -- 张大鹏的下属
(4, '赵经理', 30, 12000.00, 2, null),   -- 市场部老大
(5, '孙七', 26, 9000.00, 2, 4),         -- 赵经理的下属
(6, '周八', 23, 5000.00, 3, null),      -- 销售部老大
(7, '吴九', 27, 7500.00, 3, 6),         -- 周八的下属
(8, '郑十', 35, 15000.00, null, null);
-- 最高薪，但没有归属部门
```

### 内连接

两张表满足连接条件的交集部分。**一旦给表取了别名那么数据库里面就只认你取的别名了。**

#### 隐式内连接

```sql
-- 隐式内连接
select emp.id, emp.`name`, emp.salary, dept.`name` as '部门名称'
from emp, dept
where emp.dept_id = dept.id;
```

#### 显式内连接

```sql
-- 显式内连接
select emp.id, emp.`name`, emp.salary, dept.`name` as '部门名称'
from emp
inner join dept
on emp.dept_id = dept.id;
```

### 外连接

保留相应表全部数据，匹配不到补 null。

#### 左外连接

```sql
-- 左外连接
select emp.id, emp.`name`, emp.salary, dept.`name` as '部门名称'
from emp
left join dept
on emp.dept_id = dept.id;
```

#### 右外连接

```sql
-- 右外连接
select emp.id, emp.`name`, emp.salary, dept.`name` as '部门名称'
from emp
right join dept
on emp.dept_id = dept.id;
```

### 自连接

同一张表自己和自己关联查询。

#### 内连接自连接

如果前后没有匹配的直接过滤了。

```sql
-- 内连接自连接(如果前后没有匹配的直接过滤了)
select e1.`name` as '员工姓名', e2.`name` as '上级姓名'
from emp e1
inner join emp e2
on e1.id = e2.manager_id;
```

#### 左外连接自连接（一般使用这个）

```sql
-- 左外连接自连接(一般使用这个)
select e1.`name` as '员工姓名', e2.`name` as '上级姓名'
from emp e1
left join emp e2
on e1.id = e2.manager_id;
```

---

## 九、联合查询

### union all

直接拼接，保留所有行，常用。

```sql
-- union all(直接拼接，保留所有行，常用)
select id, name, salary from emp where salary > 8000
union all
select id, name, salary from emp where age < 30
order by id;
```

### union

自动去重，完全相同的行保留一条。

```sql
-- union(自动去重，完全相同的行保留一条)
select id, name, salary from emp where salary > 8000
union
select id, name, salary from emp where age < 30
order by id;
```

---

## 十、子查询

子查询是嵌套在另一条 SQL 语句内部的 select 查询。

### 标量子查询

只能返回一行一列，不然会报错。右边的才是内部子查询。

```sql
-- 标量子查询(只能返回一行一列，不然会报错)
select * from emp where salary > (select avg(salary) from emp);
```

### 列子查询

拿外层的 1 个字段，去跟一列值（集合）做比较。

#### in / not in

```sql
-- in / not in
select * from emp
where dept_id
in (select id from dept where name in('研发部', '市场部'));
```

#### any（或 some）

```sql
-- any 或者 some
select * from emp
where salary > any(select salary from emp where dept_id = 3);
```

#### all（集合中的全部）

```sql
-- all (集合中的全部)
select * from emp
where salary > all(select salary from emp where dept_id = 3);
```

### 行子查询

拿外层的多个字段组合，去跟一条记录的多个值做匹配。

```sql
-- 行子查询(拿外层的 多个字段组合，去跟一条记录的多个值做匹配)
select * from emp
where (age, salary) = (select age, salary from emp where `name` = '张大鹏');
```

### 表子查询（派生表）

#### 放在 from 后面

一定要起别名。

```sql
-- 放在 from 后面(一定要起别名)
select * from (select * from emp where age < 30) as t
order by t.salary desc;
```

#### 放在 where 后面

外内层字段要相等，顺序要一致。

```sql
-- 放在 where 后面(外内层字段要相等 顺序要一致)
select * from emp where (dept_id, age)
in(select dept_id, age from emp where dept_id = 3);
```

---

## 十一、事务

### 基本操作

```sql
-- 开始事务
start transaction;

-- 模拟错误的修改
update emp set salary = 128888 where `name` = '张大鹏';

-- 回滚(撤销)
rollback;
```

```sql
start transaction;

-- 模拟正确的修改
update emp set salary = 120000 where `name` = '张大鹏';

select salary from emp where `name` = '张大鹏';

-- 提交
commit;
```

### 事务隔离级别

| 现象 | 说明 |
|------|------|
| 脏读 | 一个事务读到了另一个事务尚未提交的数据 |
| 不可重复读 | 同一事务内，两次查同一条记录，因另一事务在间隙提交了修改，两次结果内容不一致 |
| 幻读 | 同一事务内，两次查同一条件数据集，因另一事务在间隙提交了插入或删除，导致第二次查询行数凭空增减 |

```sql
-- read uncommitted 读未提交（脏读、不可重复读、幻读全都有）
set session transaction isolation level read uncommitted;

-- read committed 读已提交（防脏读，但还有不可重复读和幻读）
set session transaction isolation level read committed;

-- repeatable read 可重复读（防脏读+不可重复读，MySQL默认）
set session transaction isolation level repeatable read;

-- serializable 串行化（全部防住，但最慢，像排队）
set session transaction isolation level serializable;

-- 查询当前状态
select @@transaction_isolation;
```

---

> **练习部分** → 请打开 [`MySQL学习笔记-综合练习.md`](MySQL学习笔记-综合练习.md)

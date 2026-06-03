import pymysql

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'port': 3306,
    'charset': 'utf8mb4'
}

conn = None
cursor = None

try:
    # 这里就是打开 SSMS 然后登录账号连接服务器
    conn = pymysql.connect(**db_config)

    # 这里就是点击 新建查询 编写脚本的那个窗口
    cursor = conn.cursor()
    print("连接成功")

    # 创建数据库
    cursor.execute("create database my_student;")
    print("创建好数据库名：my_student")

    # 切换数据库，就是相当于用了         use 数据库名
    conn.select_db("my_student")

    sql = """
    create table Student(
        -- auto_increment 相当于 sql server 里面的自增  identity(1,1) 
        id int primary key auto_increment,       
        -- `name` (这里是反引号) 相当于   sql server 里面的 [name] (用来处理关键字)
        `name` varchar(20),
        age int  
    );   
    """

    cursor.execute(sql)
    print("创建好Student表")

    sql = """
    insert into student(name, age) values('dzt', 20), ('lhs','24'), ('ikh','22');
    """

    cursor.execute(sql)
    # 这个就相当于保存      增删改都要必须要保存
    conn.commit()
    print("数据插入成功")

    cursor.execute("select * from Student;")

    # 这里相当于把你刚刚查询的表的    第一条数据    直接储存到这个 res里面
    res = cursor.fetchone()
    # 这里相当于把你刚刚查询的表直接打包到这个 reses里面 注意：如果上面拿走了 第一条数据，那么他只能拿下面剩下的了
    # 本质上是拿指针剩下的数据
    reses = cursor.fetchall()
    print(f"这个是第一条数据: {res}")
    print(f"这个是第剩下数据: {reses}")

except Exception as e:
    print("有问题", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("数据库已经关闭了")
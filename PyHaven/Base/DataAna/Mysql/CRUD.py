import pymysql

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'port': 3306,
    'charset': 'utf8mb4'
}


def get_connection():
    try:
        conn = pymysql.connect(**db_config)
        print("连接成功")
        return conn
    except Exception as e:
        print("连接失败",e)
        return None


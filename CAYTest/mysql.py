import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "xyzzg", "mmall", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = "INSERT INTO mmall_cart(id, \
       user_id, product_id) \
       VALUES ('%d', '%d', '%d')" % \
       (2, 3, 20)
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()

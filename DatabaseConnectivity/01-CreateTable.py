import pymysql

connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             db = 'pythondb_connect',
                             autocommit = True)

cursor = connection.cursor()

query = 'CREATE TABLE user (name varchar(100),emailId varchar(100),password varchar(50),company varchar(80), age int(100))'

cursor.execute(query)
print("Table Created Successfully...")
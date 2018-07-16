import pymysql

connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             db = 'pythondb_connect',
                             autocommit = True)

cursor = connection.cursor()

username = 'Ramesh'
useremail = 'ramesh1242@gmail.com'
userpwd = '12344545'
usercompany = 'HCL'
userage = 30

# query = "INSERT INTO user VALUES ('Ram','ram@gmail.com','ram124','TCS',28)"

query = "INSERT INTO user VALUES (%s,%s,%s,%s,%s)"

cursor.execute(query, (username,useremail,userpwd,usercompany,userage))
print("Data inserted successfully...")
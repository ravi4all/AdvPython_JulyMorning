import pymysql

connection = pymysql.connect(host='localhost',
                             port = 3306,
                             user='root',
                             db = 'pythondb_connect',
                             autocommit = True)

cursor = connection.cursor()

def checkEmailId(emailId):
    query = "SELECT * FROM user"
    cursor.execute(query)

    for data in cursor:
        if emailId in data:
            raise ValueError("User Already Exist")

def inserData():
    username = 'Ramesh Sharma'
    useremail = 'ramesh1242@gmail.com'
    userpwd = '12344545'
    usercompany = 'TCS'
    userage = 30

    checkEmailId(useremail)

    query = "INSERT INTO user VALUES (%s,%s,%s,%s,%s)"

    cursor.execute(query, (username, useremail, userpwd, usercompany, userage))
    print("Data inserted successfully...")

try:
    inserData()
except ValueError as err:
    print(err)
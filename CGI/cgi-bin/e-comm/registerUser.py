#! C:/Python36/python.exe

import cgi
import pymysql

connection = pymysql.connect(host="localhost", user = 'root', db = 'onlineShop',
                port = 3306, autocommit = True)

cursor = connection.cursor()

form = cgi.FieldStorage()

username = form.getvalue('uname')
useremail = form.getvalue('uemail')
userpwd = form.getvalue('upwd')
userphnno = form.getvalue('uphn')

query = "INSERT INTO users VALUES (%s, %s, %s, %s)"
cursor.execute(query, (username, useremail, userpwd, userphnno))

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Registered Successfully</h1>
<a href="../../e-commerce/index.html">Back to Home</a>
</body>
</html>
""")
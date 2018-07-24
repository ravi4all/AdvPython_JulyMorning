#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

username = form.getvalue('u_name')
userpwd = form.getvalue('u_pwd')

print("Content-type:text/html\r\n\r\n")
# print("<html>")
# print("<head>")
# print("<title>Login</title>")
# print("</head>")
# print("<body>")
# print("<h1>Hello {}".format(username))
# print("</body>")
# print("</html>")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Hello {}</h1>
</body>
</html>
""".format(username))
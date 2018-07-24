#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

username = form.getvalue('u_name')
userpwd = form.getvalue('u_pwd')

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
""")

if username == "Ram" and userpwd == "ram1234":
    print("<h1>Hello {}</h1>".format(username))
else:
    print("<h1>Login Failed...</h1>")

print("""
</body>
</html>
""")
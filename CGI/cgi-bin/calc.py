#! C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

# firstnumber = int(form.getvalue('fnum'))
# secondnumber = int(form.getvalue('snum'))
firstnumber = form.getvalue('fnum')
secondnumber = form.getvalue('snum')
operation = form.getvalue('opr')

# if operation == "add":
#     result = firstnumber + secondnumber
expression = firstnumber + operation + secondnumber
result = eval(expression)

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Result is {}</h1>
</body>
</html>
""".format(result))
#!C:/Python36/python.exe

import cgi

form = cgi.FieldStorage()

username = form.getvalue('u_name')
userpwd = form.getvalue('u_pwd')

def showData(message):
    print("Content-type:text/html\r\n\r\n")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <h1>{}</h1>
    </body>
    </html>
    """.format(message))

# if username == "Ram" and userpwd == "ram1234":
#     message = "Hello "+username
# else:
#     message = "Login Failed"

if username == "Ram" and userpwd == "ram1234":
    message = "Hello "+username
    showData(message)
else:
    message = "Login Failed"
    showData(message)
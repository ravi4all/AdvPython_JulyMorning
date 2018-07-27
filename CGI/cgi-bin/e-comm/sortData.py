#! C:/Python36/python.exe

import json
import cgi

form = cgi.FieldStorage()

toSearch = form.getvalue('search')
# toSearch = 'Samsung'

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
    <title>Title</title>
</head>
<body>
<div class='container'>
<h1>All Products</h1>
<hr>
<ul style='display:flex; flex-wrap:wrap;'>
""".format(toSearch))

with open('data.json') as data_file:
    data = json.load(data_file)
    # print(type(data))
    # print(data)
    data = sorted(data, key=lambda x : x['price'])
    for row in data:
        if row['name'].lower() == toSearch.lower():
            print("""<li class='list-group-item'> <img src={} class='pImage' style='width:50%;'>
                            <p>{} Price : {}</p>
                    </li>"""
                  .format(row['img'], row['name'], row['price']))

print("""
</div>
</body>
</html>
""")
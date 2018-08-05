#!C:/Python36/python.exe

import cgi, os

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['file_data']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open( fn, 'wb').write(fileitem.file.read())
   # a = open(fn,"rb")
   # str = a.read()

   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No file was uploaded'
   
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('</head>')
print('<body>')
print('<h2>%s</h2>' % message)
#print('%s' % str)
print("<img src='../{}' alt='Image'>".format(fn))
print('</body>')
print('</html>')

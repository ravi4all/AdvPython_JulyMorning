import socket

s = socket.socket()

port = 9999

s.bind(('localhost',port))

s.listen(5)
print("Listening on port",port)
print("Waiting for client...")
msg = "Thankyou for connecting with us"
while True:
    client,address = s.accept()
    print("Got connection from",address)

    client.send(msg.encode())

    client.close()
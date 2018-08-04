import socket

s = socket.socket()

port = 9999

s.bind(('localhost',port))

s.listen(5)
print("Listening on port",port)
print("Waiting for client...")
client,address = s.accept()
while True:

    print("Got connection from",address)

    data = client.recv(1024)
    data = data.decode()
    print("Client :",data)

    toSend = input("Server : ")

    client.send(toSend.encode())

client.close()
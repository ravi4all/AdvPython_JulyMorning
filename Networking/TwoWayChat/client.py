import socket

s = socket.socket()

port = 9999

s.connect(('127.0.0.1',port))

while True:
    msg = input("-> : ")
    s.send(msg.encode())

    data = s.recv(1024)
    print("Server :",data.decode())

s.close()
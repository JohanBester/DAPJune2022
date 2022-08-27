import socket

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mySock.send(cmd)

while True:
    data = mySock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mySock.close()

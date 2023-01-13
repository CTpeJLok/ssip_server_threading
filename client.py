import socket


host = input('Имя хоста: ')
port = input('Номер порта: ')

if not host:
    host = 'localhost'
if not port:
    port = 9091

sock = socket.socket()
sock.setblocking(1)

sock.connect((host,port))

while True:
    msg = input('Введите сообщение: ')

    sock.send(msg.encode())
    data = sock.recv(1024)
    if msg == 'exit':
        print('Клиент завершил свою работу!')
        break

    print("Сообщение от сервера :", data.decode())

sock.close()

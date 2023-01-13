import socket
import threading


def connect_port(host, port):
    sock = socket.socket()

    try:
        sock.connect((host, port))
        print(f"Порт {port} открыт\n")
    except (ConnectionError, OSError):
        pass

    sock.close()


hostname = input("Выберите hostname: ")
port = 0
print('Запуск сканирования!')

while port < 65500:
    if threading.active_count():
        t = threading.Thread(target=connect_port, args=(hostname, port))
        t.start()
        port += 1

print('Сканирование завершено!')

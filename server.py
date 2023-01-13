import socket
import threading


class ClientThreading(threading.Thread):
    def __init__(self, addr, conn):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr

        print (f"Новое подключение от {self.addr}")

    def run(self):
        print (f"Подключение от {self.addr}")

        while True:
            data = self.conn.recv(2048)

            msg = data.decode()
            if msg == 'exit':
                break

            print (f"Сообщение от {self.addr}: {msg}")
            self.conn.send(msg.encode())

        print (f"Клиент {self.addr} отключился!")

host = "localhost"
port = 9091

TYPE = socket.AF_INET
PROTOCOL = socket.SOCK_STREAM
sock = socket.socket(TYPE,PROTOCOL)
sock.bind((host, port))

print("Включение сервера!")
print("Ожидание подключения клиента...")

while True:
    sock.listen(5)
    conn, addr = sock.accept()
    thread = ClientThreading(addr[0], conn)
    thread.start()

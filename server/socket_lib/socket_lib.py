# 1) написать функцию обработки сокето запросов для потоков
#   1. ПРоверить если ли авторизация
#       если нет  то 2.
#       если да добавить сообщение в бд, сгенерировать ответ
#   2. проверить запрос ли это на авторизацию
#       если да то авторизовать
#       если нет то дропать
#
# 2) проверить установку на  соденинение по сокету
# 3) добавить новый сокет в поток
#
#
#
import sys, json
sys.path.append("..")
from threading import Thread, Lock
import select, time, random
from socket import socket, AF_INET, SOCK_STREAM
from message.message_lib import Message_lib as mes_lib

lock = Lock()


class Soket:
    def __init__(self, addres='127.0.0.1', port=7777):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((addres, port))
        self.sock.listen(5)
        self.sock.settimeout(0.2)
        self.dict_buf_client = {}
        self.clients = []

    def __delete__(self, instance):
        self.sock.close()

    def main(self):
        # global clients
        thrs_start = []
        self.clients = []
        thrs_start.append(
            Thread(target=self.func_thrs_accept, args=())
            # запуск потока с авторизацией
        )
        thrs_start.append(
            Thread(target=self.func_thrs_start_select, args=())
            # запуск потока для запуска потоков обработки клиентов
        )
        for t1 in thrs_start:
            t1.start()
    def func_thrs_accept(self):
        # функция отвечающая за подключение новых пользователей
        lock.acquire()
        print('start func_thrs_accept')
        while True:
            try:
                conn, addr = self.sock.accept()
            except OSError as e:
                pass
            else:
                print("connect %s" % str(addr))
                self.clients.append(conn)
        lock.release()
    def func_thrs_start_select(self):
        # функция в который будут запускатся потоки с обработкой клиентов
        print('start func_thrs_start_select')
        while True:
            thrs = []
            # lock.acquire()
            for client in self.clients:
                ip_port_client = client.getpeername()[0] + ':' + str(client.getpeername()[1]) # Получаем ip:port клиента
                # if thrs.count(client) == 0:
                if self.dict_buf_client.get(ip_port_client) == None:
                    tread = Thread(target=self.func_thrs_select(client,), args=())
                    thrs.append(tread)
                    self.dict_buf_client[ip_port_client] = tread
#                self.clients.remove(client)
            # lock.release()
            if thrs!=[]: print(thrs)

            for t in thrs:
                # if not t.isAlive():
                    t.start()
                    # t.start_new_thread()
            for t in thrs:
                t.join()
            # print('select')

    def func_thrs_select(self, client):
        # Функция обработка одного клиента
        # print('Поток старт')
        # обработка клиентов в потоке (в БД доступ ограниченб к сокету доступ ограничен)
        while True:
            w = []
            r = []
            try:
                r, w, _ = select.select([client], [client], [], 1)
                # if r != []:
                #     print('--------------------r----------------- ',r)
            except Exception as e:
                pass
            # my_mess.get_messege(r,)
            for read_mes in r:
                # self._read_mess(read_mes)
                mes_lib.get_messege(read_mes)

            # должны проверить входящее сообщение на авторизацию
            # r, self.dict_buf_client = Message_lib.Message.authorization(r, self.dict_buf_client)
            # Message_lib.Message.get_message_from_client(r)  # принятие сообщений
            # Message_lib.Message.handler_incom_massage()  # обработчик принятых сообщений
            # Message_lib.Message.send_message_from_client(r)  # отправка сообщений
            # print('end func_thrs_select')

    # def _read_mess(self, client):
    #     buf_mess = client.recv(640)
    #     json_mess = buf_mess.decode('utf-8')
    #     mess = json.loads(json_mess)
    #     print(mess)
    #     return mess

    # def send_mess(self, w):
    #     for write_client in w:
    #         pass

if __name__ == '__main__':
    sok = Soket()
    sok.main()

import sys
sys.path.append("..")
import datetime
from socket import socket, AF_INET, SOCK_STREAM
from message.message_lib import Type_message

import json

class Socket_client_send():
    # Написать две утелиты,
    # 1) сервер клиента которые считывает из БД (таблица 1) сообщение и по готовности отправляет, и меняет статус на прочитанные
    #    сервер пишит в БД (таблица 2) принятые сообщения
    # 2) клиент оболочка которая позвонялет в БД (таблица 1) записать сообщение на отправку
    #    считать сообщение из БД (таблица 2), пометить как прочитанное и вывести на экран
    def __init__(self, addres='127.0.0.1', port=7777):
        self.s = socket(AF_INET, SOCK_STREAM)
        self.s.connect((addres, port))
        self.connect = False

    def __delete__(self, instance):
        self.s.close()

    def _mess_send(self, message):
        message_json = json.dumps(message)
        message_buf = message_json.encode('utf-8')
        self.s.send(message_buf)
        pass
    def _mess_get(self):
        return mess
        pass

    def connect_server(self, *args, **kwargs):
        self.name = kwargs['name']
        self.passwd = kwargs['passwd']
        # message = {
        #     "action": "authenticate",
        #     "time": str(datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")),
        #     "user": {
        #         "account_name": self.name,
        #         "password": self.passwd,
        #     },
        # }
        # message_json = json.dumps(message)
        # message_buf = message_json.encode('utf-8')
        # self.s.send(message_buf)
        #записываем в БД сообщение на авторизацию
        self._mess_send(Type_message.authenticate(name=self.name, passed=self.passwd, id_mess=1))#id_mess надо брать из БД
        # print(message_buf)
        return 'send connect'

    # def send_mess(self, *args, **kwargs ):
    #     nameto = kwargs['nameto']
    #     msg = kwargs['msg']
    #     id_mess = kwargs['id_mess']
    #     message = {
    #         "action": "msg",
    #         "time": str(datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")),
    #         "to": nameto,
    #         "from": self.name,
    #         "id_mess": id_mess,
    #         "encoding": "utf-8",
    #         "message": msg,
    #     }
    #     print('Попытка отправки')
    #     message_json = json.dumps(message)
    #     message_buf = message_json.encode('utf-8')
    #     self.s.send(message_buf)
    #     print(message_buf)
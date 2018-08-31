import sys

sys.path.append("..")

import datetime
import json
from db.db_Alchemy import db_Alchimy as db

# # db = db_Alchemy.db_Alchimy
# session = db_Alchemy.db_Alchimy.init_db()
session = db.init_db()


class Message_lib:
    pass

    def get_messege(r, session=session):
        # принятие входящих сообщений
        ip_port_client = r.getpeername()[0] + ':' + str(
            r.getpeername()[1])  # Получаем ip:port клиента
        result = db.user_is_authorization(session, ip_port=ip_port_client)
        # Проверяем авторизован ли пользователь
        if result:
            print('Пользователь авторизован')
            try:
                # Клиент авторизован, пробуем получить сообщение
                mess = Message_lib._read_mess(r)
                print('mess ', mess)
            except:
                pass
                # не получилось получить сообзение, так как клиент мог отключится
            else:
                # print('-------------------------------------------------', mess,
                #       '----------------------------------------------------')
                Message_lib.write_get_mess_db(mess)
                # получино сообщение клиента, надо обработать
        else:
            print('Пользователь НЕ авторизован')
            # Пользователь не авторизован
            try:
                # print('reade mess авторизация')
                mess = Message_lib._read_mess(r)
                # пробуем получить сообщение от опльзователя
            except:
                pass
                # пользователь мог пропасть и сообщение не пришло, возможно надо удалить сокет
            else:
                Message_lib._authorization(mess, ip_port_client)

    def write_get_mess_db(mess, session=session):
        if mess['action'] == 'msg':
            user_to = mess['to']
            user_from = mess['from']
            id_user_from = db.get_id_user(session=session, name=user_from).uid
            if user_to == all:
                id_user_to = 0
            else:
                id_user_to = db.get_id_user(session=session, name=user_to)
            message = json.dumps(mess)
            status_mess = 's'
            if id_user_to != None:
                id_user_to = db.get_id_user(session=session, name=user_to).uid
                db.add_mess_get(session=session, id_user_to=id_user_to, id_user_from=id_user_from, mess=message,
                                status_mess=status_mess)
            else:
                db.add_mess_send(session=session, id_user_to=id_user_from, id_user_from=id_user_from,
                                 mess=json.dumps(_Response.codes_500(mess['id_mess'])), status_mess=status_mess)
                # сгенерировать ответ в виде ошибки об отуствие пользователя в системе

    def send_message():
        # отправка исхдящих сообщений
        pass

    def processing_message():
        # общая обработка сообщзений
        pass

    def _authorization(mess, ipport):
        print('Запись пользователя в БД')
        if mess['action'] == 'authenticate':
            db.add_user(session=session, name=mess['user']['account_name'], ip_port=ipport)
        else:
            print('user not authorization')

    def _read_mess(client):
        buf_mess = client.recv(640)
        json_mess = buf_mess.decode('utf-8')
        mess = json.loads(json_mess)
        return mess


class _Response():
    # Коды ошибкоу
    def codes_200(id_mess):
        message = {
            "response": 200,
            "id_mess": id_mess,
            "alert": "Не обезательное сообщение",
        }
        return message

    def codes_400(id_mess):
        message = {
            "response": 400,
            "id_mess": id_mess,
            "error": "Неправильный запрос/JSON-оъект",
        }
        return message

    def codes_500(id_mess):
        message = {
            "response": 500,
            "id_mess": id_mess,
            "error": "ошибка сервера",
        }
        return message


class _Type_message():
    def presonce(name, id_mess):
        message = {
            "action": "presence",
            "time": str(datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")),
            "type": "status",
            "id_mess": id_mess,
            "user": {
                "account_name": name,
                "status": "Yep",
            },
        }
        return message

    def authenticate(name, passed, id_mess):
        message = {
            "action": "authenticate",
            "time": str(datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")),
            "id_mess": id_mess,
            "user": {
                "account_name": name,
                "password": passed,
            },
        }
        return message

    def msg(msg, id_mess, to, from_):
        message = {
            "action": "msg",
            "time": str(datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S")),
            "id_mess": id_mess,
            "to": to,
            "from": from_,
            "encoding": "utf-8",
            "message": msg
        }
        return message

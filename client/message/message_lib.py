import datetime

class Type_message():
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
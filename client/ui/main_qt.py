import sys
sys.path.append("..")
from PyQt5 import Qt, QtGui, QtWidgets, QtCore
# from PyQt5.QtCore import (QCoreApplication, QObject, QRunnable, QThread, QThreadPool, pyqtSignal)
from threading import Thread, Lock
from ui.main_authorization_ui import Ui_MainWindow as ui_auth
# from .main_chat_ui import Ui_MainWindow as ui_main
from socket_lib.socket_lib import Socket_client_send as Socket
from db.db_Alchemy import db_Alchimy as db

class CMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_auth = ui_auth()
        self.ui_auth.setupUi(self)
        self.my_socket = Socket()
        self.my_db = db.init_db()
        thrs_start = []
        thrs_start.append(
            Thread(target=self.processing_mess_send_db, args=())
            # запуск потока для обработки сообщений на отправку
        )
        for t1 in thrs_start:
            t1.start()
    def processing_mess_send_db(self):
        # 1 заходим в БД и получаем список сообщений на отправку (сотретуем по статусу)
        # 2 пытаемся отправить сообщение
        # 3 меняем в БД статус сообщения
        pass
    def processing_mess_get_db(self):
        # 1 пытаемся получить сообщение
        # 2 добовляем полученое сообщение в БД
        pass
    def processing_mess_get(self):
        # 1 смотрим полученные сообщение в бд  (сортеруем по статусу)
        # 2 обробатываем сообщение по заданой логике и генерация ответов
        # 3 обновление статуса сообщения в БД
        pass
    def on_pushButton_join_pressed(self):
        # Попробовать авторизоватся
        # Если успешно, то открыть окрыть окно чата, а нынешнее закрыть.
        user = self.ui_auth.lineEdit_login.text()
        passwd = self.ui_auth.lineEdit_passwd.text()
        # print(f"user: {user} pass: {passwd}")
        result = self.my_socket.connect_server(name = user, passwd = passwd) #записываем в БД сообщение об авторизации
        print(result)
        return result
    # в отдельном цикле или потоке необходимо проверять сообщения на отправку и отправлять их.
    # в отдельном цикле или потоке необходимо проверять принятые сообщения и обробатывать их.

# if __name__ == '__main__':
#     CMain = CMainWindow


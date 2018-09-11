import sys
sys.path.append("..")
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from ui.main_authorization_ui import Ui_MainWindow as ui_auth
# from .main_chat_ui import Ui_MainWindow as ui_main
from socket_lib.socket_lib import Socket_client_send as Socket


class CMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_auth = ui_auth()
        self.ui_auth.setupUi(self)
        self.my_socket = Socket()

    def on_pushButton_join_pressed(self):
        # Попробовать авторизоватся
        # Если успешно, то открыть окрыть окно чата, а нынешнее закрыть.
        user = self.ui_auth.lineEdit_login.text()
        passwd = self.ui_auth.lineEdit_passwd.text()
        print(f"user: {user} pass: {passwd}")
        result = self.my_socket.connect_server(name = user, passwd = passwd)
        print(result)

# if __name__ == '__main__':
#     CMain = CMainWindow


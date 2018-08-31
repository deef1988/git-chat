from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from .main_authorization_ui import Ui_MainWindow as ui_auth
from .main_chat_ui import Ui_MainWindow as ui_main


class CMainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui_auth = ui_auth()
        self.ui_auth.setupUi(self)

    def on_pushButton_join_pressed(self):
        # Попробовать авторизоватся
        # Если успешно, то открыть окрыть окно чата, а нынешнее закрыть.
        pass

# if __name__ == '__main__':
#     CMain = CMainWindow


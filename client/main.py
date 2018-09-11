import sys
from PyQt5 import Qt
# from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from ui.main_qt import CMainWindow #as ui_class

app = Qt.QApplication(sys.argv)

dia = CMainWindow()
dia.show()

return_code = app.exec()
exit(return_code)

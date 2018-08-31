import sys
from PyQt5 import Qt
from ui.main_qt import CMainWindow

app = Qt.QApplication(sys.argv)

dia = CMainWindow()
dia.show()

return_code = app.exec()
exit(return_code)
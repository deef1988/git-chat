# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_authorization.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(248, 127)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_login.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.horizontalLayout_3.addWidget(self.lineEdit_login)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(70, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_passwd.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_passwd.setObjectName("lineEdit_passwd")
        self.horizontalLayout.addWidget(self.lineEdit_passwd)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_join = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_join.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_join.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_join.setObjectName("pushButton_join")
        self.verticalLayout_2.addWidget(self.pushButton_join, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_login, self.lineEdit_passwd)
        MainWindow.setTabOrder(self.lineEdit_passwd, self.pushButton_join)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Логин"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.pushButton_join.setText(_translate("MainWindow", "Вход"))


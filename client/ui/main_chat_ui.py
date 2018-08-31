# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_chat.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 481)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_chat = QtWidgets.QTextBrowser(self.centralwidget)
        self.main_chat.setMinimumSize(QtCore.QSize(300, 300))
        self.main_chat.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.main_chat.setOverwriteMode(True)
        self.main_chat.setObjectName("main_chat")
        self.horizontalLayout.addWidget(self.main_chat)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.list_user = QtWidgets.QListView(self.centralwidget)
        self.list_user.setMinimumSize(QtCore.QSize(0, 100))
        self.list_user.setMaximumSize(QtCore.QSize(16777215, 150))
        self.list_user.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list_user.setObjectName("list_user")
        self.gridLayout_2.addWidget(self.list_user, 0, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setMinimumSize(QtCore.QSize(80, 0))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout_2.addWidget(self.label_name)
        self.main_chat_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.main_chat_2.setObjectName("main_chat_2")
        self.horizontalLayout_2.addWidget(self.main_chat_2)
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_2.addWidget(self.pushButton_send)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.main_chat_2, self.pushButton_send)
        MainWindow.setTabOrder(self.pushButton_send, self.list_user)
        MainWindow.setTabOrder(self.list_user, self.main_chat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_name.setText(_translate("MainWindow", "Nicname"))
        self.pushButton_send.setText(_translate("MainWindow", "Отправить"))


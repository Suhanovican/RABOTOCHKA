# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pavel\Downloads\vhod.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets


class Vhod(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 331)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(120, 90, 139, 99))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Email = QtWidgets.QLabel(self.widget)
        self.Email.setObjectName("Email")
        self.gridLayout.addWidget(self.Email, 0, 0, 1, 1)
        self.Password = QtWidgets.QLabel(self.widget)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 3, 0, 1, 1)
        self.Pass_vod = QtWidgets.QLineEdit(self.widget)
        self.Pass_vod.setObjectName("Pass_vod")
        self.gridLayout.addWidget(self.Pass_vod, 4, 0, 1, 1)
        self.Email_Vod = QtWidgets.QLineEdit(self.widget)
        self.Email_Vod.setObjectName("Email_Vod")
        self.gridLayout.addWidget(self.Email_Vod, 1, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(210, 240, 195, 30))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Vhod = QtWidgets.QPushButton(self.widget1)
        self.Vhod.setObjectName("Vhod")
        self.gridLayout_2.addWidget(self.Vhod, 0, 0, 1, 1)
        self.Register = QtWidgets.QPushButton(self.widget1)
        self.Register.setObjectName("Register")
        self.gridLayout_2.addWidget(self.Register, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Вход"))
        self.Email.setText(_translate("MainWindow", "Почта"))
        self.Password.setText(_translate("MainWindow", "Пароль"))
        self.Vhod.setText(_translate("MainWindow", "Вход"))
        self.Register.setText(_translate("MainWindow", "Регистрация"))



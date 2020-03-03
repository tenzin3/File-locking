# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setPassword.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):

    def __init__(self,message):
        self.message=message
        print(self.message)

    def PassWordEntry(self):
        if self.lineEdit_ConfirmPassword.text()==self.lineEdit_Set_Pas.text()and self.lineEdit_ConfirmPassword.text()!="":
            #Add it to the sql data base
            conn=sqlite3.connect("info.db")
            c=conn.cursor()
            c.execute("INSERT INTO data_base VALUES (:first,:second)",{'first':self.message,'second':self.lineEdit_ConfirmPassword.text()})
            conn.commit()
            c.execute("SELECT *FROM data_base")
            print(c.fetchall())
            conn.close()
            #CLosing the Window
            LoginPage.close()


        else:
            self.lineEdit_Set_Pas.clear()
            self.lineEdit_ConfirmPassword.clear()

    def setupUi3(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(534, 229)
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_Set_Pas = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Set_Pas.setObjectName("lineEdit_Set_Pas")
        self.gridLayout_2.addWidget(self.lineEdit_Set_Pas, 0, 1, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_ConfirmPassword = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_ConfirmPassword.setObjectName("lineEdit_ConfirmPassword")
        self.gridLayout_2.addWidget(self.lineEdit_ConfirmPassword, 1, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        # Calling Function Path Add
        self.pushButton.clicked.connect(self.PassWordEntry)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        LoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "Login Page"))
        self.groupBox.setTitle(_translate("LoginPage", "Login"))
        self.label.setText(_translate("LoginPage", "Set Password"))
        self.label_2.setText(_translate("LoginPage", "Confirm Password"))
        self.pushButton.setText(_translate("LoginPage", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi3(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())

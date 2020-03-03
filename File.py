# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File-Locker.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os.path
from error2 import *
from setPassword import *
import sqlite3
from tkinter import *
from tkinter import filedialog

class Ui_MainWindow(object):
    def Path_Exist(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow2()
        self.ui.setupUi2(self.window)
        self.window.show()

    def Password_Entry(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LoginPage(self.message)
        self.ui.setupUi3(self.window)
        self.window.show()

    #For converting tuple into string
    def convertTuple(self,tup):
        str = ''.join(tup)
        return str

    def File_Path_Add(self):
        Get_String = self.lineEdit_FilePath_Add.text()

        r = Tk()
        r.withdraw()
        r.filename = filedialog.askopenfilename(filetypes=[("All types", "*.*")])

        #Checking if the path already exists in the list or not
        i=0
        List_No=self.listWidget_FilePath.count()
        while i <List_No:
                if self.listWidget_FilePath.item(i).text()==r.filename:
                    #Calling the error page
                    #Path alreay exit
                    self.Path_Exist()
                    break
                i=i+1
        #Adding the item in the list widget, if it doesnt exist
        if i == List_No or List_No==0:
                #Copying it in the message
                self.message=r.filename
                self.Password_Entry()

    def setupUi(self, MainWindow):
        #For counting items in List Widget
        self.count=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_FilePath_Add = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_FilePath_Add.setText("")
        self.lineEdit_FilePath_Add.setObjectName("lineEdit_FilePath_Add")
        self.gridLayout.addWidget(self.lineEdit_FilePath_Add, 0, 0, 1, 1)

        self.pushButton_Add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.gridLayout.addWidget(self.pushButton_Add, 0, 1, 1, 1)
        # Calling Function Path Add
        self.pushButton_Add.clicked.connect(self.File_Path_Add)


        self.listWidget_FilePath = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_FilePath.setObjectName("listWidget_FilePath")
        self.gridLayout.addWidget(self.listWidget_FilePath, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #########################################################
        conn = sqlite3.connect('info.db')
        c = conn.cursor()
        c.execute("SELECT File_path FROM data_base")
        temp=c.fetchall()
        for t in temp:
            str_temp=self.convertTuple(t)
            self.listWidget_FilePath.addItem(str_temp)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "$$FILE-LOCKER$$"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

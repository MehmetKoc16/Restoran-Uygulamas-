# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\pc\Desktop\KOD\Restoran Otomasyon\ui\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 500)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 330, 480))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 330, 480))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFE0B2, stop:1 #FFCC80);\n"
"border-radius: 15px;\n"
"border: 2px solid #FFA726;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 220, 120))
        font = QtGui.QFont()
        font.setPointSize(70)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #E65100;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 280, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #BF360C;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 210, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom: 2px solid #FFA000;\n"
"color: #5D4037;\n"
"padding-bottom: 7px;\n"
"border-radius: 4px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 260, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom: 2px solid #FFA000;\n"
"color: #5D4037;\n"
"padding-bottom: 7px;\n"
"border-radius: 4px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 320, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #FF9800;\n"
"}\n"
"\n"
"/* Hover efekti (üzerine gelindiğinde) */\n"
"QPushButton:hover {\n"
"    background-color: #FB8C00;\n"
"    border: 2px solid #FB8C00;\n"
"}\n"
"\n"
"/* Basılı durum efekti */\n"
"QPushButton:pressed {\n"
"    background-color: #F57C00;\n"
"    border: 2px solid #F57C00;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 370, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"    padding: 8px 16px;\n"
"    font-weight: bold;\n"
"    border: 2px solid #FF9800;\n"
"}\n"
"\n"
"/* Hover efekti (üzerine gelindiğinde) */\n"
"QPushButton:hover {\n"
"    background-color: #FB8C00;\n"
"    border: 2px solid #FB8C00;\n"
"}\n"
"\n"
"/* Basılı durum efekti */\n"
"QPushButton:pressed {\n"
"    background-color: #F57C00;\n"
"    border: 2px solid #F57C00;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 420, 250, 20))
        self.label_4.setStyleSheet("color: #BF360C;\n"
"font-size: 10px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Restoran Otomasyonu - Giriş"))
        self.label_2.setText(_translate("Form", "👨‍🍳"))
        self.label_3.setText(_translate("Form", "RESTORAN OTOMASYONU"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Kullanıcı Adı"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Şifre"))
        self.pushButton.setText(_translate("Form", "GİRİŞ"))
        self.pushButton_2.setText(_translate("Form", "KAYIT OL"))
        self.label_4.setText(_translate("Form", "Kullanıcı adı veya şifrenizi mi unuttunuz?"))

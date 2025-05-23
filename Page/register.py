# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\pc\Desktop\KOD\Restoran Otomasyon\ui\register.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 553)  # Yükseklik artırıldı
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 330, 530))  # Yükseklik artırıldı
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 330, 530))  # Yükseklik artırıldı
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #FFE0B2, stop:1 #FFB74D);\n"
"border-radius: 15px;\n"
"border: 2px solid #FFA726;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 220, 80))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #E65100;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 280, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #BF360C;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        # Kullanıcı Adı
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 160, 250, 35))
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
        
        # E-posta
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_email.setGeometry(QtCore.QRect(40, 210, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom: 2px solid #FFA000;\n"
"color: #5D4037;\n"
"padding-bottom: 7px;\n"
"border-radius: 4px;")
        self.lineEdit_email.setObjectName("lineEdit_email")
        
        # Telefon
        self.lineEdit_telefon = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_telefon.setGeometry(QtCore.QRect(40, 260, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_telefon.setFont(font)
        self.lineEdit_telefon.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom: 2px solid #FFA000;\n"
"color: #5D4037;\n"
"padding-bottom: 7px;\n"
"border-radius: 4px;")
        self.lineEdit_telefon.setObjectName("lineEdit_telefon")
        
        # Şifre
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 310, 250, 35))
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
        
        # Şifre Tekrar
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 360, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"border-bottom: 2px solid #FFA000;\n"
"color: #5D4037;\n"
"padding-bottom: 7px;\n"
"border-radius: 4px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        # Kaydet Butonu
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 250, 40))
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
        
        # Geri Butonu
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 460, 250, 40))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Restoran Otomasyonu - Kayıt"))
        self.label_2.setText(_translate("Form", "📝"))
        self.label_3.setText(_translate("Form", "YENİ KAYIT OLUŞTUR"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Kullanıcı Adı"))
        self.lineEdit_email.setPlaceholderText(_translate("Form", "  E-posta Adresi"))
        self.lineEdit_telefon.setPlaceholderText(_translate("Form", "  Telefon Numarası"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Şifre"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "  Şifre Tekrar"))
        self.pushButton.setText(_translate("Form", "KAYDET"))
        self.pushButton_2.setText(_translate("Form", "GİRİŞ EKRANINA DÖN"))
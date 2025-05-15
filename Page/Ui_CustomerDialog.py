# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomerDialog(object):
    def setupUi(self, CustomerDialog):
        CustomerDialog.setObjectName("CustomerDialog")
        CustomerDialog.resize(400, 350)
        CustomerDialog.setStyleSheet("""
            QDialog {
                background-color: #ECEFF1;
                border-radius: 10px;
            }
            QLabel {
                color: #303F9F;
                font-weight: bold;
            }
            QLineEdit {
                background-color: #F5F5F5;
                border: 1px solid #3F51B5;
                border-radius: 5px;
                padding: 5px;
                margin: 5px;
                color: #303F9F;
            }
            QPushButton {
                background-color: #3F51B5;
                color: #ECEFF1;
                border-radius: 8px;
                padding: 8px 16px;
                font-weight: bold;
                border: 2px solid #3F51B5;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #5C6BC0;
                border: 2px solid #5C6BC0;
            }
            QPushButton:pressed {
                background-color: #303F9F;
                border: 2px solid #303F9F;
            }
        """)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(CustomerDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        # Kullanıcı Adı
        self.label_username = QtWidgets.QLabel(CustomerDialog)
        self.label_username.setObjectName("label_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_username)
        
        self.lineEdit_username = QtWidgets.QLineEdit(CustomerDialog)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_username)
        
        # E-posta
        self.label_email = QtWidgets.QLabel(CustomerDialog)
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_email)
        
        self.lineEdit_email = QtWidgets.QLineEdit(CustomerDialog)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_email)
        
        # Telefon
        self.label_phone = QtWidgets.QLabel(CustomerDialog)
        self.label_phone.setObjectName("label_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_phone)
        
        self.lineEdit_phone = QtWidgets.QLineEdit(CustomerDialog)
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_phone)
        
        # Şifre
        self.label_password = QtWidgets.QLabel(CustomerDialog)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_password)
        
        self.lineEdit_password = QtWidgets.QLineEdit(CustomerDialog)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_password)
        
        # Şifre Tekrar (sadece yeni müşteri eklerken)
        self.label_confirm = QtWidgets.QLabel(CustomerDialog)
        self.label_confirm.setObjectName("label_confirm")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_confirm)
        
        self.lineEdit_confirm = QtWidgets.QLineEdit(CustomerDialog)
        self.lineEdit_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm.setObjectName("lineEdit_confirm")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_confirm)
        
        self.verticalLayout.addLayout(self.formLayout)
        
        # Butonlar
        self.buttonBox = QtWidgets.QDialogButtonBox(CustomerDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        
        self.retranslateUi(CustomerDialog)
        self.buttonBox.accepted.connect(CustomerDialog.accept)
        self.buttonBox.rejected.connect(CustomerDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CustomerDialog)

    def retranslateUi(self, CustomerDialog):
        _translate = QtCore.QCoreApplication.translate
        CustomerDialog.setWindowTitle(_translate("CustomerDialog", "Müşteri Bilgileri"))
        self.label_username.setText(_translate("CustomerDialog", "Kullanıcı Adı:"))
        self.label_email.setText(_translate("CustomerDialog", "E-posta:"))
        self.label_phone.setText(_translate("CustomerDialog", "Telefon:"))
        self.label_password.setText(_translate("CustomerDialog", "Şifre:"))
        self.label_confirm.setText(_translate("CustomerDialog", "Şifre Tekrar:"))

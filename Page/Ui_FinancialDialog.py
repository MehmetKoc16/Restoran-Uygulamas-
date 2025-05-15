# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FinancialDialog(object):
    def setupUi(self, FinancialDialog):
        FinancialDialog.setObjectName("FinancialDialog")
        FinancialDialog.resize(400, 300)
        FinancialDialog.setStyleSheet("""
            QDialog {
                background-color: #ECEFF1;
                border-radius: 10px;
            }
            QLabel {
                color: #303F9F;
                font-weight: bold;
            }
            QLineEdit, QComboBox, QDateEdit {
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
        
        self.verticalLayout = QtWidgets.QVBoxLayout(FinancialDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        # Tarih
        self.label_date = QtWidgets.QLabel(FinancialDialog)
        self.label_date.setObjectName("label_date")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_date)
        
        self.dateEdit = QtWidgets.QDateEdit(FinancialDialog)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        
        # Açıklama
        self.label_description = QtWidgets.QLabel(FinancialDialog)
        self.label_description.setObjectName("label_description")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_description)
        
        self.lineEdit_description = QtWidgets.QLineEdit(FinancialDialog)
        self.lineEdit_description.setObjectName("lineEdit_description")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_description)
        
        # Kategori
        self.label_category = QtWidgets.QLabel(FinancialDialog)
        self.label_category.setObjectName("label_category")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_category)
        
        self.comboBox_category = QtWidgets.QComboBox(FinancialDialog)
        self.comboBox_category.setObjectName("comboBox_category")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_category)
        
        # Tutar
        self.label_amount = QtWidgets.QLabel(FinancialDialog)
        self.label_amount.setObjectName("label_amount")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_amount)
        
        self.lineEdit_amount = QtWidgets.QLineEdit(FinancialDialog)
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_amount)
        
        self.verticalLayout.addLayout(self.formLayout)
        
        # Butonlar
        self.buttonBox = QtWidgets.QDialogButtonBox(FinancialDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        
        self.retranslateUi(FinancialDialog)
        self.buttonBox.accepted.connect(FinancialDialog.accept)
        self.buttonBox.rejected.connect(FinancialDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FinancialDialog)

    def retranslateUi(self, FinancialDialog):
        _translate = QtCore.QCoreApplication.translate
        FinancialDialog.setWindowTitle(_translate("FinancialDialog", "Finansal İşlem"))
        self.label_date.setText(_translate("FinancialDialog", "Tarih:"))
        self.label_description.setText(_translate("FinancialDialog", "Açıklama:"))
        self.label_category.setText(_translate("FinancialDialog", "Kategori:"))
        self.label_amount.setText(_translate("FinancialDialog", "Tutar (TL):"))

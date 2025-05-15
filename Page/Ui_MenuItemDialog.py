# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuItemDialog(object):
    def setupUi(self, MenuItemDialog):
        MenuItemDialog.setObjectName("MenuItemDialog")
        MenuItemDialog.resize(400, 300)
        MenuItemDialog.setStyleSheet("""
            QDialog {
                background-color: #ECEFF1;
                border-radius: 10px;
            }
            QLabel {
                color: #303F9F;
                font-weight: bold;
            }
            QLineEdit, QComboBox {
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
        
        self.verticalLayout = QtWidgets.QVBoxLayout(MenuItemDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        
        # Ürün Adı
        self.label_name = QtWidgets.QLabel(MenuItemDialog)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        
        self.lineEdit_name = QtWidgets.QLineEdit(MenuItemDialog)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_name)
        
        # Kategori
        self.label_category = QtWidgets.QLabel(MenuItemDialog)
        self.label_category.setObjectName("label_category")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_category)
        
        self.comboBox_category = QtWidgets.QComboBox(MenuItemDialog)
        self.comboBox_category.setObjectName("comboBox_category")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_category)
        
        # Fiyat
        self.label_price = QtWidgets.QLabel(MenuItemDialog)
        self.label_price.setObjectName("label_price")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_price)
        
        self.lineEdit_price = QtWidgets.QLineEdit(MenuItemDialog)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_price)
        
        self.verticalLayout.addLayout(self.formLayout)
        
        # Butonlar
        self.buttonBox = QtWidgets.QDialogButtonBox(MenuItemDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        
        self.retranslateUi(MenuItemDialog)
        self.buttonBox.accepted.connect(MenuItemDialog.accept)
        self.buttonBox.rejected.connect(MenuItemDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(MenuItemDialog)

    def retranslateUi(self, MenuItemDialog):
        _translate = QtCore.QCoreApplication.translate
        MenuItemDialog.setWindowTitle(_translate("MenuItemDialog", "Menü Öğesi"))
        self.label_name.setText(_translate("MenuItemDialog", "Ürün Adı:"))
        self.label_category.setText(_translate("MenuItemDialog", "Kategori:"))
        self.label_price.setText(_translate("MenuItemDialog", "Fiyat (TL):"))

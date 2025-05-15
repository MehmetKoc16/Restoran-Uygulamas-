# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        OrderDialog.setObjectName("OrderDialog")
        OrderDialog.resize(800, 600)
        OrderDialog.setStyleSheet("""
            QDialog {
                background-color: #ECEFF1;
                border-radius: 10px;
            }
            QLabel {
                color: #303F9F;
                font-weight: bold;
            }
            QLineEdit, QComboBox, QDateEdit, QSpinBox {
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
            QTableWidget {
                background-color: #F5F5F5;
                border: 1px solid #3F51B5;
                border-radius: 5px;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background-color: #5C6BC0;
                color: #FFFFFF;
            }
        """)
        
        self.verticalLayout = QtWidgets.QVBoxLayout(OrderDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Müşteri seçimi
        self.horizontalLayout_customer = QtWidgets.QHBoxLayout()
        self.horizontalLayout_customer.setObjectName("horizontalLayout_customer")
        
        self.label_customer = QtWidgets.QLabel(OrderDialog)
        self.label_customer.setObjectName("label_customer")
        self.horizontalLayout_customer.addWidget(self.label_customer)
        
        self.comboBox_customer = QtWidgets.QComboBox(OrderDialog)
        self.comboBox_customer.setObjectName("comboBox_customer")
        self.horizontalLayout_customer.addWidget(self.comboBox_customer)
        
        self.verticalLayout.addLayout(self.horizontalLayout_customer)
        
        # Ürün ekleme
        self.groupBox_product = QtWidgets.QGroupBox(OrderDialog)
        self.groupBox_product.setObjectName("groupBox_product")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_product)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label_category = QtWidgets.QLabel(self.groupBox_product)
        self.label_category.setObjectName("label_category")
        self.gridLayout.addWidget(self.label_category, 0, 0, 1, 1)
        
        self.comboBox_category = QtWidgets.QComboBox(self.groupBox_product)
        self.comboBox_category.setObjectName("comboBox_category")
        self.gridLayout.addWidget(self.comboBox_category, 0, 1, 1, 1)
        
        self.label_product = QtWidgets.QLabel(self.groupBox_product)
        self.label_product.setObjectName("label_product")
        self.gridLayout.addWidget(self.label_product, 1, 0, 1, 1)
        
        self.comboBox_product = QtWidgets.QComboBox(self.groupBox_product)
        self.comboBox_product.setObjectName("comboBox_product")
        self.gridLayout.addWidget(self.comboBox_product, 1, 1, 1, 1)
        
        self.label_quantity = QtWidgets.QLabel(self.groupBox_product)
        self.label_quantity.setObjectName("label_quantity")
        self.gridLayout.addWidget(self.label_quantity, 2, 0, 1, 1)
        
        self.spinBox_quantity = QtWidgets.QSpinBox(self.groupBox_product)
        self.spinBox_quantity.setObjectName("spinBox_quantity")
        self.spinBox_quantity.setMinimum(1)
        self.spinBox_quantity.setMaximum(100)
        self.gridLayout.addWidget(self.spinBox_quantity, 2, 1, 1, 1)
        
        self.pushButton_add = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 3, 1, 1, 1)
        
        self.verticalLayout.addWidget(self.groupBox_product)
        
        # Sipariş listesi
        self.label_order_list = QtWidgets.QLabel(OrderDialog)
        self.label_order_list.setObjectName("label_order_list")
        self.verticalLayout.addWidget(self.label_order_list)
        
        self.tableWidget_order = QtWidgets.QTableWidget(OrderDialog)
        self.tableWidget_order.setObjectName("tableWidget_order")
        self.tableWidget_order.setColumnCount(5)
        self.tableWidget_order.setHorizontalHeaderLabels(["Ürün ID", "Ürün Adı", "Birim Fiyat", "Adet", "Toplam"])
        self.tableWidget_order.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_order.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_order.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.verticalLayout.addWidget(self.tableWidget_order)
        
        # Toplam tutar
        self.horizontalLayout_total = QtWidgets.QHBoxLayout()
        self.horizontalLayout_total.setObjectName("horizontalLayout_total")
        
        self.label_total = QtWidgets.QLabel(OrderDialog)
        self.label_total.setObjectName("label_total")
        self.label_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_total.addWidget(self.label_total)
        
        self.verticalLayout.addLayout(self.horizontalLayout_total)
        
        # Butonlar
        self.horizontalLayout_buttons = QtWidgets.QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName("horizontalLayout_buttons")
        
        self.pushButton_remove = QtWidgets.QPushButton(OrderDialog)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.horizontalLayout_buttons.addWidget(self.pushButton_remove)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_buttons.addItem(spacerItem)
        
        self.buttonBox = QtWidgets.QDialogButtonBox(OrderDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_buttons.addWidget(self.buttonBox)
        
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)
        
        self.retranslateUi(OrderDialog)
        self.buttonBox.accepted.connect(OrderDialog.accept)
        self.buttonBox.rejected.connect(OrderDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OrderDialog)

    def retranslateUi(self, OrderDialog):
        _translate = QtCore.QCoreApplication.translate
        OrderDialog.setWindowTitle(_translate("OrderDialog", "Sipariş"))
        self.label_customer.setText(_translate("OrderDialog", "Müşteri:"))
        self.groupBox_product.setTitle(_translate("OrderDialog", "Ürün Ekle"))
        self.label_category.setText(_translate("OrderDialog", "Kategori:"))
        self.label_product.setText(_translate("OrderDialog", "Ürün:"))
        self.label_quantity.setText(_translate("OrderDialog", "Adet:"))
        self.pushButton_add.setText(_translate("OrderDialog", "Ekle"))
        self.label_order_list.setText(_translate("OrderDialog", "Sipariş Listesi:"))
        self.label_total.setText(_translate("OrderDialog", "Toplam: 0.00 TL"))
        self.pushButton_remove.setText(_translate("OrderDialog", "Seçili Ürünü Kaldır"))

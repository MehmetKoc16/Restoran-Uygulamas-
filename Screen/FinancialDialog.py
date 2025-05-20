import sqlite3
from PyQt5 import QtWidgets, QtCore
from Page.Ui_FinancialDialog import Ui_FinancialDialog
from DataBase import database

class FinancialDialog(QtWidgets.QDialog):
    def __init__(self, transaction_type="income", parent=None):
        super().__init__(parent)
        self.ui = Ui_FinancialDialog()
        self.ui.setupUi(self)
        self.transaction_type = transaction_type 
        
        if transaction_type == "income":
            self.setWindowTitle("Gelir Ekle")
            self.load_income_categories()
        else:
            self.setWindowTitle("Gider Ekle")
            self.load_expense_categories()
    
    def load_income_categories(self):
        """Gelir kategorilerini yükle"""
        self.ui.comboBox_category.clear()
        self.ui.comboBox_category.addItem("Satış", "Satış")
        self.ui.comboBox_category.addItem("Diğer", "Diğer")
    
    def load_expense_categories(self):
        """Gider kategorilerini yükle"""
        self.ui.comboBox_category.clear()
        self.ui.comboBox_category.addItem("Malzeme", "Malzeme")
        self.ui.comboBox_category.addItem("Personel", "Personel")
        self.ui.comboBox_category.addItem("Kira", "Kira")
        self.ui.comboBox_category.addItem("Fatura", "Fatura")
        self.ui.comboBox_category.addItem("Diğer", "Diğer")
    
    def accept(self):
        """Diyalog kabul edildiğinde (OK butonuna basıldığında) çağrılır"""
        date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        description = self.ui.lineEdit_description.text()
        category = self.ui.comboBox_category.currentText()
        amount_text = self.ui.lineEdit_amount.text().replace(',', '.')
        
        if not description:
            QtWidgets.QMessageBox.warning(self, "Hata", "Açıklama boş olamaz!")
            return
            
        try:
            amount = float(amount_text)
            if amount <= 0:
                QtWidgets.QMessageBox.warning(self, "Hata", "Tutar sıfırdan büyük olmalıdır!")
                return
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Hata", "Geçerli bir tutar giriniz!")
            return
        
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("""
                CREATE TABLE IF NOT EXISTS finansal_islemler (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tarih TEXT,
                    aciklama TEXT,
                    kategori TEXT,
                    tutar REAL,
                    tip TEXT
                )
            """)
            
            c.execute("""
                INSERT INTO finansal_islemler (tarih, aciklama, kategori, tutar, tip) 
                VALUES (?, ?, ?, ?, ?)
            """, (date, description, category, amount, self.transaction_type))
            
            conn.commit()
            super().accept()
            
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Veritabanı hatası: {str(e)}")
        finally:
            conn.close()

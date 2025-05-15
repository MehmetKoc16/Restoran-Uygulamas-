import sqlite3
from PyQt5 import QtWidgets
from Page.Ui_MenuItemDialog import Ui_MenuItemDialog
from DataBase import database

class MenuItemDialog(QtWidgets.QDialog):
    def __init__(self, item_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_MenuItemDialog()
        self.ui.setupUi(self)
        self.item_id = item_id
        
        # Kategorileri yükle
        self.load_categories()
        
        # Eğer ürün ID'si varsa, düzenleme modunda çalış
        if item_id:
            self.setWindowTitle("Menü Öğesi Düzenle")
            self.load_item_data()
        else:
            self.setWindowTitle("Yeni Menü Öğesi Ekle")
    
    def load_categories(self):
        """Kategorileri combobox'a yükle"""
        self.ui.comboBox_category.clear()
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT id, ad FROM kategoriler ORDER BY ad")
            categories = c.fetchall()
            for category_id, name in categories:
                self.ui.comboBox_category.addItem(name, category_id)
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Kategoriler yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()
    
    def load_item_data(self):
        """Ürün verilerini yükle"""
        if not self.item_id:
            return
            
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT ad, kategori_id, fiyat FROM urunler WHERE id=?", (self.item_id,))
            item = c.fetchone()
            if item:
                name, category_id, price = item
                self.ui.lineEdit_name.setText(name)
                
                # Kategori seçimi
                index = self.ui.comboBox_category.findData(category_id)
                if index >= 0:
                    self.ui.comboBox_category.setCurrentIndex(index)
                
                self.ui.lineEdit_price.setText(str(price))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Ürün verileri yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()
    
    def accept(self):
        """Diyalog kabul edildiğinde (OK butonuna basıldığında) çağrılır"""
        # Form verilerini al
        name = self.ui.lineEdit_name.text()
        category_id = self.ui.comboBox_category.currentData()
        price_text = self.ui.lineEdit_price.text().replace(',', '.')  # Virgül yerine nokta kullan
        
        # Boş alan kontrolü
        if not name:
            QtWidgets.QMessageBox.warning(self, "Hata", "Ürün adı boş olamaz!")
            return
            
        if not category_id:
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen bir kategori seçin!")
            return
            
        # Fiyat kontrolü
        try:
            price = float(price_text)
            if price <= 0:
                QtWidgets.QMessageBox.warning(self, "Hata", "Fiyat sıfırdan büyük olmalıdır!")
                return
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Hata", "Geçerli bir fiyat giriniz!")
            return
        
        # Veritabanı işlemleri
        conn = database.create_connection()
        c = conn.cursor()
        try:
            if self.item_id:  # Düzenleme modu
                c.execute("""
                    UPDATE urunler 
                    SET ad=?, kategori_id=?, fiyat=? 
                    WHERE id=?
                """, (name, category_id, price, self.item_id))
            else:  # Yeni ürün ekleme modu
                c.execute("""
                    INSERT INTO urunler (ad, kategori_id, fiyat) 
                    VALUES (?, ?, ?)
                """, (name, category_id, price))
            
            conn.commit()
            super().accept()  # Diyaloğu kapat
            
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Veritabanı hatası: {str(e)}")
        finally:
            conn.close()

import sqlite3
from PyQt5 import QtWidgets, QtCore
from Page.Ui_OrderDialog import Ui_OrderDialog
from DataBase import database

class OrderDialog(QtWidgets.QDialog):
    def __init__(self, order_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_OrderDialog()
        self.ui.setupUi(self)
        self.order_id = order_id
        self.order_items = []
        
        self.load_customers()
        
        self.load_categories()

        self.ui.comboBox_category.currentIndexChanged.connect(self.load_products)
        self.ui.pushButton_add.clicked.connect(self.add_product_to_order)
        self.ui.pushButton_remove.clicked.connect(self.remove_product_from_order)

        if order_id:
            self.setWindowTitle("Sipariş Düzenle")
            self.load_order_data()
        else:
            self.setWindowTitle("Yeni Sipariş")
            self.load_products()
    
    def load_customers(self):
        """Müşterileri combobox'a yükle"""
        self.ui.comboBox_customer.clear()
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT id, kullanici_adi FROM kullanicilar WHERE kullanici_tipi != 'admin' ORDER BY kullanici_adi")
            customers = c.fetchall()
            for customer_id, username in customers:
                self.ui.comboBox_customer.addItem(username, customer_id)
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Müşteriler yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()
    
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
    
    def load_products(self):
        """Seçili kategoriye göre ürünleri combobox'a yükle"""
        self.ui.comboBox_product.clear()
        category_id = self.ui.comboBox_category.currentData()
        if category_id is None:
            return
            
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT id, ad, fiyat FROM urunler WHERE kategori_id=? ORDER BY ad", (category_id,))
            products = c.fetchall()
            for product_id, name, price in products:
                self.ui.comboBox_product.addItem(f"{name} - {price} TL", (product_id, name, price))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Ürünler yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()
    
    def load_order_data(self):
        """Sipariş verilerini yükle"""
        if not self.order_id:
            return
            
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("""
                SELECT kullanici_id FROM faturalar WHERE id=?
            """, (self.order_id,))
            order = c.fetchone()
            
            if order:
                customer_id = order[0]
                index = self.ui.comboBox_customer.findData(customer_id)
                if index >= 0:
                    self.ui.comboBox_customer.setCurrentIndex(index)
                
                c.execute("""
                    SELECT fu.urun_id, u.ad, u.fiyat, fu.adet
                    FROM fatura_urunler fu
                    JOIN urunler u ON fu.urun_id = u.id
                    WHERE fu.fatura_id=?
                """, (self.order_id,))
                items = c.fetchall()
                
                self.order_items.clear()
                self.ui.tableWidget_order.setRowCount(0)
                
                for item in items:
                    product_id, name, price, quantity = item
                    total = price * quantity
                    self.order_items.append((product_id, name, price, quantity, total))
                    self.update_order_table()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Sipariş verileri yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()
    
    def add_product_to_order(self):
        """Seçili ürünü sipariş listesine ekle"""
        product_data = self.ui.comboBox_product.currentData()
        if not product_data:
            return
            
        product_id, name, price = product_data
        quantity = self.ui.spinBox_quantity.value()
        total = price * quantity
        
        for i, item in enumerate(self.order_items):
            if item[0] == product_id:
                new_quantity = item[3] + quantity
                new_total = item[2] * new_quantity
                self.order_items[i] = (product_id, name, price, new_quantity, new_total)
                self.update_order_table()
                return
        
        self.order_items.append((product_id, name, price, quantity, total))
        self.update_order_table()
    
    def remove_product_from_order(self):
        """Seçili ürünü sipariş listesinden kaldır"""
        selected_row = self.ui.tableWidget_order.currentRow()
        if selected_row >= 0:
            self.order_items.pop(selected_row)
            self.update_order_table()
    
    def update_order_table(self):
        """Sipariş tablosunu güncelle"""
        self.ui.tableWidget_order.setRowCount(0)
        total_amount = 0
        
        for row_index, item in enumerate(self.order_items):
            product_id, name, price, quantity, total = item
            self.ui.tableWidget_order.insertRow(row_index)
            self.ui.tableWidget_order.setItem(row_index, 0, QtWidgets.QTableWidgetItem(str(product_id)))
            self.ui.tableWidget_order.setItem(row_index, 1, QtWidgets.QTableWidgetItem(name))
            self.ui.tableWidget_order.setItem(row_index, 2, QtWidgets.QTableWidgetItem(f"{price:.2f} TL"))
            self.ui.tableWidget_order.setItem(row_index, 3, QtWidgets.QTableWidgetItem(str(quantity)))
            self.ui.tableWidget_order.setItem(row_index, 4, QtWidgets.QTableWidgetItem(f"{total:.2f} TL"))
            total_amount += total
        
        self.ui.label_total.setText(f"Toplam: {total_amount:.2f} TL")
    
    def accept(self):
        """Diyalog kabul edildiğinde (OK butonuna basıldığında) çağrılır"""
        if not self.order_items:
            QtWidgets.QMessageBox.warning(self, "Hata", "Sipariş listesi boş olamaz!")
            return
            
        customer_id = self.ui.comboBox_customer.currentData()
        if not customer_id:
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen bir müşteri seçin!")
            return
        
        total_amount = sum(item[4] for item in self.order_items)
        
        conn = database.create_connection()
        c = conn.cursor()
        try:
            if self.order_id:
                c.execute("DELETE FROM fatura_urunler WHERE fatura_id=?", (self.order_id,))
                c.execute("""
                    UPDATE faturalar 
                    SET kullanici_id=?, toplam_tutar=? 
                    WHERE id=?
                """, (customer_id, total_amount, self.order_id))
                
                for product_id, _, _, quantity, _ in self.order_items:
                    c.execute("""
                        INSERT INTO fatura_urunler (fatura_id, urun_id, adet) 
                        VALUES (?, ?, ?)
                    """, (self.order_id, product_id, quantity))
            else:
                c.execute("""
                    INSERT INTO faturalar (kullanici_id, toplam_tutar) 
                    VALUES (?, ?)
                """, (customer_id, total_amount))
                
                fatura_id = c.lastrowid

                for product_id, _, _, quantity, _ in self.order_items:
                    c.execute("""
                        INSERT INTO fatura_urunler (fatura_id, urun_id, adet) 
                        VALUES (?, ?, ?)
                    """, (fatura_id, product_id, quantity))
            
            conn.commit()
            super().accept()
            
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Veritabanı hatası: {str(e)}")
        finally:
            conn.close()

import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from Page.Ui_admin import Ui_AdminPanel
from DataBase import database

class AdminWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AdminPanel()
        self.ui.setupUi(self)
        self.setWindowTitle("Admin Paneli")

        self.ui.btnLogout.clicked.connect(self.logout)

        self.ui.btnAddCustomer.clicked.connect(self.add_customer)
        self.ui.btnEditCustomer.clicked.connect(self.edit_customer)
        self.ui.btnDeleteCustomer.clicked.connect(self.delete_customer)
        self.ui.txtCustomerSearch.textChanged.connect(self.search_customer)

        self.ui.btnAddMenuItem.clicked.connect(self.add_menu_item)
        self.ui.btnEditMenuItem.clicked.connect(self.edit_menu_item)
        self.ui.btnDeleteMenuItem.clicked.connect(self.delete_menu_item)
        self.ui.cmbMenuCategory.currentIndexChanged.connect(self.filter_menu_items)

        self.ui.btnAddIncome.clicked.connect(self.add_income)
        self.ui.btnAddExpense.clicked.connect(self.add_expense)

        self.ui.btnNewOrder.clicked.connect(self.new_order)
        self.ui.btnEditOrder.clicked.connect(self.edit_order)
        self.ui.btnCancelOrder.clicked.connect(self.cancel_order)
        self.ui.cmbOrderStatusFilter.currentIndexChanged.connect(self.filter_orders)

        self.load_customers()
        self.load_menu_items()
        self.load_financial_data()
        self.load_orders()

    def logout(self):
        """Admin panelinden çıkış yap ve giriş ekranına dön"""
        from Screen.LoginWindow import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def load_customers(self):
        """Müşteri verilerini veritabanından yükle"""
        self.ui.customerTable.setRowCount(0)
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT id, kullanici_adi, telefon, email FROM kullanicilar WHERE kullanici_tipi != 'admin'")
            customers = c.fetchall()

            for row_index, customer in enumerate(customers):
                self.ui.customerTable.insertRow(row_index)
                for col_index, data in enumerate(customer):
                    self.ui.customerTable.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.customerTable.setItem(row_index, 4, QtWidgets.QTableWidgetItem(""))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Müşteri verileri yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()

    def add_customer(self):
        """Yeni müşteri ekle"""
        from Screen.CustomerDialog import CustomerDialog
        dialog = CustomerDialog(parent=self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_customers()
            QtWidgets.QMessageBox.information(self, "Başarılı", "Yeni müşteri başarıyla eklendi.")

    def edit_customer(self):
        """Seçili müşteriyi düzenle"""
        selected_row = self.ui.customerTable.currentRow()
        if selected_row >= 0:
            customer_id = self.ui.customerTable.item(selected_row, 0).text()
            from Screen.CustomerDialog import CustomerDialog
            dialog = CustomerDialog(customer_id=int(customer_id), parent=self)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.load_customers()
                QtWidgets.QMessageBox.information(self, "Başarılı", "Müşteri bilgileri başarıyla güncellendi.")
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen düzenlenecek bir müşteri seçin.")

    def delete_customer(self):
        """Seçili müşteriyi sil"""
        selected_row = self.ui.customerTable.currentRow()
        if selected_row >= 0:
            customer_id = self.ui.customerTable.item(selected_row, 0).text()
            customer_name = self.ui.customerTable.item(selected_row, 1).text()
            reply = QtWidgets.QMessageBox.question(self, "Onay",
                                                 f"Müşteri '{customer_name}' (ID: {customer_id}) silinecek. Emin misiniz?",
                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                conn = database.create_connection()
                c = conn.cursor()
                try:
                    c.execute("SELECT COUNT(*) FROM faturalar WHERE kullanici_id=?", (customer_id,))
                    fatura_sayisi = c.fetchone()[0]

                    if fatura_sayisi > 0:
                        reply = QtWidgets.QMessageBox.question(self, "Dikkat",
                                                            f"Bu müşteriye ait {fatura_sayisi} adet fatura bulunuyor. Müşteriyi silmek, bu faturaları da silecektir. Devam etmek istiyor musunuz?",
                                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                        if reply != QtWidgets.QMessageBox.Yes:
                            conn.close()
                            return

                        c.execute("""
                            DELETE FROM fatura_urunler
                            WHERE fatura_id IN (SELECT id FROM faturalar WHERE kullanici_id=?)
                        """, (customer_id,))

                        c.execute("DELETE FROM faturalar WHERE kullanici_id=?", (customer_id,))

                    c.execute("DELETE FROM kullanicilar WHERE id=?", (customer_id,))
                    conn.commit()
                    self.load_customers() 
                    QtWidgets.QMessageBox.information(self, "Başarılı", "Müşteri başarıyla silindi.")
                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.warning(self, "Hata", f"Müşteri silinirken hata oluştu: {str(e)}")
                finally:
                    conn.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen silinecek bir müşteri seçin.")

    def search_customer(self):
        """Müşteri ara"""
        search_text = self.ui.txtCustomerSearch.text().lower()
        for row in range(self.ui.customerTable.rowCount()):
            match_found = False
            for col in range(self.ui.customerTable.columnCount()):
                item = self.ui.customerTable.item(row, col)
                if item and search_text in item.text().lower():
                    match_found = True
                    break
            self.ui.customerTable.setRowHidden(row, not match_found)

    def load_menu_items(self):
        """Menü öğelerini veritabanından yükle"""
        self.ui.menuTable.setRowCount(0)
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("""
                SELECT u.id, u.ad, k.ad, u.fiyat, 'Var' as stok
                FROM urunler u
                JOIN kategoriler k ON u.kategori_id = k.id
            """)
            menu_items = c.fetchall()

            for row_index, item in enumerate(menu_items):
                self.ui.menuTable.insertRow(row_index)
                for col_index, data in enumerate(item):
                    self.ui.menuTable.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(data)))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Menü öğeleri yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()

    def add_menu_item(self):
        """Yeni menü öğesi ekle"""
        from Screen.MenuItemDialog import MenuItemDialog
        dialog = MenuItemDialog(parent=self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_menu_items() 
            QtWidgets.QMessageBox.information(self, "Başarılı", "Yeni menü öğesi başarıyla eklendi.")

    def edit_menu_item(self):
        """Seçili menü öğesini düzenle"""
        selected_row = self.ui.menuTable.currentRow()
        if selected_row >= 0:
            item_id = self.ui.menuTable.item(selected_row, 0).text()
            from Screen.MenuItemDialog import MenuItemDialog
            dialog = MenuItemDialog(item_id=int(item_id), parent=self)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.load_menu_items() 
                QtWidgets.QMessageBox.information(self, "Başarılı", "Menü öğesi başarıyla güncellendi.")
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen düzenlenecek bir menü öğesi seçin.")

    def delete_menu_item(self):
        """Seçili menü öğesini sil"""
        selected_row = self.ui.menuTable.currentRow()
        if selected_row >= 0:
            item_id = self.ui.menuTable.item(selected_row, 0).text()
            reply = QtWidgets.QMessageBox.question(self, "Onay",
                 f"Menü öğesi {item_id} silinecek. Emin misiniz?",
                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                conn = database.create_connection()
                c = conn.cursor()
                try:
                    c.execute("DELETE FROM urunler WHERE id=?", (item_id,))
                    conn.commit()
                    self.load_menu_items()
                    QtWidgets.QMessageBox.information(self, "Başarılı", "Menü öğesi başarıyla silindi.")
                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.warning(self, "Hata", f"Menü öğesi silinirken hata oluştu: {str(e)}")
                finally:
                    conn.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen silinecek bir menü öğesi seçin.")

    def filter_menu_items(self):
        """Kategori filtresine göre menü öğelerini filtrele"""
        selected_category = self.ui.cmbMenuCategory.currentText()
        if selected_category == "Tüm Kategoriler":
            for row in range(self.ui.menuTable.rowCount()):
                self.ui.menuTable.setRowHidden(row, False)
        else:
            for row in range(self.ui.menuTable.rowCount()):
                category_item = self.ui.menuTable.item(row, 2)
                if category_item and category_item.text() != selected_category:
                    self.ui.menuTable.setRowHidden(row, True)
                else:
                    self.ui.menuTable.setRowHidden(row, False)

    def load_financial_data(self):
        """Finansal verileri yükle"""
        self.ui.incomeTable.setRowCount(0)
        self.ui.expensesTable.setRowCount(0)

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
            conn.commit()

            c.execute("""
                SELECT tarih, 'Satış', toplam_tutar, 'Satış' as kategori
                FROM faturalar
                ORDER BY tarih DESC
            """)
            incomes = c.fetchall()

            total_income = 0
            for row_index, income in enumerate(incomes):
                self.ui.incomeTable.insertRow(row_index)
                for col_index, data in enumerate(income):
                    self.ui.incomeTable.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(data)))
                total_income += float(income[2])

            c.execute("""
                SELECT tarih, aciklama, tutar, kategori
                FROM finansal_islemler
                WHERE tip = 'income'
                ORDER BY tarih DESC
            """)
            financial_incomes = c.fetchall()

            start_row = self.ui.incomeTable.rowCount()
            for row_index, income in enumerate(financial_incomes):
                self.ui.incomeTable.insertRow(start_row + row_index)
                for col_index, data in enumerate(income):
                    self.ui.incomeTable.setItem(start_row + row_index, col_index, QtWidgets.QTableWidgetItem(str(data)))
                total_income += float(income[2])

            self.ui.lblTotalIncome.setText(f"Toplam Gelir: {total_income:.2f} TL")

            c.execute("""
                SELECT tarih, aciklama, tutar, kategori
                FROM finansal_islemler
                WHERE tip = 'expense'
                ORDER BY tarih DESC
            """)
            expenses = c.fetchall()

            total_expense = 0
            for row_index, expense in enumerate(expenses):
                self.ui.expensesTable.insertRow(row_index)
                for col_index, data in enumerate(expense):
                    self.ui.expensesTable.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(data)))
                total_expense += float(expense[2])

            self.ui.lblTotalExpenses.setText(f"Toplam Gider: {total_expense:.2f} TL")

            net_profit = total_income - total_expense
            self.ui.lblNetProfit.setText(f"Net Kâr: {net_profit:.2f} TL")

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Finansal veriler yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()

    def add_income(self):
        """Yeni gelir ekle"""
        from Screen.FinancialDialog import FinancialDialog
        dialog = FinancialDialog(transaction_type="income", parent=self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_financial_data()
            QtWidgets.QMessageBox.information(self, "Başarılı", "Yeni gelir başarıyla eklendi.")

    def add_expense(self):
        """Yeni gider ekle"""
        from Screen.FinancialDialog import FinancialDialog
        dialog = FinancialDialog(transaction_type="expense", parent=self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_financial_data() 
            QtWidgets.QMessageBox.information(self, "Başarılı", "Yeni gider başarıyla eklendi.")

    def load_orders(self):
        """Sipariş verilerini yükle"""
        self.ui.ordersTable.setRowCount(0)
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("""
                SELECT f.id, k.kullanici_adi, f.tarih, f.toplam_tutar, 'Tamamlandı' as durum, 'Detay' as detay
                FROM faturalar f
                JOIN kullanicilar k ON f.kullanici_id = k.id
                ORDER BY f.tarih DESC
            """)
            orders = c.fetchall()

            for row_index, order in enumerate(orders):
                self.ui.ordersTable.insertRow(row_index)
                for col_index, data in enumerate(order):
                    self.ui.ordersTable.setItem(row_index, col_index, QtWidgets.QTableWidgetItem(str(data)))
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Sipariş verileri yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()

    def new_order(self):
        """Yeni sipariş oluştur"""
        from Screen.OrderDialog import OrderDialog
        dialog = OrderDialog(parent=self)
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.load_orders() 
            self.load_financial_data()  
            QtWidgets.QMessageBox.information(self, "Başarılı", "Yeni sipariş başarıyla oluşturuldu.")

    def edit_order(self):
        """Seçili siparişi düzenle"""
        selected_row = self.ui.ordersTable.currentRow()
        if selected_row >= 0:
            order_id = self.ui.ordersTable.item(selected_row, 0).text()
            from Screen.OrderDialog import OrderDialog
            dialog = OrderDialog(order_id=int(order_id), parent=self)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.load_orders()  
                self.load_financial_data()  
                QtWidgets.QMessageBox.information(self, "Başarılı", "Sipariş başarıyla güncellendi.")
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen düzenlenecek bir sipariş seçin.")

    def cancel_order(self):
        """Seçili siparişi iptal et"""
        selected_row = self.ui.ordersTable.currentRow()
        if selected_row >= 0:
            order_id = self.ui.ordersTable.item(selected_row, 0).text()
            reply = QtWidgets.QMessageBox.question(self, "Onay",
                                                 f"Sipariş {order_id} iptal edilecek. Emin misiniz?",
                                                 QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.Yes:
                conn = database.create_connection()
                c = conn.cursor()
                try:
                    c.execute("DELETE FROM fatura_urunler WHERE fatura_id=?", (order_id,))

                    c.execute("DELETE FROM faturalar WHERE id=?", (order_id,))

                    conn.commit()
                    self.load_orders()  
                    self.load_financial_data()  
                    QtWidgets.QMessageBox.information(self, "Başarılı", "Sipariş başarıyla iptal edildi.")
                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.warning(self, "Hata", f"Sipariş iptal edilirken hata oluştu: {str(e)}")
                finally:
                    conn.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen iptal edilecek bir sipariş seçin.")

    def filter_orders(self):
        """Sipariş durumuna göre siparişleri filtrele"""
        selected_status = self.ui.cmbOrderStatusFilter.currentText()
        if selected_status == "Tüm Siparişler":
            for row in range(self.ui.ordersTable.rowCount()):
                self.ui.ordersTable.setRowHidden(row, False)
        else:
            for row in range(self.ui.ordersTable.rowCount()):
                status_item = self.ui.ordersTable.item(row, 4)
                if status_item and status_item.text() != selected_status:
                    self.ui.ordersTable.setRowHidden(row, True)
                else:
                    self.ui.ordersTable.setRowHidden(row, False)

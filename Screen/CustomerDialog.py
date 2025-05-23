import sqlite3
from PyQt5 import QtWidgets
from Page.Ui_CustomerDialog import Ui_CustomerDialog
from DataBase import database

class CustomerDialog(QtWidgets.QDialog):
    def __init__(self, customer_id=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_CustomerDialog()
        self.ui.setupUi(self)
        self.customer_id = customer_id
        
        if customer_id:
            self.setWindowTitle("Müşteri Düzenle")
            self.load_customer_data()
            self.ui.label_confirm.hide()
            self.ui.lineEdit_confirm.hide()
        else:
            self.setWindowTitle("Yeni Müşteri Ekle")
    
    def load_customer_data(self):
        """Müşteri verilerini yükle"""
        if not self.customer_id:
            return
            
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT kullanici_adi, email, telefon FROM kullanicilar WHERE id=?", (self.customer_id,))
            customer = c.fetchone()
            if customer:
                username, email, phone = customer
                self.ui.lineEdit_username.setText(username)
                self.ui.lineEdit_email.setText(email if email else "")
                self.ui.lineEdit_phone.setText(phone if phone else "")
                self.ui.lineEdit_password.setText("")
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Müşteri verileri yüklenirken hata oluştu: {str(e)}")
        finally:
            conn.close()
    
    def accept(self):
        """Diyalog kabul edildiğinde (OK butonuna basıldığında) çağrılır"""
        username = self.ui.lineEdit_username.text()
        email = self.ui.lineEdit_email.text()
        phone = self.ui.lineEdit_phone.text()
        password = self.ui.lineEdit_password.text()
        confirm = self.ui.lineEdit_confirm.text()
        
        if not username:
            QtWidgets.QMessageBox.warning(self, "Hata", "Kullanıcı adı boş olamaz!")
            return
            
        if email and ('@' not in email or '.' not in email):
            QtWidgets.QMessageBox.warning(self, "Hata", "Geçerli bir e-posta adresi giriniz!")
            return
            
        if phone and not all(c.isdigit() or c.isspace() for c in phone):
            QtWidgets.QMessageBox.warning(self, "Hata", "Geçerli bir telefon numarası giriniz!")
            return

        if not self.customer_id:
            if not password:
                QtWidgets.QMessageBox.warning(self, "Hata", "Şifre boş olamaz!")
                return
                
            if password != confirm:
                QtWidgets.QMessageBox.warning(self, "Hata", "Şifreler eşleşmiyor!")
                return

        conn = database.create_connection()
        c = conn.cursor()
        try:
            if self.customer_id: 
                if password: 
                    c.execute("""
                        UPDATE kullanicilar 
                        SET kullanici_adi=?, email=?, telefon=?, sifre=? 
                        WHERE id=?
                    """, (username, email, phone, password, self.customer_id))
                else:
                    c.execute("""
                        UPDATE kullanicilar 
                        SET kullanici_adi=?, email=?, telefon=? 
                        WHERE id=?
                    """, (username, email, phone, self.customer_id))
            else:
                c.execute("""
                    INSERT INTO kullanicilar (kullanici_adi, email, telefon, sifre, kullanici_tipi) 
                    VALUES (?, ?, ?, ?, ?)
                """, (username, email, phone, password, "kullanici"))
            
            conn.commit()
            super().accept()
            
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Hata", "Bu kullanıcı adı zaten kullanılıyor!")
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Veritabanı hatası: {str(e)}")
        finally:
            conn.close()

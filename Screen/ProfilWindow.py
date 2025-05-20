import sqlite3
from PyQt5 import QtWidgets
from Page.Ui_Profil import Ui_ProfilSayfasi
from DataBase import database

class ProfilWindow(QtWidgets.QWidget):
    def __init__(self, user_id, parent=None):
        super().__init__()
        self.user_id = user_id
        self.parent = parent
        self.ui = Ui_ProfilSayfasi()
        self.ui.setupUi(self)
        self.load_user_data()
        self.load_fatura_gecmisi()
        self.ui.guncelleButon.clicked.connect(self.uptade_profile)

    def load_user_data(self):
        conn = database.create_connection()
        c = conn.cursor()
        c.execute("SELECT kullanici_adi, email, telefon FROM kullanicilar WHERE id=?", (self.user_id,))
        user = c.fetchone()
        conn.close()

        if user:
            username, email, telefon = user
            self.ui.kullaniciAdiLineEdit.setText(username)
            self.ui.epostaLineEdit.setText(email)
            self.ui.sifreLineEdit.setText("")

    def load_fatura_gecmisi(self):
        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("""
                SELECT 
                    f.id,
                    f.tarih,
                    f.toplam_tutar,
                    GROUP_CONCAT(u.ad || ' x ' || fu.adet || ' = ' || (u.fiyat * fu.adet) || ' TL') as urunler
                FROM faturalar f
                LEFT JOIN fatura_urunler fu ON f.id = fu.fatura_id
                LEFT JOIN urunler u ON fu.urun_id = u.id
                WHERE f.kullanici_id = ?
                GROUP BY f.id
                ORDER BY f.tarih DESC
                LIMIT 10
            """, (self.user_id,))
            faturalar = c.fetchall()
            
            gecmis_text = ""
            for fatura in faturalar:
                fatura_id, tarih, toplam_tutar, urunler = fatura
                gecmis_text += f"Fatura No: {fatura_id}\n"
                gecmis_text += f"Tarih: {tarih}\n"
                gecmis_text += "Ürünler:\n"
                if urunler:
                    for urun in urunler.split(','):
                        gecmis_text += f"- {urun}\n"
                gecmis_text += f"Toplam Tutar: {toplam_tutar:.2f} TL\n"
                gecmis_text += "-" * 40 + "\n\n"
            
            self.ui.gecmisTextEdit.setText(gecmis_text)
        except sqlite3.Error as e:
            self.ui.gecmisTextEdit.setText("Fatura geçmişi yüklenirken bir hata oluştu.")
        finally:
            conn.close()

    def uptade_profile(self):
        username = self.ui.kullaniciAdiLineEdit.text()
        email = self.ui.epostaLineEdit.text()
        password = self.ui.sifreLineEdit.text()

        if not username or not email:
            QtWidgets.QMessageBox.warning(self, "Hata", "Kullanıcı adı ve e-posta alanları boş bırakılamaz!")
            return

        conn = database.create_connection()
        c = conn.cursor()
        try:
            if password:
                c.execute("UPDATE kullanicilar SET kullanici_adi=?, email=?, sifre=? WHERE id=?",
                         (username, email, password, self.user_id))
            else:
                c.execute("UPDATE kullanicilar SET kullanici_adi=?, email=? WHERE id=?",
                         (username, email, self.user_id))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Başarılı", "Profil bilgileri güncellendi!")
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Hata", f"Güncelleme sırasında bir hata oluştu: {str(e)}")
        finally:
            conn.close()

    def closeEvent(self, event):
        if self.parent:
            self.parent.show()
        event.accept()

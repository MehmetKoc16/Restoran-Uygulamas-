import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Page.Ui_Kart import Ui_KartBilgisiEkrani
from DataBase import database
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class KartWindow(QtWidgets.QWidget):
    def __init__(self, toplam_tutar, siparisler, parent_window=None, home_window=None, user_id=None):
        super().__init__()
        self.ui = Ui_KartBilgisiEkrani()
        self.ui.setupUi(self)
        self.setWindowTitle("Kart ile Ödeme")
        self.ui.label_toplam.setText(f"Toplam Tutar: {toplam_tutar:.2f} TL")
        self.ui.kart_numarasi.setMaxLength(16)
        self.toplam_tutar = toplam_tutar
        self.siparisler = siparisler
        self.parent_window = parent_window
        self.home_window = home_window
        self.user_id = user_id

        self.ui.odeme_btn.clicked.connect(self.odeme_tamamla)

    def odeme_tamamla(self):
        dosya_yolu, _ = QFileDialog.getSaveFileName(self, "Fatura Kaydet", "fatura.pdf", "PDF Dosyası (*.pdf)")
        if dosya_yolu:
            self.fatura_olustur(dosya_yolu)
            self.fatura_kaydet()

            # HomePage'i göster
            if self.home_window:
                self.home_window.show()
                if hasattr(self.home_window, 'profil_window'):
                    self.home_window.profil_window.load_fatura_gecmisi()

            if self.parent_window:
                self.parent_window.close()
            self.close()
            QMessageBox.information(self, "Başarılı", "Ödeme başarıyla tamamlandı!")

    def fatura_olustur(self, dosya_yolu):
        c = canvas.Canvas(dosya_yolu, pagesize=A4)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 800, "Restoran Otomasyonu - Fatura")
        
        # Tarih ve saat bilgisi
        from datetime import datetime
        now = datetime.now()
        c.setFont("Helvetica", 10)
        c.drawString(100, 780, f"Tarih: {now.strftime('%d/%m/%Y %H:%M')}")
        
        # Sipariş detayları
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, 750, "Siparis Detaylari:")
        c.setFont("Helvetica", 10)
        y = 730
        for urun, fiyat in self.siparisler:
            c.drawString(120, y, f"{urun}")
            c.drawString(400, y, f"{fiyat:.2f} TL")
            y -= 20
        
        # Toplam tutar
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y-20, "Toplam Tutar:")
        c.drawString(400, y-20, f"{self.toplam_tutar:.2f} TL")
        
        # Ödeme bilgileri
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y-50, "Ödeme Bilgileri:")
        c.setFont("Helvetica", 10)
        c.drawString(120, y-70, f"Ödeme Türü: Kart")
        c.drawString(120, y-90, f"Kart No: {self.ui.kart_numarasi.text()[:4]} **** **** {self.ui.kart_numarasi.text()[-4:]}")
        
        # Teşekkür mesajı
        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y-120, "Tesekkür Ederiz!")
        
        c.save()

    def fatura_kaydet(self):
        conn = database.create_connection()
        c = conn.cursor()
        try:
            # Faturayı kaydet
            c.execute("INSERT INTO faturalar (kullanici_id, toplam_tutar) VALUES (?, ?)",
                     (self.user_id, self.toplam_tutar))
            fatura_id = c.lastrowid

            # Fatura ürünlerini kaydet
            for urun, fiyat in self.siparisler:
                # Önce ürün ID'sini bul
                c.execute("SELECT id FROM urunler WHERE ad = ?", (urun,))
                urun_id = c.fetchone()[0]
                
                # Fatura ürününü kaydet
                c.execute("INSERT INTO fatura_urunler (fatura_id, urun_id, adet) VALUES (?, ?, ?)",
                         (fatura_id, urun_id, 1))  # Varsayılan olarak adet 1

            conn.commit()
        except sqlite3.Error as e:
            print(f"Fatura kaydedilirken hata oluştu: {e}")
        finally:
            conn.close()

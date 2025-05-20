import sqlite3
from PyQt5 import QtWidgets
from Page.Ui_MasaPage import Ui_MasaSayfasi
from DataBase import database

class MasaWindow(QtWidgets.QWidget):
    def __init__(self, masa_no, home_window, user_id):
        super().__init__()
        self.ui = Ui_MasaSayfasi()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Masa {masa_no} Sipariş Ekranı")
        self.masa_no = masa_no
        self.home_window = home_window
        self.user_id = user_id
        self.siparisler = []

        self.load_kategoriler()
        self.ui.kategori_secim.currentIndexChanged.connect(self.load_urunler)
        self.ui.urun_secim.currentIndexChanged.connect(self.print_selected_urun_id)
        self.ui.ekle_btn.clicked.connect(self.siparis_ekle)
        self.ui.odeme_btn.clicked.connect(self.odeme_yap)

    def load_kategoriler(self):
        self.ui.kategori_secim.clear()
        conn = database.create_connection()
        c = conn.cursor()
        c.execute("SELECT id, ad FROM kategoriler")
        kategoriler = c.fetchall()
        for kategori_id, ad in kategoriler:
            self.ui.kategori_secim.addItem(ad, int(kategori_id))
        conn.close()
        self.load_urunler()

    def load_urunler(self):
        self.ui.urun_secim.clear()
        kategori_id = self.ui.kategori_secim.currentData()
        if kategori_id is None:
            return
        conn = database.create_connection()
        c = conn.cursor()
        c.execute("SELECT id, ad, fiyat FROM urunler WHERE kategori_id=?", (kategori_id,))
        urunler = c.fetchall()
        for urun_id, ad, fiyat in urunler:
            self.ui.urun_secim.addItem(f"{ad} - {fiyat} TL", int(urun_id))
        conn.close()

    def get_selected_urun_id(self):
        urun_id = self.ui.urun_secim.currentData()
        return urun_id

    def print_selected_urun_id(self):
        urun_id = self.get_selected_urun_id()
        print("Seçili ürün id:", urun_id)

    def siparis_ekle(self):
        urun_id = self.get_selected_urun_id()
        if urun_id is None:
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen bir ürün seçin!")
            return
        conn = database.create_connection()
        c = conn.cursor()
        c.execute("SELECT ad, fiyat FROM urunler WHERE id=?", (urun_id,))
        urun = c.fetchone()
        conn.close()
        if urun:
            ad, fiyat = urun
            self.siparisler.append((ad, fiyat))
            self.ui.siparis_listesi.addItem(f"{ad} - {fiyat} TL")

    def odeme_yap(self):
        if not self.siparisler: 
            QtWidgets.QMessageBox.warning(self, "Uyarı", "Lütfen önce sipariş ekleyin!")
            return
            
        from Screen.OdemeWindow import OdemeWindow
        self.odeme_window = OdemeWindow(self.masa_no, self.siparisler, self, self.user_id)
        self.odeme_window.show()
        self.close() 

    def closeEvent(self, event):
        button = getattr(self.home_window.ui, f"masaButon{self.masa_no}")
        button.setText(f"Masa {self.masa_no} (Boş)")
        button.setEnabled(True)
        self.home_window.masa_durumlari[self.masa_no] = "Boş"
        event.accept()

from PyQt5 import QtWidgets
from Page.Ui_OdemePage import Ui_OdemeSecimEkrani

class OdemeWindow(QtWidgets.QWidget):
    def __init__(self, masa_no, siparisler, parent_window=None, user_id=None):
        super().__init__()
        self.ui = Ui_OdemeSecimEkrani()
        self.ui.setupUi(self)
        self.setWindowTitle(f"Masa {masa_no} Ödeme Ekranı")
        self.masa_no = masa_no
        self.siparisler = siparisler
        self.parent_window = parent_window
        self.home_window = parent_window.home_window if parent_window else None
        self.user_id = user_id
        toplam = self.hesapla_toplam_tutar()
        self.ui.label_toplam.setText(f"Toplam Tutar: {toplam:.2f} TL")
        self.ui.kart_btn.clicked.connect(self.kart_ile_ode)

    def hesapla_toplam_tutar(self):
        return sum(fiyat for ad, fiyat in self.siparisler)

    def kart_ile_ode(self):
        toplam = self.hesapla_toplam_tutar()
        from Screen.KartWindow import KartWindow
        self.kart_window = KartWindow(toplam, self.siparisler, self, self.home_window, self.user_id)
        self.kart_window.show()
        self.close()

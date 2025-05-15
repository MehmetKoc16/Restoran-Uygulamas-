from PyQt5 import QtWidgets
from Page.Ui_HomePage import Ui_AnaEkran

class HomeWindow(QtWidgets.QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.ui = Ui_AnaEkran()
        self.ui.setupUi(self)
        self.masa_durumlari = {i: "Boş" for i in range(1, 17)}
        self.setup_masa_buttons()
        self.setup_profil_button()

    def setup_masa_buttons(self):
        for i in range(1, 17):
            button = getattr(self.ui, f"masaButon{i}")
            button.clicked.connect(lambda checked, masa_no=i: self.open_masa(masa_no))

    def setup_profil_button(self):
        self.ui.profilButon.clicked.connect(self.show_profile)

    def show_profile(self):
        from Screen.ProfilWindow import ProfilWindow
        self.profil_window = ProfilWindow(self.user_id, self)
        self.profil_window.show()
        self.hide()

    def open_masa(self, masa_no):
        button = getattr(self.ui, f"masaButon{masa_no}")
        button.setText(f"Masa {masa_no} (Dolu)")
        button.setEnabled(False)
        self.masa_durumlari[masa_no] = "Dolu"
        from Screen.MasaWindow import MasaWindow
        self.masa_window = MasaWindow(masa_no, self, self.user_id)
        self.masa_window.show()
        self.hide()

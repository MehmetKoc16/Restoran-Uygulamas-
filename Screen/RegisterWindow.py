import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from Page.register import Ui_Form as RegisterForm
from DataBase import database

class RegisterWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Ana pencereyi frameless yap
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.ui = RegisterForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.register)
        self.ui.pushButton_2.clicked.connect(self.show_login)

    def register(self):
        username = self.ui.lineEdit.text()
        email = self.ui.lineEdit_email.text()
        telefon = self.ui.lineEdit_telefon.text()
        password = self.ui.lineEdit_2.text()
        confirm = self.ui.lineEdit_3.text()

        # Boş alan kontrolü
        if not all([username, email, telefon, password, confirm]):
            QtWidgets.QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun!")
            return

        # E-posta formatı kontrolü
        if '@' not in email or '.' not in email:
            QtWidgets.QMessageBox.warning(self, "Hata", "Geçerli bir e-posta adresi giriniz!")
            return

        # Telefon formatı kontrolü (basit kontrol)
        if not telefon.replace(' ', '').isdigit() or len(telefon.replace(' ', '')) < 10:
            QtWidgets.QMessageBox.warning(self, "Hata", "Geçerli bir telefon numarası giriniz!")
            return

        if password != confirm:
            QtWidgets.QMessageBox.warning(self, "Hata", "Şifreler eşleşmiyor!")
            return

        conn = database.create_connection()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO kullanicilar (kullanici_adi, email, telefon, sifre) VALUES (?, ?, ?, ?)", 
                     (username, email, telefon, password))
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Başarılı", "Kayıt başarılı!")
            self.show_login()
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.warning(self, "Hata", "Bu kullanıcı adı veya e-posta zaten kullanılıyor!")
        finally:
            conn.close()

    def show_login(self):
        from Screen.LoginWindow import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()

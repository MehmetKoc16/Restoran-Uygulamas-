import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui
from Page.login import Ui_Form as LoginForm
from DataBase import database

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Ana pencereyi frameless yap
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 150))
        self.ui = LoginForm()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.show_register)

    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        conn = database.create_connection()
        c = conn.cursor()
        c.execute("SELECT id, kullanici_tipi FROM kullanicilar WHERE kullanici_adi=? AND sifre=?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            user_id = user[0]
            kullanici_tipi = user[1] if len(user) > 1 else "kullanici"
            if kullanici_tipi == "admin" or username == "admin":  # veya başka bir admin kontrolü
                from Screen.AdminWindow import AdminWindow
                self.admin_panel = AdminWindow()
                self.admin_panel.show()
                self.close()
            else:
                from Screen.HomeWindow import HomeWindow
                self.home = HomeWindow(user_id)
                self.home.show()
                self.close()
        else:
            QtWidgets.QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

    def show_register(self):
        from Screen.RegisterWindow import RegisterWindow
        self.register = RegisterWindow()
        self.register.show()
        self.close()

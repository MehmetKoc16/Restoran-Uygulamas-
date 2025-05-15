import sys
import os
import sqlite3
from PyQt5 import QtWidgets
from DataBase import database
from Screen.LoginWindow import LoginWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Veritabanını başlat
    database.init_database()

    # Mevcut veritabanına kullanici_tipi sütununu ekle (eğer yoksa)
    conn = database.create_connection()
    c = conn.cursor()
    try:
        c.execute("ALTER TABLE kullanicilar ADD COLUMN kullanici_tipi TEXT DEFAULT 'kullanici'")
        conn.commit()
        print("kullanici_tipi sütunu eklendi.")
    except sqlite3.OperationalError:
        print("kullanici_tipi sütunu zaten var.")
    finally:
        conn.close()

    # Admin kullanıcısı ekle (eğer yoksa)
    conn = database.create_connection()
    c = conn.cursor()
    c.execute("SELECT id FROM kullanicilar WHERE kullanici_adi='admin'")
    admin = c.fetchone()
    if not admin:
        c.execute("""
            INSERT INTO kullanicilar (kullanici_adi, sifre, email, telefon, kullanici_tipi)
            VALUES (?, ?, ?, ?, ?)
        """, ("admin", "admin123", "admin@restoran.com", "5551234567", "admin"))
        conn.commit()
        print("Admin kullanıcısı eklendi.")
    conn.close()


    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

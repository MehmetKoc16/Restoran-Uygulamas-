import sqlite3

def create_connection():
    return sqlite3.connect("restoran.db")

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    # Kullanıcılar
    c.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tam_ad TEXT,
            kullanici_adi TEXT UNIQUE,
            sifre TEXT,
            email TEXT,
            telefon TEXT,
            kullanici_tipi TEXT DEFAULT 'kullanici'
        )
    """)
    # Kategoriler
    c.execute("""
        CREATE TABLE IF NOT EXISTS kategoriler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad TEXT UNIQUE
        )
    """)
    # Ürünler
    c.execute("""
        CREATE TABLE IF NOT EXISTS urunler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kategori_id INTEGER,
            ad TEXT,
            fiyat REAL,
            FOREIGN KEY (kategori_id) REFERENCES kategoriler(id)
        )
    """)
    # Faturalar
    c.execute("""
        CREATE TABLE IF NOT EXISTS faturalar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_id INTEGER,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            toplam_tutar REAL,
            FOREIGN KEY (kullanici_id) REFERENCES kullanicilar(id)
        )
    """)
    # Fatura Ürünleri
    c.execute("""
        CREATE TABLE IF NOT EXISTS fatura_urunler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fatura_id INTEGER,
            urun_id INTEGER,
            adet INTEGER DEFAULT 1,
            FOREIGN KEY (fatura_id) REFERENCES faturalar(id),
            FOREIGN KEY (urun_id) REFERENCES urunler(id)
        )
    """)
    conn.commit()
    conn.close()

def init_database():
    create_tables()
    # Varsayılan kategoriler
    conn = create_connection()
    c = conn.cursor()
    for kategori in ["🍔 Yiyecekler", "🥤 İçecekler", "🍰 Tatlılar"]:
        c.execute("INSERT OR IGNORE INTO kategoriler (ad) VALUES (?)", (kategori,))

    # Admin kullanıcısı ekle (eğer yoksa)
    c.execute("SELECT id FROM kullanicilar WHERE kullanici_adi='admin'")
    admin = c.fetchone()
    if not admin:
        c.execute("""
            INSERT INTO kullanicilar (kullanici_adi, sifre, email, telefon, kullanici_tipi)
            VALUES (?, ?, ?, ?, ?)
        """, ("admin", "admin123", "admin@restoran.com", "5551234567", "admin"))

    conn.commit()
    conn.close()
from DataBase import database
def add_sample_data():
    conn = database.create_connection()
    c = conn.cursor()
    try:
        c.execute("DELETE FROM urunler")
        print("Mevcut ürünler temizlendi.")
    except Exception as e:
        print(f"Ürünler temizlenirken hata: {e}")

    c.execute("SELECT id, ad FROM kategoriler")
    kategoriler = {ad: kid for kid, ad in c.fetchall()}

    if not kategoriler:
        print("Kategoriler bulunamadı, örnek veri eklenemedi.")
        conn.close()
        return

    yiyecekler = [
        ("Hamburger", 120), ("Pizza", 150), ("Patates Kızartması", 40)
    ]
    for ad, fiyat in yiyecekler:
        try:
            c.execute("INSERT INTO urunler (kategori_id, ad, fiyat) VALUES (?, ?, ?)",
                    (kategoriler["🍔 Yiyecekler"], ad, fiyat))
        except Exception as e:
            print(f"Yiyecek eklenirken hata: {e}")

    icecekler = [
        ("Kola", 20), ("Ayran", 15), ("Çay", 10)
    ]
    for ad, fiyat in icecekler:
        try:
            c.execute("INSERT INTO urunler (kategori_id, ad, fiyat) VALUES (?, ?, ?)",
                    (kategoriler["🥤 İçecekler"], ad, fiyat))
        except Exception as e:
            print(f"İçecek eklenirken hata: {e}")

    tatlilar = [
        ("Baklava", 60), ("Künefe", 70)
    ]
    for ad, fiyat in tatlilar:
        try:
            c.execute("INSERT INTO urunler (kategori_id, ad, fiyat) VALUES (?, ?, ?)",
                    (kategoriler["🍰 Tatlılar"], ad, fiyat))
        except Exception as e:
            print(f"Tatlı eklenirken hata: {e}")

    print("Örnek ürünler başarıyla eklendi.")
    conn.commit()
    conn.close()

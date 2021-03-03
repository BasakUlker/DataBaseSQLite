import sqlite3
import os

# veritabani dosyasi olusturmak icin connect fonk kullanilir
con = sqlite3.connect("notlar.db")

# veritabani uzerinde islemler icin cursor(imlec) kullanilir
cur = con.cursor()

# imlec olusturulduktan sonra veritabani icinde komutlari uygulayabilmemiz icin execute komutu kullanilir
cur.execute("CREATE TABLE IF NOT EXISTS ogrenciler (isim TEXT, soyisim TEXT, puan INTEGER)")
# veritabani icinde anahtar kelimeler kullanilir. yukaridaki ornekte buyuk harfle yazilan kelimeler anahtar kelimlerdir.
# ayni programi iki kez calistirirsak goruruz ki file already exist hatasi aliriz. bunun onune gecmek icin create table if not exist kullaniliriz.

# program ikinci kez calistirildiginda asagida veritabanina girilen degerler tekrar tabloya yazilir. bunun onune gecmek icin os kutuphanesindeki os.path.exists() fonksiyonunu bir if not blogu icinde kullaniriz. 
if not os.path.exists("notlar.db"):
    cur.execute("INSERT INTO ogrenciler (isim, soyisim, puan) VALUES (?,?,?)", ("Ali", "Yildiz", 80))
    cur.execute("INSERT INTO ogrenciler (isim, soyisim, puan) VALUES (?,?,?)", ("Basak", "Ulker", 90))


#girilen verileri silmek icin delete kullanilir:
cur.execute("DELETE FROM ogrenciler WHERE isim='Basak' ")

#girilen verileri guncellemek icin update anahtar kelimesi kullanilir.:
cur.execute("UPDATE ogrenciler SET isim='Bilge' WHERE isim='Ali' ")

#yukarida tablomuza veri girme islemi yaptik fakat verileri veritabanina islemedik. bunun icin commit komutunu kullaniriz.
con.commit()

cur.execute("SELECT * FROM ogrenciler")
#tablodan belirli bir satiri secmek icin select anahtarini kullaniriz, * isareti tum satirlari secmemizi saglar.

al = cur.fetchall()
#secilen satirlari almak icin fetchall fonksiyonu kullanilir.alinan verileri ekrana yazdiralim:
for i in al:
    print(i)

#programi kapattigimizde veritabani da otomatik olarak kapanir fakat bunu clo0se komutuyla da yapailiriz
con.close()

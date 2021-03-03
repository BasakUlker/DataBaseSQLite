import sqlite3
import os

con = sqlite3.connect("notlar.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS ogrenciler (isim TEXT, soyisim TEXT, puan INTEGER)")

if not os.path.exists("notlar.db"):
    cur.execute("INSERT INTO ogrenciler (isim, soyisim, puan) VALUES (?,?,?)", ("Ali", "Yildiz", 80))
    cur.execute("INSERT INTO ogrenciler (isim, soyisim, puan) VALUES (?,?,?)", ("Basak", "Ulker", 90))


cur.execute("DELETE FROM ogrenciler WHERE isim='Basak' ")

cur.execute("UPDATE ogrenciler SET isim='Bilge' WHERE isim='Ali' ")

con.commit()

cur.execute("SELECT * FROM ogrenciler")

al = cur.fetchall()
for i in al:
    print(i)

con.close()

import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("create table if not exists Students(id integer,ime text,prezime text,prosek float);")
conn.commit()
broj_sudenti = int(input("Kolku studenti ke vnesuvas: "))
for i in range(broj_sudenti):
    ime = input("Vnesi ime: ")
    prezime = input("Vnesi prezime: ")
    prosek = float(input("Vnesi prosek: "))
    cursor.execute(f'insert into Students(id,ime,prezime,prosek) values ({i},"{ime}","{prezime}", {prosek});')
    conn.commit()

studenti = cursor.execute("select * from Students").fetchall()
print(studenti)


conn.close()
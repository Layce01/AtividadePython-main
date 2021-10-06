import sqlite3
conector = sqlite3.connect("agenda.db")

cursor = conector.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos
        (
            NumContato   INTEGER PRIMARY KEY AUTOINCREMENT,
            nome        TEXT NOT NULL,
            cel     TEXT NOT NULL,
            tel    TEXT NOT NULL,
            email       TEXT NOT NULL,
            aniver TEXT NOT NULL
        )
    ''')

conector.commit()
cursor.close()
conector.close()

print("banco criado com sucesso")








import sqlite3

conexao = sqlite3.connect('bd.sqlite')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY, nome text NOT NULL, email text NOT NULL);"""

nome = "weliton"
email = "weliton@gmail.com"

cursor.execute(sql)

for index in range(2):
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))

cursor.execute('SELECT * FROM usuarios')
for usuario in cursor:
    print(list(usuario))

conexao.commit()
conexao.close()


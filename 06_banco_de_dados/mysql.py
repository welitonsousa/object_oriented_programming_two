import mysql.connector as mysql

conexao = mysql.connect(host='localhost', db='bdmysql', user='root', passwd='1234')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY, nome text NOT NULL, email text NOT NULL);"""

nome = "weliton"
email = "weliton@gmail.com"

cursor.execute(sql)

for index in range(2):
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (%s, %s)', (nome, email))

cursor.execute('SELECT * FROM usuarios')
for usuario in cursor:
    print(list(usuario))

conexao.commit()
conexao.close()


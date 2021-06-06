import mysql.connector as mysql

conexao = mysql.connect(host='localhost', db='bdmysql', user='root', passwd='1234')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY, nome text NOT NULL, senha VARCHAR(32) NOT NULL, email text NOT NULL);"""

nome = "weliton"
senha = '1234'
email = "darice@gmail.com"

cursor.execute(sql)

for i in range(5):
    cursor.execute('INSERT INTO usuarios_senha (nome, senha, email) VALUES (%s, MD5(%s), %s)', (nome, senha, email))

cursor.execute('SELECT * FROM usuarios_senha WHERE nome = %s AND senha = MD5(%s)',(nome, senha))

for c in cursor:
    print(c)

conexao.commit()
conexao.close()
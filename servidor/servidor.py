import socket
from pessoa import Pessoa
from conta import Conta
from historico import Historico

'''abrindo a conexao do servidor'''
ip = 'localhost'
porta = 8004
endereco = ((ip, porta))
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor_socket.bind(endereco)
servidor_socket.listen(1)
conexao, cliente = servidor_socket.accept()

id_conta_atual = None
print('conectado')

import sqlite3

bd = sqlite3.connect('bd.sqlite')
cursor = bd.cursor()

pessoas = """CREATE TABLE IF NOT EXISTS pessoas(id integer PRIMARY KEY, nome text NOT NULL, sobrenome text NOT NULL, cpf text NOT NULL);"""
contas = """CREATE TABLE IF NOT EXISTS contas(id integer PRIMARY KEY, id_pessoa integer NOT NULL, numero_conta text NOT NULL, saldo float NOT NULL, data_abertura text NOT NULL);"""
historicos = """CREATE TABLE IF NOT EXISTS historicos(id integer PRIMARY KEY, id_conta text NOT NULL, transacao text NOT NULL);"""

cursor.execute(pessoas)
cursor.execute(contas)
cursor.execute(historicos)

def stringEmArray(valor: str) -> list:
  '''
    converte uma string em array. Cada '/' indica o final de um endereco de memoria.
    Utilizada para receber uma resposta do cliente através de uma string
    O primeiro endereco de memoria da lista deve ser sempre o comando requerido pelo cliente
    :param valor: str
      string recebida para conversão
    :return: list
      retorna uma lista da string recebida
  '''
  valores = []
  string = ''
  for caractere in valor:
    if caractere != '/':
      string += caractere
    else:
      valores.append(string)
      string = ''
  return valores


def conta_existe(numero_conta: str, cursor):
  '''
   verifica se o numero da conta digitada pertence a uma conta
  :param numero_conta: str
    numero da conta que vai buscar
  :return:
    objeto conta -> Se a conta com tal número existir
    None -> Se não existir
  '''
  id_conta = Conta.busca_conta(numero_conta, cursor)
  if id_conta != False:
      return id_conta
  return None
 
while(True):
    '''
    o servidor recebe uma mensagem do cliente e retorna uma resposta se necessario.
    se a mensagem recebida for uma string vazia, o servidor é encerrado.
    '''
    mensagem_recebida = conexao.recv(1024).decode()    
    if mensagem_recebida == '':
      bd.commit()
      bd.close()
      conexao.close()
      break

    print('cliente: ' + mensagem_recebida)
    
    if mensagem_recebida != '':
      valores = stringEmArray(mensagem_recebida)
      
      print(valores)
      if valores[0] == 'cadastrar_cliente':

        retorno = Pessoa.cadastrar(valores[1], valores[2], valores[3], cursor)
        conexao.send(str(retorno).encode())


      if valores[0] == 'criar_conta':
        id_pessoa = Pessoa.busca_pessoa(valores[1], cursor)
        if (id_pessoa == False):
          numero = 0
          retorno = 'False'
        else:
          numero = Conta.criar_conta(id_pessoa, cursor)
          retorno = 'True'
        retorno = '{}/{}/'.format(retorno, numero)
        conexao.send(retorno.encode())

      if(valores[0] == 'total_contas'):
        total = len(list(cursor.execute('SELECT * from contas')))
        conexao.send(str(total).encode())

      if(valores[0] == 'conta_existe'):
        numero_conta = valores[1]
        id_conta_atual = conta_existe(numero_conta, cursor)
        if id_conta_atual == None:
          conexao.send('False'.encode())
        else:
          conexao.send('True'.encode())

      if(valores[0] == 'depositar'):
        valor_deposito = valores[1]
        retorno = str(Conta.depositar(id_conta_atual, float(valor_deposito), cursor, True))
        conexao.send(retorno.encode())

      if(valores[0] == 'sacar'):
        valor_saque = valores[1]
        retorno = str(Conta.sacar(id_conta_atual, float(valor_saque), cursor, True))
        conexao.send(retorno.encode())

      if(valores[0] == 'transferir'):
        valor = valores[1]
        id_destino = conta_existe(valores[2], cursor)
        if(id_destino == None):
          conexao.send('False'.encode())
        else:
          retorno = str(Conta.transferir(id_conta_atual, float(valor), id_destino, cursor))
          conexao.send(retorno.encode())

      if(valores[0] == 'extrato'):
        saldo, data_abertura = list(cursor.execute('SELECT saldo, data_abertura FROM contas WHERE id="{}"'.format(id_conta_atual)))[0]

        data_abertura = data_abertura.replace('/','-')
        retorno = str('{}/{}/'.format(data_abertura,saldo))
        conexao.send(retorno.encode())
      
      if(valores[0] == 'historico'):
        historico = Historico.get_historico(id_conta_atual, cursor)
        retorno = ''
        for i in historico:
          i = i.replace('/', '-')
          retorno += '{}/'.format(i)
        conexao.send(retorno.encode())
    bd.commit()

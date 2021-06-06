import socket
from pessoa import Pessoa
from conta import Conta

'''abrindo a conexao do servidor'''
ip = 'localhost'
porta = 8004
endereco = ((ip, porta))
servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor_socket.bind(endereco)
servidor_socket.listen(1)
conexao, cliente = servidor_socket.accept()

conta_atual = None
print('conectado')




import sqlite3

bd = sqlite3.connect('bd.sqlite')
cursor = bd.cursor()

pessoas = """CREATE TABLE IF NOT EXISTS pessoas(id integer PRIMARY KEY, nome text NOT NULL, sobrenome text NOT NULL, cpf text NOT NULL);"""
contas = """CREATE TABLE IF NOT EXISTS contas(id integer PRIMARY KEY, id_pessoa integer NOT NULL, numero_conta text NOT NULL, saldo float NOT NULL, data_abertura text NOT NULL);"""
historicos = """CREATE TABLE IF NOT EXISTS historicos(id integer PRIMARY KEY, numero_conta text NOT NULL, transacao text NOT NULL);"""

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


def conta_existe(numero_conta: str):
  '''
   verifica se o numero da conta digitada pertence a uma conta
  :param numero_conta: str
    numero da conta que vai buscar
  :return:
    objeto conta -> Se a conta com tal número existir
    None -> Se não existir
  '''
  conta = Conta.busca_conta(numero_conta)
  if conta != None:
      return conta
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
        pessoa = Pessoa.busca_pessoa(valores[1])
        if (pessoa == None):
          numero = 0
          retorno = 'False'
        else:
          numero = Conta.criar_conta(pessoa)
          retorno = 'True'
        retorno = '{}/{}/'.format(retorno, numero)
        conexao.send(retorno.encode())

      if(valores[0] == 'total_contas'):
        conexao.send(str(len(Conta.lista)).encode())

      if(valores[0] == 'conta_existe'):
        numero_conta = valores[1]
        conta_atual = conta_existe(numero_conta)
        if conta_atual == None:
          conexao.send('False'.encode())
        else:
          conexao.send('True'.encode())

      if(valores[0] == 'depositar'):
        valor_deposito = valores[1]
        retorno = str(Conta.depositar(conta_atual, float(valor_deposito)))
        conexao.send(retorno.encode())

      if(valores[0] == 'sacar'):
        valor_saque = valores[1]
        retorno = str(Conta.sacar(conta_atual, float(valor_saque)))
        conexao.send(retorno.encode())

      if(valores[0] == 'transferir'):
        valor = valores[1]
        conta_destino = conta_existe(valores[2])
        if(conta_destino == None):
          conexao.send('False'.encode())
        else:
          retorno = str(Conta.transferir(conta_atual, float(valor), conta_destino))
          conexao.send(retorno.encode())

      if(valores[0] == 'extrato'):
        data_abertura = conta_atual._data_abertura.replace('/','-')
        saldo = conta_atual._saldo
        retorno = str('{}/{}/'.format(data_abertura,saldo))
        conexao.send(retorno.encode())
      
      if(valores[0] == 'historico'):
        historico = Conta.historico(conta_atual)
        retorno = ''
        for i in historico:
          i = i.replace('/', '-')
          retorno += '{}/'.format(i)
        conexao.send(retorno.encode())

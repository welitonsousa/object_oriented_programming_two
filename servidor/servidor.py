import socket
from pessoa import Pessoa
from conta import Conta

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

def stringEmArray(valor: str) -> list:
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
    conta = Conta.busca_conta(numero_conta)
    if conta != None:
        return conta
    return None


while(True):
    mensagem_recebida = conexao.recv(1024).decode()    
    print('cliente: ' + mensagem_recebida)
    
    if mensagem_recebida != '':
      valores = stringEmArray(mensagem_recebida)
      
      print(valores)

      if valores[0] == 'cadastrar_cliente':
        retorno = Pessoa.cadastrar(valores[1], valores[2], valores[3])
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
        conta_atual = None
        conexao.send(retorno.encode())

      if(valores[0] == 'sacar'):
        valor_saque = valores[1]
        retorno = str(Conta.sacar(conta_atual, float(valor_saque)))
        conta_atual = None
        conexao.send(retorno.encode())

      if(valores[0] == 'transferir'):
        valor = valores[1]
        conta_destino = conta_existe(valores[2])
        if(conta_destino == None):
          conexao.send('False'.encode())
        else:
          retorno = str(Conta.transferir(conta_atual, float(valor), conta_destino))
          conta_atual = None
          conexao.send(retorno.encode())

      if(valores[0] == 'extrato'):
        data_abertura = conta_atual._data_abertura.replace('/','-')
        saldo = conta_atual._saldo
        retorno = str('{}/{}/'.format(data_abertura,saldo))
        conta_atual = None
        conexao.send(retorno.encode())
      

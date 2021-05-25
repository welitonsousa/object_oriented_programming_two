from pessoa import Pessoa
from historico import Historico
from datetime import datetime
import uuid


class Conta:

  '''
  recebe um titular, que é um objeto da classe Pessoa.
  '''
  
  lista = []
  '''
  lista: atributo estático da classe conta do tipo list
    armazena todas as contas criadas
  '''

  def __init__(self, titular: Pessoa):
    '''
    :param titular: objeto da classe Pessoa
      titular da conta
    :param saldo: float
      saldo da conta
    :param historico: classe Historico
      historico de transações da conta
    :param data_abertura: str
      data em que a conta foi criada
    :param numero: str
      id único que representa o numero da conta
    :return: não retorna nada
    '''
    self._titular = titular
    self._limite = 500
    self._saldo = 0
    self._historico = Historico()
    self._data_abertura = str(datetime.now().strftime('%d/%m/%Y %H:%M'))
    self._numero = str(uuid.uuid4())[:4]

  @property
  def saldo(self):
    return self._saldo

  @property
  def data_abertura(self):
    return self._data_abertura

  def criar_conta(pessoa: Pessoa):
    '''
    Cria a conta, que é uma instancia da classe pessoa.
    Adiciona a conta na variavel list
    :param pessoa: Objeto da classe pessoa
      O titular da conta
    :return: str
      O numero da conta
    '''
    conta = Conta(pessoa)
    Conta.lista.append(conta)
    return conta._numero
  
  def busca_conta(numero_buscar: str):
    '''
    verifica se o numero da conta digitada pertence a uma conta
    :param numero_buscar: str
      numero da conta que vai buscar
    :return:
      objeto conta -> Se a conta com tal número existir
      None -> Se não existir
    '''
    for conta in Conta.lista:
      if numero_buscar == conta._numero:
        return conta
    return None

  def sacar(self, valor: float) -> bool:
    '''
    saca um dinheiro de determinada conta
    :param self: objeto conta
      conta que realizará o saque
    :param valor: 
      valor do saque
    :raise:
      nao aceita sacar um valor maior que o saldo da conta
    :return: bool
      True -> se o saque foi realizado
      False -> se o saque não foi realizado
    '''
    if valor <= self._saldo:
      self._saldo -= valor
      self._historico.nova_trasacao('Saque\nData: {}\nValor:{}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor))
      return True
    return False

  def depositar(self, valor: float) -> bool:
    '''
    deposita um dinheiro em determinada conta
    :param self: objeto conta
      conta que receberá o deposito
    :param valor: 
      valor do deposito
    :return: bool
      returna True
    '''
    self._saldo += valor
    self._historico.nova_trasacao('Deposito\nData: {}\nValor:{}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor))
    return True

  def extrato(self) -> str:
    '''
    :param self: objeto conta
      conta para tirar o extrato
    :return: str
      string contem o numero da conta e o saldo atual
    '''
    self._historico.nova_trasacao('Extrato\nData: {}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M')))
    return 'Numero: {} \nSaldo: {}'.format(self._numero, self._saldo)

  def transferir(self, valor: float, destino) -> bool:
    '''
    transfere um valor de uma conta para outra
    :param self: objeto conta
      conta que enviará o deposito
    :param valor: float
      valor da transferencia
    :param destino: objeto conta
      conta que receberá o deposito
    :raise:
      nao aceita transferir um valor maior que o saldo da conta do remetente
    :return: bool
      True -> transferencia realizada
      False -> transferencia não realizada
    '''
    if self.sacar(valor):
      return destino.depositar(valor)
    return False
  
  def historico(self) -> list:
    '''
    :param self: objeto conta
      conta da qual vai ser impresso o historico
    :return: list
      returna uma lista com as transações
    '''
    return self._historico.get_historico()


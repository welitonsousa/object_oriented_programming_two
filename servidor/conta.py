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

  update_saldo = """UPDATE contas SET saldo=? WHERE id=?;"""

  def __init__(self, id_titular: int):
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
    self._id_titular = id_titular
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

  def criar_conta(id_pessoa: int, cursor):
    '''
    Cria a conta, que é uma instancia da classe pessoa.
    Adiciona a conta na variavel list
    :param pessoa: Objeto da classe pessoa
      O titular da conta
    :return: str
      O numero da conta
    '''
    conta = Conta(id_pessoa)
    print(conta._saldo)
    cursor.execute("INSERT INTO contas (id_pessoa, numero_conta, saldo, data_abertura) VALUES(?,?,?,?)", (conta._id_titular, conta._numero, conta._saldo, conta._data_abertura))
    return conta._numero
  
  def busca_conta(numero_buscar: str, cursor):
    '''
    verifica se o numero da conta digitada pertence a uma conta
    :param numero_buscar: str
      numero da conta que vai buscar
    :return:
      objeto conta -> Se a conta com tal número existir
      None -> Se não existir
    '''

    busca_conta = 'SELECT * FROM contas WHERE numero_conta="{}"'.format(numero_buscar)
    contasads = list(cursor.execute(busca_conta))

    if ( len(contasads) != 0):
      return contasads[0][0]
    return False

  def sacar(id_conta, valor: float, cursor) -> bool:
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
    saldo = list(cursor.execute('SELECT saldo FROM contas WHERE id={}'.format(id_conta)))[0][0]
    if valor <= saldo and valor > 0:
      saldo -= valor
      cursor.execute(Conta.update_saldo, (saldo, id_conta))
      return True
    return False

  def depositar(id_conta: str, valor: float, cursor) -> bool:
    '''
    deposita um dinheiro em determinada conta
    :param self: objeto conta
      conta que receberá o deposito
    :param valor: 
      valor do deposito
    :return: bool
      returna True
    '''
    saldo = list(cursor.execute('SELECT saldo FROM contas WHERE id="{}"'.format(id_conta)))[0][0]
    if valor > 0:
      saldo += valor
      cursor.execute(Conta.update_saldo, (saldo,  id_conta))
      return True
    return False

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


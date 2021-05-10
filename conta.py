from pessoa import Pessoa
from historico import Historico
from datetime import datetime
import uuid


class Conta:

  lista = []

  def __init__(self, titular: Pessoa):
    self._titular = titular
    self._limite = 500
    self._saldo = 0
    self._historico = Historico()
    self._numero = str(uuid.uuid4())

  def criar_conta(pessoa: Pessoa):
    conta = Conta(pessoa)
    Conta.lista.append(conta)
    return conta.numero
  
  def busca_conta(numero_buscar: str):
    for conta in Conta.lista:
      if numero_buscar == conta.numero:
        return conta
    return None

  @property
  def numero(self):
    self._numero

  def sacar(self, valor: float) -> bool:
    if valor <= self._saldo:
      self._saldo -= valor
      self._historico.novo_historico('Saque\nData: {}\nValor:{}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor))
      return True
    return False

  def depositar(self, valor: float) -> bool:
    self._saldo += valor
    self._historico.novo_historico('Deposito\nData: {}\nValor:{}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'), valor))
    return True

  def extrato(self) -> str:
    self._historico.novo_historico('Extrato\nData: {}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M')))
    return 'Numero: {} \nSaldo: {}'.format(self._numero, self._saldo)

  def transferir(self, valor: float, destino: Conta) -> bool:
    if self.sacar(valor):
      return destino.depositar(valor)
    return False
  
  @property
  def historico(self) -> list:
    return self._historico.get_historico
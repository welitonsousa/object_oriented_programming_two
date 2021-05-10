from pessoa import Pessoa
from historico import Historico
from datetime import datetime
import uuid


class Conta:
  def __init__(self, titular: Pessoa):
    self._titular = titular
    self._limite = 500
    self._saldo = 0
    self._historico = Historico()
    self._numero = str(uuid.uuid4())

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

  def estrato(self) -> str:
    self._historico.novo_historico('Extrato\nData: {}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M')))
    return 'Numero: {} \nSaldo: {}'.format(self._numero, self._saldo)

  def transfere(self, valor: float, destino) -> bool:
    if self.sacar(valor):
      return destino.depositar(valor)
    return False
  
  def getData(self) ->None:
     return self._historico.getData()
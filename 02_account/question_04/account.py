from person import Pessoa
from history import Historico
from datetime import datetime

class Conta:

  def __init__(self, titular: Pessoa):
    self._titular = titular
    self._limite = 500
    self._saldo = 0
    self._historico = Historico()
    self._numero = str(abs(hash('python')))

  def sacar(self, value: float) -> bool:
    if value <= self._saldo:
      self._saldo -= value
      self._historico.novo_historico('Saque\nData: {}\nValor:{}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'), value))
      return True
    return False

  def depositar(self, value: float) -> bool:
    self._saldo += value
    self._historico.novo_historico('Deposito\nData: {}\nValor:{}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M'), value))
    return True

  def estrato(self) -> str:
    self._historico.novo_historico('Extrato\nData: {}\n'.format(datetime.now().strftime('%d/%m/%Y %H:%M')))
    return 'Numero: {} \nSaldo: {}'.format(self._numero, self._saldo)

  def transfere(self, value: float, destino) -> bool:
    if self.sacar(value):
      return destino.depositar(value)
    return False
  
  def getData(self) ->None:
     return self._historico.getData()
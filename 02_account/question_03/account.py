from person import Pessoa

class Conta:
  _numero: str
  _titular: Pessoa
  _saldo: float
  _limite: float

  def __init__(self, titular: Pessoa):
    self._titular = titular
    self._limite = 500
    self._saldo = 0
    self._numero = str(abs(hash('python')))

  def sacar(self, value: float) -> bool:
    if value <= self._saldo:
      self._saldo -= value
      return True
    return False

  def depositar(self, value: float) -> bool:
    self._saldo += value
    return True

  def estrato(self) -> str:
    return 'Numero: {} \nSaldo: {}'.format(self._numero, self._saldo)

  def transfere(self, value: float, destino) -> bool:
    if self.sacar(value):
      return destino.depositar(value)
    return False

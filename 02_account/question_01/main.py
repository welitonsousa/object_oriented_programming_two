class Conta:
  _numero: str
  _titular: str
  _saldo: float
  _limite: float

  def __init__(self, titular: str):
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


conta = Conta('Weliton')

print(conta.estrato())
conta.depositar(500)

print(conta.sacar(500))
print(conta.estrato())

print(conta.sacar(200))
print(conta.estrato())
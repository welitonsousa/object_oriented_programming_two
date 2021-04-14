class Conta:
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

  def transfere(self, value: float, destino) -> bool:
    if self.sacar(value):
      return destino.depositar(value)
    return False

conta1 = Conta('Weliton')
conta2 = Conta('sergio')

conta1.depositar(299)

print(conta1.transfere(100, conta2))
print(conta1.estrato())
print(conta2.estrato())
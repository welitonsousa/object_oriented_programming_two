from account import Conta
from person import Pessoa

conta = Conta(Pessoa('weliton', 'sousa', '1234'))
conta2 = Conta(Pessoa('1111', 'so12usa', '12344'))

conta.depositar(300)
conta.sacar(200)

conta.transfere(50, conta2)

for historico in conta.getData():
  print(historico)
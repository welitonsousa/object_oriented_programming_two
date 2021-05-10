from conta import Conta
from pessoa import Pessoa
from clientes import Clientes

clientes = Clientes()


pessoa = Pessoa('weliton', 'sousa', '1234')
conta = Conta(pessoa)

clientes.adicionar_cliente(conta)



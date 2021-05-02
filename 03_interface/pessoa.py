class Pessoa:
  __slots__ = ['_nome', '_cpf', '_endereco', '_nascimento']
  
  def __init__(self, nome: str, cpf: str, endereco: str, nascimento: str):
    self._nome = nome
    self._cpf = cpf
    self._endereco = endereco
    self._nascimento = nascimento
  
  def getData(self):
    return {
      'nome': self._nome,
      'cpf': self._cpf,
      'endereco': self._endereco,
      'nascimento': self._nascimento
    }

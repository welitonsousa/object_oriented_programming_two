class Pessoa:

  __slots__ = ["_nome", "_cpf", "_endereco", "_telefone"]

  def __init__(self, nome: str, cpf: str, endereco: str, telefone: str):
    self._nome = nome
    self._cpf = cpf
    self._endereco = endereco
    self._telefone = telefone
  
  @property
  def data(self):
    return {
      "nome": self._nome,
      "cpf": self._cpf,
      "endereco": self._endereco,
      "telefone": self._telefone,
    }

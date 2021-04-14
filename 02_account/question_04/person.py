class Pessoa:
  _nome: str
  _sobrenome: str
  _cpf: str

  def __init__(self, nome: str, sobrenome: str, cpf: str):
    self._nome = nome
    self._sobrenome = sobrenome
    self._cpf = cpf

  def getData(self):
    return {
      nome: self._nome,
      sobrenome: self._sobrenome,
      cpf: self._cpf
    }
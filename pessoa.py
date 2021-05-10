class Pessoa:

  lista = []

  def __init__(self, nome: str, sobrenome: str, cpf: str):
    self._nome = nome
    self._sobrenome = sobrenome
    self._cpf = cpf

  def cadastrar(nome: str, sobrenome: str, cpf: str):
    if Pessoa.busca_pessoa(cpf) != None:
      return False

    Pessoa.lista.append(Pessoa(nome, sobrenome, cpf))
    return True

  property
  def cpf(self):
    return self._cpf

  def busca_pessoa(cpf_buscar: str):
    for pessoa in Pessoa.lista:
      if pessoa.cpf == cpf_buscar:
        return pessoa
    return None

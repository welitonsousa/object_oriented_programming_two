from pessoa import Pessoa

class Cadastro:
  _pessoas = []

  staticmethod
  def nova_pessoa(nova_pessoa: Pessoa) -> bool:
    _, pessoa = Cadastro.buscar_pessoas(nova_pessoa.getData()["cpf"])
    if not _:
      Cadastro._pessoas.append(nova_pessoa)
    return not _

  staticmethod
  def buscar_pessoas(cpf: str) -> list:
    for pessoa in Cadastro._pessoas:
      if pessoa.getData()["cpf"] == cpf:
        return [True, pessoa]
    return [False, None]

  staticmethod
  def pessoas() -> list:
    return Cadastro._pessoas;
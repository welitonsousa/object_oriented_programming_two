from pessoa import Pessoa


class Cadastro:
  _pessoas = []

  def nova_pessoa(self, nova_pessoa: Pessoa) -> bool:
    _, pessoa = self.buscar_pessoas(nova_pessoa.getData["cpf"])
    if not _:
      Cadastro._pessoas.append(nova_pessoa)
    return not _

  def buscar_pessoas(self, cpf: str) -> list:
    for pessoa in self._pessoas:
      if pessoa.getData["cpf"] == cpf:
        return [True, pessoa]
    return [False, None]

  def pessoas(self) -> list:
    return Cadastro._pessoas
class Historico:


  """
  classe para armazenar um array de strings referente ao historico de uma conta
  """
  def init(self):
    self._historico = []

  def nova_trasacao(self, valor: str) -> None:
    """
    adiciona uma nova transação feita na conta
    :param valor: string
      valor que será adicionado na operação realizada
    """
    
    self._historico.append(valor)

  def get_historico(self) -> list:
    """
    retornar todas as transações feitas na conta
    """
    return self._historico
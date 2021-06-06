class Historico:


  """
  classe para armazenar um array de strings referente ao historico de uma conta
  """
  def init(self):
    self._historico = []

  def nova_trasacao(id_conta: str, valor: str, cursor) -> None:
    """
    adiciona uma nova transação feita na conta
    :param valor: string
      valor que será adicionado na operação realizada
    """
    cursor.execute('INSERT INTO historicos (id_conta, transacao) VALUES(?, ?)', (id_conta, valor))

  def get_historico(id_conta:str, cursor) -> list:
    """
    retornar todas as transações feitas na conta
    """
    historico = list(cursor.execute('SELECT transacao FROM historicos WHERE id_conta="{}"'.format(id_conta)))
    retorno = []
    for i in historico:
      retorno.append(list(i)[0])
    return retorno
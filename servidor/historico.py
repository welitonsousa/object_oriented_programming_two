class Historico:


  """
  classe para armazenar um array de strings referente ao historico de uma conta
  """
  def init(self):
    self._historico = []

  def nova_trasacao(id_conta: str, valor: str, cursor, sinc) -> None:
    """
    adiciona uma nova transação feita na conta
    :param valor: string
      valor que será adicionado na operação realizada
    """
    sinc.acquire()
    cursor.execute('INSERT INTO historicos (id_conta, transacao) VALUES(%s, %s)', (int(id_conta), valor))
    sinc.release()

  def get_historico(id_conta:str, cursor) -> list:
    """
    retornar todas as transações feitas na conta
    """
    historico = []
    cursor.execute('SELECT id_conta, transacao FROM historicos')
    for transacao in cursor:
      print(transacao)
      if str(transacao[0]) == str(id_conta):
        historico.append(transacao[1])
    if len(historico) == 0:
      historico.append('')
    return historico
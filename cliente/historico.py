class Historico:

  def __init__(self):
    self._historico = []
  
  def nova_trasacao(self, valor: str) -> None:
    self._historico.append(valor)

  def get_historico(self) -> list:
    return self._historico
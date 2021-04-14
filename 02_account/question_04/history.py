class Historico:
  _historico: list

  def __init__(self):
    self._historico = []
  
  def novo_historico(self, value: str) -> None:
    self._historico.append(value)

  def getData(self) -> list:
    return self._historico
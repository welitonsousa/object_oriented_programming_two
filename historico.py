class Historico:

  def __init__(self):
    self._historico = []
  
  def novo_historico(self, valor: str) -> None:
    self._historico.append(valor)

  def getData(self) -> list:
    return self._historico
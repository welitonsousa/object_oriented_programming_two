from skimage import io
from matplotlib import pyplot as plt
from datetime import datetime
from person import Pessoa

class Fotografia:
  _counter = 0
  __slots__ = ["_foto", "_fotografo", "_proprietario", "_data"]

  def __init__(self, foto: str, fotografo: Pessoa, proprietario: Pessoa ):
    self._foto = io.imread(foto)
    self._fotografo = fotografo
    self._proprietario = proprietario
    self._data = str(datetime.now().strftime('%d/%m/%Y %H:%M'))
    Fotografia._counter += 1

  def mostrar_fotografia(self) -> None:
    plt.imshow(self._foto)
    plt.show()
  
  def propriedade_fotografia(self):
    return self._foto.shape

  @staticmethod
  def counter():
    return Fotografia._counter

  @property
  def data(self):
    return {
      "foto": self._foto,
      "fotografo": self._fotografo,
      "proprietario": self._proprietario,
      "data": self._data,
    }
  
  @data.setter
  def data(self, foto: str, fotografo: Pessoa, proprietario: Pessoa, data: str) -> None:
    self._foto = foto
    self._fotografo = fotografo
    self._proprietario = proprietario
    self._data = data

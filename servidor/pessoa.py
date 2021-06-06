class Pessoa:
  """
  Classe Pessoa tem a responsabilidade de criar objetos do seu respectivo tipo
  """
  lista = []

  """
  atibuto estatico para armazenar a lista de todas as pessoas criadas
  """

  def init(self, nome: str, sobrenome: str, cpf: str):
    """
    retorna um objeto da classe Pessoa

    :param nome: string
      contem o valor do nome da pessoa a ser criada
    :param sobrenome: string]
      sobrenome da pessoa a ser criada
    :param cpf: string
      deve ser um atributo único referente a pessoa a ser retornada
      
    """
    self._nome = nome
    self._sobrenome = sobrenome
    self._cpf = cpf

  def cadastrar(nome: str, sobrenome: str, cpf: str, cursor):
    """
    este método retorna um booleano dizendo se a pessoa foi cadastrada ou não no parametro estatico da classe

    :param nome: string
      contem o valor do nome da pessoa a ser criada
    :param sobrenome: string]
      sobrenome da pessoa a ser criada
    :param cpf: string
      deve ser um atributo único referente a pessoa a ser retornada
    """


    if Pessoa.busca_pessoa(cpf, cursor) == False:
      cursor.execute("INSERT INTO pessoas (nome, sobrenome, cpf) VALUES(?,?,?)", (nome, sobrenome, cpf))
      return True
    return False

  @property
  def cpf(self):
    """
    retorna o cpf de uma instancia de pessoa
    """
    return self._cpf

  def busca_pessoa(cpf_buscar: str, cursor):
    """
    retorna uma instancia de Pessoa quando o cpf foi encontrado no atributo estatico da classe
    :param cpf_buscar: string
      cpf a ser buscado
    """
    pessoa = list(cursor.execute('SELECT * FROM pessoas WHERE cpf = "{}"'.format(cpf_buscar)))
    if (len(pessoa)!= 0):
      return pessoa[0][0]
    return False

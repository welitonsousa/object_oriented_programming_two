from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from rotas import Rotas

'''realiza a conexao com o servidor'''
import socket
ip = 'localhost'
porta = 8004
endereco = ((ip, porta))
cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(endereco)

def stringEmArray(valor: str) -> list:
    '''
    converte uma string em array. Cada '/' indica o final de um endereco de memoria.
    Utilizada para receber uma resposta do servidor através de uma string
    :param valor: str
      string recebida para conversão
    :return: list
      retorna uma lista da string recebida
  '''
    valores = []
    string = ''
    for caractere in valor:
        if caractere != '/':
            string += caractere
        else:
            valores.append(string)
            string = ''
    return valores


class Main(QMainWindow, Rotas):
    '''
    define os metodos a serem chamados quando clicar nos botoes
    '''
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tela_menu.botao_login.clicked.connect(self.para_login)
        self.tela_menu.botao_criar_conta.clicked.connect(self.para_criar_conta)
        self.tela_menu.botao_cadastrar_cliente.clicked.connect(self.para_cadastrar_cliente)

        self.tela_menu.edit_numero_conta.setText('0')
        
        self.tela_cadastrar_cliente.botao_cadastrar.clicked.connect(self.cadastrar_cliente)
        self.tela_cadastrar_cliente.botao_menu.clicked.connect(self.para_menu)

        self.tela_criar_conta.botao_cadastrar.clicked.connect(self.criar_conta)
        self.tela_criar_conta.botao_menu.clicked.connect(self.para_menu)

        self.tela_login.botao_menu.clicked.connect(self.para_menu)
        self.tela_login.botao_depositar.clicked.connect(self.botao_depositar)
        self.tela_login.botao_sacar.clicked.connect(self.botao_sacar)
        
        self.tela_login.botao_extrato.clicked.connect(self.botao_extrato)

        self.tela_depositar.botao_depositar.clicked.connect(self.depositar)
        self.tela_depositar.botao_menu.clicked.connect(self.para_menu)

        self.tela_sacar.botao_menu.clicked.connect(self.para_menu)
        self.tela_sacar.botao_sacar.clicked.connect(self.sacar)

        self.tela_extrato.botao_menu.clicked.connect(self.para_menu)


        self.tela_login.botao_transferir.clicked.connect(self.botao_transferir)
        self.tela_transferir.botao_menu.clicked.connect(self.para_menu)
        self.tela_transferir.botao_transferir.clicked.connect(self.tranferir)

        self.tela_login.botao_historico.clicked.connect(self.botao_historico)
        self.tela_historico.botao_menu.clicked.connect(self.para_menu)
        self.conta_atual = None


    def cadastrar_cliente(self):
        """
        cadastra um cliente.
        Envia o nome, o sobrenome e o cpf para o servidor
        Imprime uma mensagem na tela informando se a conta foi criada ou se o CPF já estava cadastrado
        """
        nome = self.tela_cadastrar_cliente.edit_nome.text()
        sobrenome = self.tela_cadastrar_cliente.edit_sobrenome.text()
        cpf = self.tela_cadastrar_cliente.edit_cpf.text()

        if nome != '' and sobrenome != '' and cpf != '':
            cliente_socket.send('cadastrar_cliente/{}/{}/{}/'.format(nome,sobrenome,cpf).encode())
            retorno = cliente_socket.recv(1024).decode()
            if retorno == 'True':    
                self.mensagem('Sucesso', 'cadastrado com sucesso!')
                self.tela_cadastrar_cliente.edit_nome.setText('')
                self.tela_cadastrar_cliente.edit_sobrenome.setText('')
                self.tela_cadastrar_cliente.edit_cpf.setText('')
            else:
                self.mensagem('Erro', 'CPF já cadastrado')

    def criar_conta(self):
        """
        cria uma conta
        Envia o cpf para o servidor
        Imprime uma mensagem na tela informando o numero da conta criada ou se o cpf nao foi encontrado, e assim, a conta nao foi criada
        """
        cpf = self.tela_criar_conta.edit_cpf.text()
        if cpf != '':
            cliente_socket.send('criar_conta/{}/'.format(cpf).encode())
            retorno = cliente_socket.recv(1024).decode()
            retorno = stringEmArray(retorno)
            if retorno[0] == 'True':
                numero = 'numero da conta: ' + retorno[1]
                self.mensagem('Sucesso', numero)
                self.tela_criar_conta.edit_cpf.setText('')
                cliente_socket.send('total_contas/'.encode())
                total_contas = cliente_socket.recv(1024).decode()
                self.tela_menu.edit_numero_conta.setText(total_contas)
            else:
                self.mensagem('Erro', 'CPF não encontrado')

    def botao_extrato(self):
        """
        Envia o numero da conta para o servidor
        recebe a informação do servidor se a conta existe
        se existir, chama o metodo extrato
        se não existir, informa ao usuario
        """
        numero = self.tela_login.edit_numero_conta.text()
        cliente_socket.send('conta_existe/{}/'.format(numero).encode())
        retorno = cliente_socket.recv(1024).decode()
        if retorno == 'True':
            self.extrato()
            self.para_extrato()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def botao_depositar(self):
        """
        Envia o numero da conta para o servidor
        recebe a informação do servidor se a conta existe
        se existir, chama o metodo depositar
        se não existir, informa ao usuario
        """
        numero = self.tela_login.edit_numero_conta.text()
        cliente_socket.send('conta_existe/{}/'.format(numero).encode())
        retorno = cliente_socket.recv(1024).decode()
        if retorno == 'True':
            self.para_depositar()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def botao_sacar(self):
        """
        Envia o numero da conta para o servidor
        recebe a informação do servidor se a conta existe
        se existir, chama o metodo sacar
        se não existir, informa ao usuario
        """
        numero = self.tela_login.edit_numero_conta.text()
        cliente_socket.send('conta_existe/{}/'.format(numero).encode())
        retorno = cliente_socket.recv(1024).decode()
        if retorno == 'True':
            self.para_sacar()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def botao_transferir(self):
        """
        Envia o numero da conta para o servidor
        recebe a informação do servidor se a conta existe
        se existir, chama o metodo transferir
        se não existir, informa ao usuario
        """
        numero = self.tela_login.edit_numero_conta.text()
        cliente_socket.send('conta_existe/{}/'.format(numero).encode())
        retorno = cliente_socket.recv(1024).decode()
        if retorno == 'True':
            self.para_transferir()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def botao_historico(self):
        """
        Envia o numero da conta para o servidor
        recebe a informação do servidor se a conta existe
        se existir, chama o metodo historico
        se não existir, informa ao usuario
        """
        numero = self.tela_login.edit_numero_conta.text()
        cliente_socket.send('conta_existe/{}/'.format(numero).encode())
        retorno = cliente_socket.recv(1024).decode()
        if retorno == 'True':
            cliente_socket.send('historico/'.encode())
            retorno = cliente_socket.recv(1024).decode()

            self.tela_historico.lista_itens.clear()
            items = stringEmArray(retorno)
            for operacao in items:
                self.tela_historico.lista_itens.addItem(operacao)
            self.para_historico()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def depositar(self):
        """
        faz um deposito na conta do usuário logado e da um feedback visual atraves de um dialog em caso de sucesso ou de erro
        """
        valor = self.tela_depositar.edit_valor.text()
        if valor != '':
            cliente_socket.send('depositar/{}/'.format(valor).encode())
            retorno = cliente_socket.recv(1024).decode()
            if retorno == 'True':
                self.mensagem('Sucesso', 'Deposito realizado com sucesso')
                self.tela_depositar.edit_valor.setText('')
                self.para_login()
            else:
                self.mensagem('Erro', 'Algo deu errado')

    def sacar(self):
        """
        faz um saque na conta do usuário logado e da um feedback visual atraves de um dialog em caso de sucesso ou de erro
        """
        valor = self.tela_sacar.edit_valor.text()
        if valor != '':
            cliente_socket.send('sacar/{}/'.format(valor).encode())
            retorno = cliente_socket.recv(1024).decode()
            if retorno == 'True':
                self.mensagem('Sucesso', 'Saque realizado com sucesso')
                self.tela_sacar.edit_valor.setText('')
                self.para_login()
            else:
                self.mensagem('Erro', 'Algo deu errado')

    def tranferir(self):
        """
        faz uma transferência do usuário logado para a conta de numero informado e dá um feedback visual para caso de sucesso ou erro
        """
        valor = self.tela_transferir.edit_valor.text()
        destinatario = self.tela_transferir.edit_conta_Destinatario.text()
        if destinatario != '' and valor != '':
            cliente_socket.send('transferir/{}/{}/'.format(valor, destinatario).encode())
            retorno = cliente_socket.recv(1024).decode()
            if retorno == 'True':
                self.mensagem('Sucesso', 'Transferencia realizada com sucesso')
                self.para_login()
            else:
                self.mensagem('Erro', 'Algo deu errado')

    def extrato(self):
        """
        busca o extrato da conta logada e lista todos os elementos numa lista
        """
        cliente_socket.send('extrato/'.encode())
        retorno = cliente_socket.recv(1024).decode()
        retorno = stringEmArray(retorno)
        data_abertura = retorno[0]
        saldo = retorno[1]
        self.tela_extrato.edit_conta_aberta.setText(data_abertura)
        self.tela_extrato.edit_saldo.setText(saldo)
            
    def mensagem(self, titulo: str, mensagem: str):
        """
        mensagem que dispara um dialog na tela do usuário
        :param titulo: string
          titulo do dialog
        :param mensagem: string
          body do dialog
        """
        QMessageBox.information(None, titulo, mensagem)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

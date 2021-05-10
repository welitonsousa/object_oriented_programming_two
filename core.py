from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from rotas import Rotas
from conta import Conta
from pessoa import Pessoa


class Main(QMainWindow, Rotas):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.tela_menu.botao_login.clicked.connect(self.para_login)
        self.tela_menu.botao_criar_conta.clicked.connect(self.para_criar_conta)
        self.tela_menu.botao_cadastrar_cliente.clicked.connect(self.para_cadastrar_cliente)

        self.tela_menu.edit_numero_conta.setText(str(len(Conta.lista)))

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

        self.conta_atual = None

    def botao_extrato(self):
        self.conta_atual = self.conta_existe()
        if self.conta_atual != None:
            self.extrato()
            self.para_extrato()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def botao_depositar(self):
        self.conta_atual = self.conta_existe()
        if self.conta_atual != None:
            self.para_depositar()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def botao_sacar(self):
        self.conta_atual = self.conta_existe()
        if self.conta_atual != None:
            self.para_sacar()
        else:
            self.mensagem('Erro', 'Conta não encontrada')

    def depositar(self):
        valor = self.tela_depositar.edit_valor.text()
        if valor != '':
            if Conta.depositar(self.conta_atual, float(valor)):
                self.mensagem('Sucesso', 'Deposito realizado com sucesso')
                self.tela_depositar.edit_valor.setText('')
                self.para_login()
            else:
                self.mensagem('Erro', 'Algo deu errado')

    def sacar(self):
        valor = self.tela_sacar.edit_valor.text()
        if valor != '':
            if Conta.sacar(self.conta_atual, float(valor)):
                self.mensagem('Sucesso', 'Saque realizado com sucesso')
                self.tela_sacar.edit_valor.setText('')
                self.para_login()
            else:
                self.mensagem('Erro', 'Algo deu errado')

    def extrato(self):
        self.tela_extrato.edit_conta_aberta.setText(self.conta_atual.data_abertura)
        self.tela_extrato.edit_saldo.setText(str(self.conta_atual.saldo))

    def conta_existe(self):
        numero = self.tela_login.edit_numero_conta.text()
        conta = Conta.busca_conta(numero)
        if conta != None:
            return conta
        return None

    def cadastrar_cliente(self):
        nome = self.tela_cadastrar_cliente.edit_nome.text()
        sobrenome = self.tela_cadastrar_cliente.edit_sobrenome.text()
        cpf = self.tela_cadastrar_cliente.edit_cpf.text()

        if nome != '' and sobrenome != '' and cpf != '':
            if Pessoa.cadastrar(nome, sobrenome, cpf):
                self.mensagem('Sucesso', 'cadastrado com sucesso!')
                self.tela_cadastrar_cliente.edit_nome.setText('')
                self.tela_cadastrar_cliente.edit_sobrenome.setText('')
                self.tela_cadastrar_cliente.edit_cpf.setText('')
            else:
                self.mensagem('Erro', 'CPF já cadastrado')

    def criar_conta(self):
        cpf = self.tela_criar_conta.edit_cpf.text()
        if cpf != '':
            pessoa = Pessoa.busca_pessoa(cpf)
            if pessoa != None:
                numero = 'numero da conta: ' + str(Conta.criar_conta(pessoa))
                
                self.mensagem('Sucesso', numero)
                self.tela_criar_conta.edit_cpf.setText('')
                self.tela_menu.edit_numero_conta.setText(str(len(Conta.lista)))
            else:
                self.mensagem('Erro', 'CPF não encontrado')
            
    def mensagem(self, titulo: str, mensagem: str):
        QMessageBox.information(None, titulo, mensagem)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

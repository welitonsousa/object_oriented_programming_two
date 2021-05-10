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

    def mensagem(self, titulo: str, mensagem: str):
        QMessageBox.information(None, titulo, mensagem)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

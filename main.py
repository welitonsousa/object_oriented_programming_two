from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_cadastrar_cliente import TelaCadastrarCliente
from tela_criar_conta import TelaCriarConta
from tela_depositar import TelaDepositar
from tela_extrato import TelaExtrato
from tela_historico import TelaHistorico
from tela_login import TelaLogin
from tela_menu import TelaMenu
from tela_sacar import TelaSacar
from tela_transferir import TelaTransferir

from conta import Conta
from pessoa import Pessoa


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.controle_telas = QtWidgets.QStackedLayout()

        self.stack_cadastrar_cliente = QtWidgets.QMainWindow()
        self.stack_criar_conta = QtWidgets.QMainWindow()
        self.stack_depositar = QtWidgets.QMainWindow()
        self.stack_extrato = QtWidgets.QMainWindow()
        self.stack_historico = QtWidgets.QMainWindow()
        self.stack_login = QtWidgets.QMainWindow()
        self.stack_menu = QtWidgets.QMainWindow()
        self.stack_sacar = QtWidgets.QMainWindow()
        self.stack_transferir = QtWidgets.QMainWindow()

        self.tela_cadastrar_cliente = TelaCadastrarCliente()
        self.tela_cadastrar_cliente.setupUi(self.stack_cadastrar_cliente)

        self.tela_criar_conta = TelaCriarConta()
        self.tela_criar_conta.setupUi(self.stack_criar_conta)

        self.tela_depositar = TelaDepositar()
        self.tela_depositar.setupUi(self.stack_depositar)

        self.tela_extrato = TelaExtrato()
        self.tela_extrato.setupUi(self.stack_extrato)

        self.tela_historico = TelaHistorico()
        self.tela_historico.setupUi(self.stack_historico)

        self.tela_login = TelaLogin()
        self.tela_login.setupUi(self.stack_login)

        self.tela_menu = TelaMenu()
        self.tela_menu.setupUi(self.stack_menu)

        self.tela_sacar = TelaSacar()
        self.tela_sacar.setupUi(self.stack_sacar)

        self.tela_transferir = TelaTransferir()
        self.tela_transferir.setupUi(self.stack_transferir)

        self.index_cadastrar_cliente = 6
        self.index_criar_conta = 1
        self.index_depositar = 2
        self.index_extrato = 3
        self.index_historico = 4
        self.index_login = 5
        self.index_menu = 0
        self.index_sacar = 7
        self.index_transferir = 8

        
        self.controle_telas.addWidget(self.stack_menu)
        self.controle_telas.addWidget(self.stack_criar_conta)
        self.controle_telas.addWidget(self.stack_depositar)
        self.controle_telas.addWidget(self.stack_extrato)
        self.controle_telas.addWidget(self.stack_historico)
        self.controle_telas.addWidget(self.stack_login)
        self.controle_telas.addWidget(self.stack_cadastrar_cliente)
        self.controle_telas.addWidget(self.stack_sacar)
        self.controle_telas.addWidget(self.stack_transferir)
        


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.tela_menu.botao_login.clicked.connect(self.teste)

    def teste(self):
        self.mensagem('erro', 'algo deu errado')
        


    def mensagem(self, titulo: str, mensagem: str):
        QMessageBox.information(None, titulo, mensagem)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_busca import TelaBusca
from tela_cadastro import TelaCadastro
from menu import Menu

from cadastros import Cadastro
from pessoa import Pessoa


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.menu_stack = QtWidgets.QMainWindow()
        self.cadastro_stack = QtWidgets.QMainWindow()
        self.busca_stack = QtWidgets.QMainWindow()

        self.menu = Menu()
        self.menu.setupUi(self.menu_stack)

        self.tela_cadastro = TelaCadastro()
        self.tela_cadastro.setupUi(self.cadastro_stack)

        self.tela_busca = TelaBusca()
        self.tela_busca.setupUi(self.busca_stack)

        self.numeroMenu = 0
        self.numeroCadastro = 1
        self.numeroBusca = 2
        self.QtStack.addWidget(self.menu_stack)
        self.QtStack.addWidget(self.cadastro_stack)
        self.QtStack.addWidget(self.busca_stack)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.cadastros = Cadastro()

        self.menu.abrir_busca.clicked.connect(self.abrir_busca)
        self.menu.abrir_cadastro.clicked.connect(self.abrir_cadastro)

        self.tela_cadastro.button_cadastrar.clicked.connect(self.cadastrar)
        self.tela_busca.button_buscar.clicked.connect(self.buscar_pessoas)
        self.tela_busca.button_voltar.clicked.connect(self.abrir_menu)

    def abrir_busca(self):
        self.QtStack.setCurrentIndex(self.numeroBusca)

    def abrir_menu(self):
        self.QtStack.setCurrentIndex(self.numeroMenu)

    def abrir_cadastro(self):
        self.QtStack.setCurrentIndex(self.numeroCadastro)

    def cadastrar(self):
        cpf = self.tela_cadastro.edit_cpf.text()
        nome = self.tela_cadastro.edit_nome.text()
        endereco = self.tela_cadastro.edit_endereco.text()
        nascimento = self.tela_cadastro.edit_nascimento.text()

        if cpf != '' and nome != '' and endereco != '' and nascimento != '':
            pessoa = Pessoa(nome, cpf, endereco, nascimento)

            if self.cadastros.nova_pessoa(pessoa):
                self.message('Sucesso', '{} cadastrado com sucesso'.format(nome))
                self.QtStack.setCurrentIndex(0)
            else:
                self.message('Erro', 'Não foi possivel salva {}'.format(nome))

    def buscar_pessoas(self):
        cadastro, pessoa = self.cadastros.buscar_pessoas(self.tela_busca.edit_cpf.text())
        if cadastro:
            self.tela_busca.name.setText(pessoa.getData["nome"])
            self.tela_busca.endereco.setText(pessoa.getData["endereco"])
            self.tela_busca.nascimento.setText(pessoa.getData["nascimento"])

    def message(self, title: str, body: str):
        QMessageBox.information(None, title, body)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

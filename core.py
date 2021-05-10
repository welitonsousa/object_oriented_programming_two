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

    def mensagem(self, titulo: str, mensagem: str):
        QMessageBox.information(None, titulo, mensagem)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

from main import Ui_Main


class Rotas(Ui_Main):
    def para_login(self):
        self.controle_telas.setCurrentIndex(self.index_login)
    def para_menu(self):
        self.controle_telas.setCurrentIndex(self.index_menu)
    def para_sacar(self):
        self.controle_telas.setCurrentIndex(self.index_sacar)
    def para_extrato(self):
        self.controle_telas.setCurrentIndex(self.index_extrato)
    def para_depositar(self):
        self.controle_telas.setCurrentIndex(self.index_depositar)
    def para_cadastrar_cliente(self):
        self.controle_telas.setCurrentIndex(self.index_cadastrar_cliente)
    def para_criar_conta(self):
        self.controle_telas.setCurrentIndex(self.index_criar_conta)
    def para_historico(self):
        self.controle_telas.setCurrentIndex(self.index_historico)
    def para_transferir(self):
        self.controle_telas.setCurrentIndex(self.index_transferir)
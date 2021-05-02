from PyQt5 import QtCore, QtGui, QtWidgets
from cadastros import Cadastro
from pessoa import Pessoa
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.button_cadastro.setGeometry(QtCore.QRect(300, 270, 75, 23))
        self.button_cadastro.setObjectName("button_cadastro")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(190, 100, 47, 13))
        self.label_name.setObjectName("label_name")
        self.edit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name.setGeometry(QtCore.QRect(250, 100, 181, 20))
        self.edit_name.setObjectName("edit_name")
        self.label_cadastro = QtWidgets.QLabel(self.centralwidget)
        self.label_cadastro.setGeometry(QtCore.QRect(270, 10, 121, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.label_cadastro.sizePolicy().hasHeightForWidth())
        self.label_cadastro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_cadastro.setFont(font)
        self.label_cadastro.setObjectName("label_cadastro")
        self.label_endereco = QtWidgets.QLabel(self.centralwidget)
        self.label_endereco.setGeometry(QtCore.QRect(190, 140, 47, 13))
        self.label_endereco.setObjectName("label_endereco")
        self.edit_endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_endereco.setGeometry(QtCore.QRect(250, 140, 181, 20))
        self.edit_endereco.setObjectName("edit_endereco")
        self.label_cpf = QtWidgets.QLabel(self.centralwidget)
        self.label_cpf.setGeometry(QtCore.QRect(190, 180, 47, 13))
        self.label_cpf.setObjectName("label_cpf")
        self.edit_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_cpf.setGeometry(QtCore.QRect(250, 180, 181, 20))
        self.edit_cpf.setObjectName("edit_cpf")
        self.label_nascimento = QtWidgets.QLabel(self.centralwidget)
        self.label_nascimento.setGeometry(QtCore.QRect(190, 220, 61, 16))
        self.label_nascimento.setObjectName("label_nascimento")
        self.edit_nascimento = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_nascimento.setGeometry(QtCore.QRect(250, 220, 181, 20))
        self.edit_nascimento.setObjectName("edit_nascimento")
        self.label_buscar = QtWidgets.QLabel(self.centralwidget)
        self.label_buscar.setGeometry(QtCore.QRect(280, 350, 121, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.label_buscar.sizePolicy().hasHeightForWidth())
        self.label_buscar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_buscar.setFont(font)
        self.label_buscar.setObjectName("label_buscar")
        self.label_nascimento_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_nascimento_2.setGeometry(QtCore.QRect(100, 580, 61, 16))
        self.label_nascimento_2.setObjectName("label_nascimento_2")
        self.label_name_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_name_2.setGeometry(QtCore.QRect(100, 510, 47, 13))
        self.label_name_2.setObjectName("label_name_2")
        self.edit_nascimento_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_nascimento_2.setEnabled(False)
        self.edit_nascimento_2.setGeometry(QtCore.QRect(160, 580, 181, 20))
        self.edit_nascimento_2.setObjectName("edit_nascimento_2")
        self.label_cpf_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_cpf_2.setGeometry(QtCore.QRect(100, 420, 47, 13))
        self.label_cpf_2.setObjectName("label_cpf_2")
        self.edit_name_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name_2.setEnabled(False)
        self.edit_name_2.setGeometry(QtCore.QRect(160, 510, 181, 20))
        self.edit_name_2.setObjectName("edit_name_2")
        self.label_endereco_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_endereco_2.setGeometry(QtCore.QRect(100, 550, 47, 13))
        self.label_endereco_2.setObjectName("label_endereco_2")
        self.edit_cpf_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_cpf_2.setGeometry(QtCore.QRect(210, 420, 131, 20))
        self.edit_cpf_2.setObjectName("edit_cpf_2")
        self.edit_endereco_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_endereco_2.setEnabled(False)
        self.edit_endereco_2.setGeometry(QtCore.QRect(160, 550, 181, 20))
        self.edit_endereco_2.setObjectName("edit_endereco_2")
        self.button_cadastro_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_cadastro_2.setGeometry(QtCore.QRect(350, 420, 75, 23))
        self.button_cadastro_2.setObjectName("button_cadastro_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.button_cadastro.clicked.connect(self.nova_pessoa)
        self.button_cadastro_2.clicked.connect(self.buscar_pessoas)


    def nova_pessoa(self):
        cpf = self.edit_cpf.text()
        nome = self.edit_name.text()
        endereco = self.edit_endereco.text()
        nascimento = self.edit_nascimento.text()

        pessoa = Pessoa(nome, cpf, endereco, nascimento)
        
        if Cadastro.nova_pessoa(pessoa):
            self.message('Sucesso', '{} cadastrado com sucesso'.format(nome))
            self.clean()
        else:
            self.message('Erro', 'Não foi possivel salva {}'.format(nome))
            
    def message(self, title: str, body: str):
        QMessageBox.information(None, title, body)

    def clean(self):
        self.edit_cpf.setText('')
        self.edit_name.setText('')
        self.edit_endereco.setText('')
        self.edit_nascimento.setText('')

    def buscar_pessoas(self):
        cadastro, pessoa = Cadastro.buscar_pessoas(self.edit_cpf_2.text())
        if cadastro:
            self.edit_name_2.setText(pessoa.getData()["nome"])
            self.edit_endereco_2.setText(pessoa.getData()["endereco"])
            self.edit_nascimento_2.setText(pessoa.getData()["nascimento"])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_cadastro.setText(_translate("MainWindow", "Cadastrar"))
        self.label_name.setText(_translate("MainWindow", "Nome"))
        self.label_cadastro.setText(_translate("MainWindow", "Cadastro"))
        self.label_endereco.setText(_translate("MainWindow", "Endereco"))
        self.label_cpf.setText(_translate("MainWindow", "CPF"))
        self.label_nascimento.setText(_translate("MainWindow", "Nascimento"))
        self.label_buscar.setText(_translate("MainWindow", "Buscar"))
        self.label_nascimento_2.setText(_translate("MainWindow", "Nascimento"))
        self.label_name_2.setText(_translate("MainWindow", "Nome"))
        self.label_cpf_2.setText(_translate("MainWindow", "CPF"))
        self.label_endereco_2.setText(_translate("MainWindow", "Endereco"))
        self.button_cadastro_2.setText(_translate("MainWindow", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

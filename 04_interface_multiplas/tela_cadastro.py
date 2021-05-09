from PyQt5 import QtCore, QtGui, QtWidgets


class TelaCadastro(object):
    def setupUi(self, Besteira):
        Besteira.setObjectName("Besteira")
        Besteira.resize(641, 436)
        self.centralwidget = QtWidgets.QWidget(Besteira)
        self.centralwidget.setObjectName("centralwidget")
        self.button_cadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.button_cadastrar.setGeometry(QtCore.QRect(270, 280, 75, 23))
        icon = QtGui.QIcon.fromTheme("aa")
        self.button_cadastrar.setIcon(icon)
        self.button_cadastrar.setObjectName("button_cadastrar")
        self.edit_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_cpf.setGeometry(QtCore.QRect(220, 110, 171, 21))
        self.edit_cpf.setAccessibleDescription("")
        self.edit_cpf.setInputMask("")
        self.edit_cpf.setText("")
        self.edit_cpf.setClearButtonEnabled(True)
        self.edit_cpf.setObjectName("edit_cpf")
        self.edit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_nome.setGeometry(QtCore.QRect(220, 150, 171, 21))
        self.edit_nome.setAccessibleDescription("")
        self.edit_nome.setInputMask("")
        self.edit_nome.setText("")
        self.edit_nome.setClearButtonEnabled(True)
        self.edit_nome.setObjectName("edit_nome")
        self.edit_endereco = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_endereco.setGeometry(QtCore.QRect(220, 190, 171, 21))
        self.edit_endereco.setAccessibleDescription("")
        self.edit_endereco.setInputMask("")
        self.edit_endereco.setText("")
        self.edit_endereco.setClearButtonEnabled(True)
        self.edit_endereco.setObjectName("edit_endereco")
        self.edit_nascimento = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_nascimento.setGeometry(QtCore.QRect(220, 230, 171, 21))
        self.edit_nascimento.setAccessibleDescription("")
        self.edit_nascimento.setInputMask("")
        self.edit_nascimento.setText("")
        self.edit_nascimento.setClearButtonEnabled(True)
        self.edit_nascimento.setObjectName("edit_nascimento")
        Besteira.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Besteira)
        self.statusbar.setObjectName("statusbar")
        Besteira.setStatusBar(self.statusbar)

        self.retranslateUi(Besteira)
        QtCore.QMetaObject.connectSlotsByName(Besteira)

    def retranslateUi(self, Besteira):
        _translate = QtCore.QCoreApplication.translate
        Besteira.setWindowTitle(_translate("Besteira", "MainWindow"))
        self.button_cadastrar.setText(_translate("Besteira", "Cadastrar"))
        self.edit_cpf.setPlaceholderText(_translate("Besteira", "CPF"))
        self.edit_nome.setPlaceholderText(_translate("Besteira", "Nome"))
        self.edit_endereco.setPlaceholderText(_translate("Besteira", "Endereço"))
        self.edit_nascimento.setPlaceholderText(_translate("Besteira", "Nascimento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Besteira = QtWidgets.QMainWindow()
    ui = TelaCadastro()
    ui.setupUi(Besteira)
    Besteira.show()
    sys.exit(app.exec_())

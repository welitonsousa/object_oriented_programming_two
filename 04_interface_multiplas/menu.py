from PyQt5 import QtCore, QtGui, QtWidgets


class Menu(object):
    def setupUi(self, Besteira):
        Besteira.setObjectName("Besteira")
        Besteira.resize(640, 447)
        self.centralwidget = QtWidgets.QWidget(Besteira)
        self.centralwidget.setObjectName("centralwidget")
        self.abrir_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.abrir_cadastro.setGeometry(QtCore.QRect(210, 210, 75, 23))
        self.abrir_cadastro.setObjectName("abrir_cadastro")
        self.abrir_busca = QtWidgets.QPushButton(self.centralwidget)
        self.abrir_busca.setGeometry(QtCore.QRect(340, 210, 75, 23))
        self.abrir_busca.setObjectName("abrir_busca")
        Besteira.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Besteira)
        self.statusbar.setObjectName("statusbar")
        Besteira.setStatusBar(self.statusbar)

        self.retranslateUi(Besteira)
        QtCore.QMetaObject.connectSlotsByName(Besteira)

    def retranslateUi(self, Besteira):
        _translate = QtCore.QCoreApplication.translate
        Besteira.setWindowTitle(_translate("Besteira", "MainWindow"))
        self.abrir_cadastro.setText(_translate("Besteira", "Cadastrar"))
        self.abrir_busca.setText(_translate("Besteira", "Buscar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Besteira = QtWidgets.QMainWindow()
    ui = Menu()
    ui.setupUi(Besteira)
    Besteira.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSacar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class TelaSacar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_sacar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sacar.setGeometry(QtCore.QRect(380, 70, 75, 23))
        self.botao_sacar.setObjectName("botao_sacar")
        self.edit_valor = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_valor.setGeometry(QtCore.QRect(180, 70, 181, 20))
        self.edit_valor.setText("")
        self.edit_valor.setReadOnly(False)
        self.edit_valor.setClearButtonEnabled(True)
        self.edit_valor.setObjectName("edit_valor")
        self.botao_menu = QtWidgets.QPushButton(self.centralwidget)
        self.botao_menu.setGeometry(QtCore.QRect(510, 340, 86, 26))
        self.botao_menu.setObjectName("botao_menu")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_sacar.setText(_translate("MainWindow", "Sacar"))
        self.edit_valor.setPlaceholderText(_translate("MainWindow", "VALOR"))
        self.botao_menu.setText(_translate("MainWindow", "Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TelaSacar()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_historico.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.botao_menu = QtWidgets.QPushButton(self.centralwidget)
        self.botao_menu.setGeometry(QtCore.QRect(480, 380, 86, 26))
        self.botao_menu.setObjectName("botao_menu")
        self.edit_descricao = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_descricao.setEnabled(False)
        self.edit_descricao.setGeometry(QtCore.QRect(130, 170, 381, 20))
        self.edit_descricao.setReadOnly(True)
        self.edit_descricao.setObjectName("edit_descricao")
        self.edit_data = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_data.setEnabled(False)
        self.edit_data.setGeometry(QtCore.QRect(220, 120, 181, 20))
        self.edit_data.setReadOnly(False)
        self.edit_data.setObjectName("edit_data")
        self.botao_anterior = QtWidgets.QPushButton(self.centralwidget)
        self.botao_anterior.setGeometry(QtCore.QRect(280, 210, 86, 26))
        self.botao_anterior.setObjectName("botao_anterior")
        self.label_historico = QtWidgets.QLabel(self.centralwidget)
        self.label_historico.setGeometry(QtCore.QRect(260, 40, 181, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(19)
        sizePolicy.setHeightForWidth(self.label_historico.sizePolicy().hasHeightForWidth())
        self.label_historico.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_historico.setFont(font)
        self.label_historico.setObjectName("label_historico")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_menu.setText(_translate("MainWindow", "Menu"))
        self.botao_anterior.setText(_translate("MainWindow", "Anterior"))
        self.label_historico.setText(_translate("MainWindow", "Histórico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

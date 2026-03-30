# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window -> setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

import sys

from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Minha Janela")

botao1 = QPushButton("Texto do botão")
botao1.setStyleSheet("font-size: 40px")

botao2 = QPushButton("Botão 2")
botao2.setStyleSheet("font-size: 80px")

botao3 = QPushButton("Botão 3")
botao3.setStyleSheet("font-size: 60px")


layout = QGridLayout()
central_widget.setLayout(layout)  # defini o layout para o widget central

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


def slot_example(status_bar):
    status_bar.showMessage("O slot foi executado")


# Status bar
status_bar = window.statusBar()
status_bar.showMessage("Motrar Mensagem na barra")

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu("Primeiro Menu")
primeira_acao = primeiro_menu.addAction("Primeira Ação")
primeira_acao.triggered.connect(lambda: slot_example(status_bar))
# Quando essa ação for clicada o slot_example será executado


window.show()
app.exec()  # loop da aplicação

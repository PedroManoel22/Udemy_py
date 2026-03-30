# O básico sobre Signal e Slots (eventos e documentação)

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QWidget,
)

app = QApplication(sys.argv)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.botao1 = QPushButton("Texto do botão")
        self.botao1.setStyleSheet("font-size: 40px")

        self.botao1.clicked.connect(terceiro_slot(segunda_acao))

        self.botao2 = QPushButton("Botão 2")
        self.botao2.setStyleSheet("font-size: 80px")

        self.botao3 = QPushButton("Botão 3")
        self.botao3.setStyleSheet("font-size: 60px")

        self.central_widget = QWidget()

        self.setCentralWidget(self.central_widget)
        self.setWindowTitle("Minha Janela")

        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(
            self.grid_layout
        )  # defini o grid_layout para o widget central

        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)


self = MyWindow()


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage("O meu slot foi executado")

    return inner


@Slot()
def outro_slot(checked):  # já é padrão vim o checked
    print("Está marcado?", checked)


@Slot()
def terceiro_slot(acao):  # é a mesma coisa que foi feito no triggered da primeira ação
    """Toda vez que passarmos o mouse encima da segunda ação retornamos o checked"""

    def inner():
        outro_slot(acao.isChecked())

    return inner


# Status bar
status_bar = self.statusBar()
status_bar.showMessage("Motrar Mensagem na barra")

# menuBar
menu = self.menuBar()
primeiro_menu = menu.addMenu("Primeiro Menu")
primeira_acao = primeiro_menu.addAction("Primeira Ação")
primeira_acao.triggered.connect(slot_example(status_bar))
# Quando essa ação for clicada o slot_example será executado

segunda_acao = primeiro_menu.addAction("Segunda Ação")
segunda_acao.setCheckable(True)  # muda ação para "liga-desliga"
segunda_acao.toggled.connect(outro_slot)
segunda_acao.hovered.connect(terceiro_slot(segunda_acao))


self.show()
app.exec()  # loop da aplicação

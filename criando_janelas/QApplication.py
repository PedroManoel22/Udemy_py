# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> um botão
# PySide6.Qtwidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton("Texto do botão")
botao.setStyleSheet("font-size: 40px")
botao.show()  # Adicionar o widget na hierarquia e exibe a janela

app.exec()  # loop da aplicação

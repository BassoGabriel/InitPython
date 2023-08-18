
# PyQt5 - Criando Interfaces gráficas com Python
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QSize

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.x = 640
        self.y = 480
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Hello Word - Processamento Digital de Imagens")

        self.texto = QLabel("Hello Word", self)
        self.texto.adjustSize()
        self.texto.setAlignment(QtCore.Qt.AlignCenter)
        self.texto.move(320, 240)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
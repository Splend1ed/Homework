from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Calculator')
        # self.setWindowIcoN()
        self.setMinimumSize(350, 355)
        self.setSizeIncrement(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setFamily("URW Gothic")
        font.setItalic(True)
        self.setFont(font)
        self.setTabletTracking(False)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.setStyleSheet("background-color: rgb(49,49,49);""color: rgb(238, 238, 236);")
        self.screen = QtWidgets.QLabel(self)
        self.screen.setStyleSheet("background-color: rgb(52, 52, 52)")
        self.screen.setMinimumSize(QtCore.QSize(350, 60))
        self.screen.setGeometry(QtCore.QRect(0, 125, 0, 0))
        self.gridLayout.addWidget(self.screen, 0, 0, 1, 6)
        self.b1 = Buttons(12, 309, '0', 52, 35, self)
        self.b2 = Buttons(67, 309, ',', 52, 35, self)
        self.b3 = Buttons(122, 309, '%', 52, 35, self)
        self.b4 = Buttons(177, 309, '+', 52, 35, self)
        self.b5 = Buttons(232, 309, '=', 107, 35, self)
        self.b6 = Buttons(12, 271, '1', 52, 35, self)
        self.b7 = Buttons(67, 271, '2', 52, 35, self)
        self.b8 = Buttons(122, 271, '3', 52, 35, self)
        self.b9 = Buttons(177, 271, '-', 52, 35, self)
        self.b10 = Buttons(232, 271, 'x\u00B2', 52, 35, self)
        self.b11 = Buttons(287, 271, '\u221A', 52, 35, self)
        self.b12 = Buttons(12, 233, '4', 52, 35, self)
        self.b13 = Buttons(67, 233, '5', 52, 35, self)
        self.b14 = Buttons(122, 233, '6', 52, 35, self)
        self.b15 = Buttons(177, 233, '\u00D7', 52, 35, self)
        self.b16 = Buttons(232, 233, '(', 52, 35, self)
        self.b17 = Buttons(287, 233, ')', 52, 35, self)
        self.b18 = Buttons(12, 195, '7', 52, 35, self)
        self.b19 = Buttons(67, 195, '8', 52, 35, self)
        self.b20 = Buttons(122, 195, '9', 52, 35, self)
        self.b21 = Buttons(177, 195, '\u00F7', 52, 35, self)
        self.b22 = Buttons(232, 195, '\u21B5', 52, 35, self)
        self.b23 = Buttons(287, 195, 'C', 52, 35, self)



class Buttons:
    def __init__(self, move1: int, move2: int, set_text: str, set_size1: int, set_size2: int, window: 'Window'):
        self.window = window
        self.button = QtWidgets.QPushButton(self.window)
        self.button.move(move1, move2)
        self.button.setText(set_text)
        self.button.setFixedSize(set_size1, set_size2)
        # self.button.setStyleSheet('background-color: rgb(72,72,72)')
        self.button.clicked.connect(self.add_symbol)

    def add_symbol(self):
        self.window.screen.setText(self.button.text())
        self.window.screen.move(50, 50)
        self.window.screen.setFixedSize(60, 60)


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()


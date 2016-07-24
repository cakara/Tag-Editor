from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget(self)

        self.menuBar = Menu(self)
        self.fileDialog = TabWidget(self.centralWidget)
        self.tv = TreeView(self.centralWidget)
        self.consol = Consol(self.centralWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.tv)
        self.verticalLayout.addWidget(self.consol)

        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.addWidget(self.fileDialog)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.setCentralWidget(self.centralWidget)
        self.setMenuBar(self.menuBar)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

from PyQt5.QtWidgets import *
import sys


class Menu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.menu = QMenu(self)
        self.menu.setTitle("Dosya")
        self.addMenu(self.menu)
        self.action1 = QAction(self.menu)
        self.action1.setText("Aç")
        self.menu.addAction(self.action1)
        self.menu.addSeparator()
        self.action2 = QAction(self.menu)
        self.action2.setText("Kaydet")
        self.menu.addAction(self.action2)
        self.action3 = QAction(self.menu)
        self.action3.setText("Farklı Kaydet")
        self.menu.addAction(self.action3)

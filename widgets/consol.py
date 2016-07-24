from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
try:
    from core import sql
except ImportError:
    import sql

def completer(list):
    comp = QCompleter(list)
    comp.setCaseSensitivity(Qt.CaseInsensitive)
    return comp

class Consol(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setSizePolicy(sizePolicy)
        
        self.layout = QFormLayout(self)

        self.title = QLineEdit(self)
        self.artist = QLineEdit(self)
        self.album = QLineEdit(self)
        self.genre = QLineEdit(self)
        self.year = QLineEdit(self)
        self.year.setValidator(QIntValidator())
        self.year.setMaxLength(4)
        
        self.layout.addRow("<font size='4'>Title</font>", self.title)
        self.layout.addRow("<font size='4'>Artist</font>", self.artist)
        self.layout.addRow("<font size='4'>Album</font>", self.album)
        self.layout.addRow("<font size='4'>Genre</font>", self.genre)
        self.layout.addRow("<font size='4'>Year</font>", self.year)

        self.show()
        self.setCompleters()
        
    def setCompleters(self):
        db = sql.ReaderDb()
        self.artist.setCompleter(completer(db.artists()))
        self.album.setCompleter(completer(db.albums()))
        self.genre.setCompleter(completer(db.genres()))
        db.close()

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pen = Consol()
    uygulama.exec_()

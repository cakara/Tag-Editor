from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sys

def createConnection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName("tagarchive.db")
    db.open()

class TreeView(QTreeView):
    sel = pyqtSignal(QSqlRecord)
    def __init__(self,parent=None):
        super().__init__(parent)
        createConnection()
        self.model = QSqlQueryModel()
        self.model.setQuery('select artist, album, genre from files')
        #for column, name in enumerate(headers):
            #model.setHeaderData(column, Qt.Horizontal, name)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        
        self.setSizePolicy(sizePolicy) 
        self.setModel(self.model)     
        self.setRootIsDecorated(False)
        self.setAlternatingRowColors(True)
        self.show()

        #self.horizontalLayout = QHBoxLayout(self)
        #self.horizontalLayout.addWidget(self.view)

        self.selectionModel().currentRowChanged.connect(self.fonk)

    def fonk(self,x,y):
        if not x:
            x = y
        ri = x.row()
        record = self.model.record(ri)
        self.sel.emit(record)


if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    #createConnection() 
    pen = TreeView()
    #pen.show()
    uygulama.exec_()


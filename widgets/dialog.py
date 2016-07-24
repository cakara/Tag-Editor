from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

def TabWidget(parent=None):
    tabWidget = QTabWidget(parent)
    sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
    tabWidget.setSizePolicy(sizePolicy)
    tabWidget.resize(200, 550)
    tabWidget.setMinimumSize(200, 0)
    
    tabWidget.addTab(fileSystemTab(), "File System")
    tabWidget.addTab(allFilesTab(), "All Files")
    tabWidget.show()
    return tabWidget

def fileSystemTab():    
    model = QFileSystemModel()
    model.setRootPath("")
    model.setFilter(QDir.AllDirs | QDir.NoDotAndDotDot)
    model.setNameFilters(["*.mp3"])
    model.setNameFilterDisables(False)

    tab = NewTab(model)
    return tab

def allFilesTab():
    def createItem(name,icon):
        new_item = QStandardItem()
        new_item.setText(name)
        #new_item.setIcon(icon)
        new_item.setEditable(False)
        return new_item  
    items = [("a",["b","c","d"]),
             ("b",["t","i"]),
             ("c",[])]
    model = QStandardItemModel()
    for item, subitems in items:
        new_item = createItem(item, "icon")
        for row, child in enumerate(subitems):
            new_item.setChild(row, createItem(child, "icon2")) 
        model.appendRow(new_item)

    tab = NewTab(model)
    return tab
    
class NewTab(QWidget):
    def __init__(self, model, parent=None):
        super().__init__(parent)
        
        self.treeView = QTreeView()
        self.treeView.setModel(model)
        self.model = self.treeView.model()
        
        self.selectionModel = self.treeView.selectionModel()
        self.selectionModel.selectionChanged.connect(self.selection)
        
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.setHeaderHidden(True)
        
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.addWidget(self.treeView)

    def selection(self, selection):
        selection_index = selection.indexes()[0]
        try:
            path = self.model.filePath(selection_index)
        except AttributeError:
            item = self.model.itemFromIndex(selection_index)
            parent = item.parent()

class YeniPencere(QWidget):
    def __init__(self):
        super().__init__()
        w = TabWidget(self)
        w.show()    

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = YeniPencere()
    pencere.show()

    uygulama.exec_()

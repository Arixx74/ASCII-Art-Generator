import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QAction, QFileSystemModel, QTreeView, QFileDialog
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets

class DIR_WINDOW(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "Convex"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 400
        self.icon_name = "NIT-Silchar-Logo.png"
        self.path = ''
        self.initApp()

    def initApp(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.model = QFileSystemModel()
        self.model.setRootPath("C:")
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        
        self.tree.setWindowTitle("Explorer")
        self.tree.resize(640, 480)
        self.tree.move(20, 20)
        self.tree.clicked.connect(self.selectPath)
        
        self.select_button = QPushButton("Select", self)
        self.select_button.setToolTip("Click to select image")
        self.select_button.setMinimumHeight(40)
        self.select_button.clicked.connect(self.obtainPath)
        
        #windowLayout = QVBoxLayout()
        #windowLayout.addWidget(self.tree)
        #windowLayout.addWidget(select_button)
        #self.setLayout(windowLayout)
        
        self.show()
    
    def selectPath(self, index):
        self.path = self.sender().model().filePath(index)
        
    def obtainPath(self):
        print("obtain path:" + self.path)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = DIR_WINDOW()
    sys.exit(App.exec())
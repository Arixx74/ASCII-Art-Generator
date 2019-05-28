
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets

class WINDOW(QtWidgets.QWidget):
    def __init__(self, title = "Convex", top = 100, left = 100, width = 500, height = 200, icon_name = None):
        super().__init__()
        
        self.title = title
        self.top = top
        self.left = left
        self.width = width
        self.height = height
        self.icon_name = icon_name
        self.initApp()

    def initApp(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = WINDOW(icon_name="NIT-Silchar-Logo.png", width=1600)
    sys.exit(App.exec())
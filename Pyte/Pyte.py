print("hello world")
#from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout, QLabel, QAction
#import sys
#from PyQt5 import QtGui
#from PyQt5 import QtCore, QtWidgets
#from PIL import Image
##from interface import Browse

#class Window(QWidget):
#        def __init__(self):
#            super().__init__()

#            self.title = "Convex"
#            self.top = 100
#            self.left = 100
#            self.width = 500
#            self.height = 200
#            self.icon_name = "NIT-Silchar-Logo.png"
#            self.InitWindow()

#        def InitWindow(self):
#            self.setWindowIcon(QtGui.QIcon(self.icon_name))
#            self.setWindowTitle(self.title)
#            self.setGeometry(self.left, self.top, self.width, self.height)
            
#            self.CreateInternalLayout()
#            self.CreateExternalLayout()

#            vbox = QVBoxLayout()
#            title = QLabel("Convex")
#            title.setFont(QtGui.QFont("Sanserif", 20))
#            title.setStyleSheet("color:blue")
            
#            vbox.addWidget(title)
#            vbox.addWidget(self.internal_group_box)
#            vbox.addWidget(self.external_group_box)
#            """
#            flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
#            self.setWindowFlags(flags)
#            size_grip = QtWidgets.QSizeGrip(self)
#            vbox.addWidget(size_grip)
#            """
#            self.setLayout(vbox)

#            self.show()
            
#        def CreateInternalLayout(self):
#            self.internal_group_box = QGroupBox()
#            vbox = QVBoxLayout()

#            input_box = QGroupBox()
#            hboxlayout = QHBoxLayout()
            
#            #SELECT LINE EDIT1
#            self.line_edit_select = QtWidgets.QLineEdit(self)
#            hboxlayout.addWidget(self.line_edit_select)
#            self.line_edit_select.setFont(QtGui.QFont("Sanserif", 15))
#            self.line_edit_select.returnPressed.connect(self.SetPix)

#            #SELECT BUTTON
#            button_select = QPushButton("  Select Image")
#            button_select.setIcon(QtGui.QIcon("select.png"))
#            button_select.setIconSize(QtCore.QSize(20, 20))
#            button_select.setToolTip("Select an image to convert to ASCII art")
#            button_select.setMinimumHeight(40)
#            button_select.setMinimumWidth(150)
#            hboxlayout.addWidget(button_select)
#            button_select.clicked.connect(self.SelectSignal)
#            """
#            action_select = QAction()
#            action_select.setShortcut("Ctrl+E")
#            action_select.triggered.connect(self.SelectSignal)
#            button_select.addAction(action_select)
#            """
#            input_box.setLayout(hboxlayout)

#            vbox.addWidget(input_box)

#            #IMAGE

#            self.image_label = QLabel(self)
#            #pixmap = QtGui.QPixmap(self.icon_name)
#            #image_label.setPixmap(pixmap)
#            vbox.addWidget(self.image_label)



#            self.internal_group_box.setLayout(vbox)

#        def CreateExternalLayout(self):
#            self.external_group_box = QGroupBox("Select an image and click Convert")
#            hboxlayout = QHBoxLayout()
            
#            #CONVERT BUTTON
#            button_convert = QPushButton("  Convert", self)
#            #button.move(50, 50)
#            button_convert.setIcon(QtGui.QIcon("convert.png"))
#            button_convert.setIconSize(QtCore.QSize(20, 20))
#            button_convert.setToolTip("Click to convert image to ASCII art")
#            button_convert.setMinimumHeight(40)
#            hboxlayout.addWidget(button_convert)
#            button_convert.clicked.connect(self.ConvertSignal)

#            #SAVE BUTTON
#            button_save = QPushButton("  Save", self)
#            button_save.setIcon(QtGui.QIcon("save.png"))
#            button_save.setIconSize(QtCore.QSize(20, 20))
#            button_save.setToolTip("Click to save the ASCII art")
#            button_save.setMinimumHeight(40)
#            hboxlayout.addWidget(button_save)
#            button_save.clicked.connect(self.SaveSignal)
            
#            #CLOSE BUTTON
#            button_close = QPushButton("  Exit", self)
#            #button_close.setGeometry(QtCore.QRect(100, 220, 111, 50))
#            button_close.setIcon(QtGui.QIcon("exit.png"))
#            button_close.setIconSize(QtCore.QSize(20, 20))
#            button_close.setToolTip("Click to close the application")
#            button_close.setMinimumHeight(40)
#            hboxlayout.addWidget(button_close)
#            button_close.clicked.connect(self.CloseSignal)

#            self.external_group_box.setLayout(hboxlayout)

#        def ConvertSignal(self):
#            print("Convert image")

#        def CloseSignal(self):
#            print("Closed successfully")
#            self.close()
#            #sys.exit()

#        def SelectSignal(self):
#            browse = Browse()

#            print("Select image")

#        def SaveSignal(self):
#            print("Save image")

#        def SetPix(self):
#            #img = Image.open(self.line_edit_select.text())
#            pixmap = QtGui.QPixmap(self.line_edit_select.text())
#            self.image_label.setPixmap(pixmap)

#if __name__ == "__main__":
#    App = QApplication(sys.argv)
#    window = Window()
#    sys.exit(App.exec())

import sys
from sec_window import SEC_WINDOW
import ASCII_Art as asc
from PyQt5 import QtCore, QtGui, QtWidgets

class MAIN_WINDOW(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #INITIAL VALUES:
        self.title = "ASCII Art Generator"
        self.top = 100
        self.left = 500
        self.width = 940
        self.height = 140
        self.icon_name = "NIT-Silchar-Logo.png"
        #self.defaultImgPath = "C:/Users/Arif Ahmed/Pictures/Arts/7cxunfcbuzl11.jpg"
        #self.defaultImgPathLabel = "Please select an image.."
        self.defaultImgPath = 'C:\\Users\\Arif Ahmed\\Pictures'
        self.pixmap_resized = QtGui.QPixmap('')
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.setWindowFlags(flags)

        #SELECT LINE EDIT
        self.line_edit_select = QtWidgets.QLineEdit(self)
        self.line_edit_select.setFont(QtGui.QFont("Sanserif", 9))
        self.line_edit_select.setText("Please select an image..")
        self.line_edit_select.setMinimumHeight(40)
        self.line_edit_select.setMinimumWidth(560)
        self.line_edit_select.move(20, 20)
        self.line_edit_select.returnPressed.connect(self.SetPix)

        #SELECT BUTTON
        self.button_select = QtWidgets.QPushButton("  Select", self)
        self.button_select.setIcon(QtGui.QIcon("select3.png"))
        self.button_select.setIconSize(QtCore.QSize(20, 20))
        self.button_select.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.button_select.setToolTip("Select an image to convert to ASCII art")
        self.button_select.setMinimumHeight(40)
        self.button_select.setMinimumWidth(150)
        self.button_select.move(600, 20)
        self.button_select.clicked.connect(self.BrowseImage)
        
        #IMAGE
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.move(20, 80)
        self.image_label.setMinimumHeight(720)
        self.image_label.setMinimumWidth(900)
        #self.image_label.setGeometry(QtCore.QRect(20, 80, 490, 880))

        #CONVERT BUTTON
        self.button_convert = QtWidgets.QPushButton("  Convert", self)
        self.button_convert.setIcon(QtGui.QIcon("convert.png"))
        self.button_convert.setIconSize(QtCore.QSize(20, 20))
        self.button_convert.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.button_convert.setToolTip("Click to convert image to ASCII art")
        self.button_convert.move(770, 20)
        self.button_convert.setMinimumHeight(40)
        self.button_convert.setMinimumWidth(150)
        self.button_convert.clicked.connect(self.ConvertSignal)
        
        #CLOSE BUTTON
        #self.button_close = QtWidgets.QPushButton("  Close", self)
        #self.button_close.setIcon(QtGui.QIcon("exit.png"))
        #self.button_close.setIconSize(QtCore.QSize(20, 20))
        #self.button_close.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        #self.button_close.setToolTip("Click to close the application")
        #self.button_close.move(20, 20)
        #self.button_close.setMinimumHeight(40)
        #self.button_close.setMinimumWidth(150)
        #self.button_close.clicked.connect(self.CloseSignal)

        self.show()

    def ConvertSignal(self):
        art = ''
        self.secWindow = SEC_WINDOW(art, self.defaultImgPath)
        if not self.pixmap_resized.isNull():
            art = asc.main(self.defaultImgPath, self.secWindow.defaultRes, self.secWindow.mode, self.secWindow.defaultScale)
        else:
            art = 'Image not found!'
        self.secWindow = SEC_WINDOW(art, self.defaultImgPath)
        #print(art)
        #self.secWindow.resize(QtCore.QSize(1920, 1080))
        self.secWindow.show()

        print("Convert image")
    
    #def CloseSignal(self):
    #    print("Closed successfully")
    #    self.close()
    #    #sys.exit()
    #
    #def SelectSignal(self):
    #    browse = interface.Browse()
    #    browse.show()
    #    print("Select image")
    
    #def SaveSignal(self):
    #    print("Save image")
    
    def SetPix(self):
        #img = Image.open(self.line_edit_select.text())
        imgPath = self.line_edit_select.text()
        pixmap = QtGui.QPixmap(imgPath)
        if not pixmap.isNull():
            self.setGeometry(self.left, self.top, self.width, 900)
            self.defaultImgPath = imgPath
        self.pixmap_resized = pixmap.scaled(900, 720, QtCore.Qt.KeepAspectRatio)
        #pixmap_resized = pixmap.scaledToWidth(900)
        self.image_label.setPixmap(self.pixmap_resized)
        
    def BrowseImage(self):
        imgFile = QtWidgets.QFileDialog.getOpenFileName(self,'Select', self.defaultImgPath, 'Image files (*.jpg *.png)')
        imgPath = imgFile[0]
        self.line_edit_select.setText(imgPath)
        self.defaultImgPath = imgPath
        
        pixmap = QtGui.QPixmap(self.defaultImgPath)
        if not pixmap.isNull():
            self.setGeometry(self.left, self.top, self.width, 900)
        self.pixmap_resized = pixmap.scaled(900, 720, QtCore.Qt.KeepAspectRatio)
        #pixmap_resized = pixmap.scaledToWidth(900)
        self.image_label.setPixmap(self.pixmap_resized)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MAIN_WINDOW()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
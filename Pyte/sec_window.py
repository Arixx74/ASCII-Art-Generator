
import sys
import ASCII_Art as asc
from PyQt5 import QtCore, QtGui, QtWidgets

class SEC_WINDOW(QtWidgets.QMainWindow):
    def __init__(self, art, defaultImgPath, title='ASCII Art'):
        super().__init__()

        """
        self.mode = True
        """
        self.mode = False
        #"""
        self.defaultImgPath = defaultImgPath
        self.defaultRes = 300
        self.defaultScale = 0.43
        self.defaultFontSize = 6
        self.art = art
        self.title = title
        self.top = 0
        self.left = 0
        self.width = 1920
        self.height = 1080
        self.icon_name = "NIT-Silchar-Logo.png"
        self.defaultSavePath = "C:\\Users\\Arif Ahmed\\Desktop"
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)

        #PLAIN TEXT
        self.art_label = QtWidgets.QPlainTextEdit(self)
        fixed_font = QtGui.QFont("monospace", 10)
        fixed_font.setStyleHint(QtGui.QFont.TypeWriter)
        self.art_label.setFont(fixed_font)
        self.art_label.move(20, 80)
        self.art_label.setMinimumHeight(970)
        self.art_label.setMinimumWidth(1880)
        self.art_label.insertPlainText(self.art)
        #vbox = QtWidgets.QVBoxLayout()
        #vbox.addWidget(art_label)
        
        #SCALE LABEL
        self.scale_label = QtWidgets.QLabel(self)
        self.scale_label.move(865, 20)
        self.scale_label.resize(QtCore.QSize(100, 40))
        self.scale_label.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.scale_label.setText("Aspect-Ratio")
        
        #SCALE LINE EDIT
        self.line_edit_scale = QtWidgets.QLineEdit(self)
        self.line_edit_scale.setFont(QtGui.QFont("Sanserif", 9))
        self.line_edit_scale.setText(str(self.defaultScale))
        self.line_edit_scale.resize(QtCore.QSize(60, 40))
        self.line_edit_scale.move(1045, 20)
        self.line_edit_scale.returnPressed.connect(self.SetScale)

        #SCALE_UP BUTTON
        self.button_scale_up = QtWidgets.QPushButton(self)
        self.button_scale_up.setIcon(QtGui.QIcon("up.png"))
        self.button_scale_up.setIconSize(QtCore.QSize(20, 20))
        self.button_scale_up.setToolTip("Click to increase aspect ratio")
        self.button_scale_up.move(1125, 20)
        self.button_scale_up.resize(QtCore.QSize(40, 40))
        self.button_scale_up.clicked.connect(self.ScaleUpSignal)
        
        #SCALE_DOWN BUTTON
        self.button_scale_down = QtWidgets.QPushButton(self)
        self.button_scale_down.setIcon(QtGui.QIcon("down.png"))
        self.button_scale_down.setIconSize(QtCore.QSize(20, 20))
        self.button_scale_down.setToolTip("Click to increase aspect ratio")
        self.button_scale_down.move(985, 20)
        self.button_scale_down.resize(QtCore.QSize(40, 40))
        self.button_scale_down.clicked.connect(self.ScaleDownSignal)


        #MODE BUTTON
        self.mode_button = QtWidgets.QPushButton("High" if self.mode else "Low", self)
        self.mode_button.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.mode_button.setToolTip("Click to change character variance")
        self.mode_button.move(1185, 20)
        self.mode_button.resize(QtCore.QSize(60, 40))
        self.mode_button.clicked.connect(self.ToggleMode)

        #RES LABEL
        self.res_label = QtWidgets.QLabel(self)
        self.res_label.move(1265, 20)
        self.res_label.resize(QtCore.QSize(85, 40))
        self.res_label.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.res_label.setText("Resolution")

        #RES LINE EDIT
        self.line_edit_res = QtWidgets.QLineEdit(self)
        self.line_edit_res.setFont(QtGui.QFont("Sanserif", 9))
        self.line_edit_res.setText(str(self.defaultRes))
        self.line_edit_res.resize(QtCore.QSize(60, 40))
        self.line_edit_res.move(1430, 20)
        self.line_edit_res.returnPressed.connect(self.SetRes)

        #RES_UP BUTTON
        self.button_res_up = QtWidgets.QPushButton(self)
        self.button_res_up.setIcon(QtGui.QIcon("up.png"))
        self.button_res_up.setIconSize(QtCore.QSize(20, 20))
        self.button_res_up.setToolTip("Click to increase number of characters")
        self.button_res_up.move(1510, 20)
        self.button_res_up.resize(QtCore.QSize(40, 40))
        self.button_res_up.clicked.connect(self.ResUpSignal)

        #RES_DOWN BUTTON
        self.button_res_down = QtWidgets.QPushButton(self)
        self.button_res_down.setIcon(QtGui.QIcon("down.png"))
        self.button_res_down.setIconSize(QtCore.QSize(20, 20))
        self.button_res_down.setToolTip("Click to decrease the number of characters")
        self.button_res_down.move(1370, 20)
        self.button_res_down.resize(QtCore.QSize(40, 40))
        self.button_res_down.clicked.connect(self.ResDownSignal)

        #ZOOM LABEL
        self.zoom_label = QtWidgets.QLabel(self)
        self.zoom_label.move(1570, 20)
        self.zoom_label.resize(QtCore.QSize(50, 40))
        self.zoom_label.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.zoom_label.setText("Zoom")

        #ZOOM_IN BUTTON
        self.button_zoom_in = QtWidgets.QPushButton(self)
        self.button_zoom_in.setIcon(QtGui.QIcon("up.png"))
        self.button_zoom_in.setIconSize(QtCore.QSize(20, 20))
        self.button_zoom_in.setToolTip("Click to zoom in")
        self.button_zoom_in.move(1690, 20)
        self.button_zoom_in.resize(QtCore.QSize(40, 40))
        self.button_zoom_in.clicked.connect(self.ZoomInSignal)

        #ZOOM_OUT BUTTON
        self.button_zoom_out = QtWidgets.QPushButton(self)
        self.button_zoom_out.setIcon(QtGui.QIcon("down.png"))
        self.button_zoom_out.setIconSize(QtCore.QSize(20, 20))
        self.button_zoom_out.setToolTip("Click to zoom out")
        self.button_zoom_out.move(1630, 20)
        self.button_zoom_out.resize(QtCore.QSize(40, 40))
        self.button_zoom_out.clicked.connect(self.ZoomOutSignal)
        
        #SAVE BUTTON
        self.button_save = QtWidgets.QPushButton("  Save", self)
        self.button_save.setIcon(QtGui.QIcon("save.png"))
        self.button_save.setIconSize(QtCore.QSize(20, 20))
        self.button_save.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.button_save.setToolTip("Click to save the ASCII art")
        self.button_save.move(1750, 20)
        self.button_save.setMinimumHeight(40)
        self.button_save.setMinimumWidth(150)
        self.button_save.clicked.connect(self.SaveSignal)
        #vbox.addWidget(artWindow.button_save)
        
        #CLOSE BUTTON
        self.button_close = QtWidgets.QPushButton("  Close", self)
        self.button_close.setIcon(QtGui.QIcon("exit.png"))
        self.button_close.setIconSize(QtCore.QSize(20, 20))
        self.button_close.setFont(QtGui.QFont("Sanserif", 11, 1.5))
        self.button_close.setToolTip("Click to close the application")
        self.button_close.move(20, 20)
        self.button_close.setMinimumHeight(40)
        self.button_close.setMinimumWidth(150)
        self.button_close.clicked.connect(self.CloseSignal)

        #ZOOM SLIDER
        #self.zoom_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        #self.zoom_slider.setFocusPolicy(QtCore.Qt.StrongFocus)
        #self.zoom_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        #self.zoom_slider.setTickInterval(10)
        #self.zoom_slider.setSingleStep(1)
        #self.zoom_slider.move(920, 20)
        #self.zoom_slider.setMinimumHeight(40)
        #self.zoom_slider.setMinimumWidth(150)

    def CloseSignal(self):
        print("Closed successfully")
        self.close()
    def SaveSignal(self):
        #saveFile = QtWidgets.QFileDialog.getExistingDirectory(self, 'Save', self.defaultSavePath)
        saveFile = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', self.defaultSavePath, 'Text file (*.txt)')
        self.savePath = saveFile[0]
        self.defaultSavePath = self.savePath

        fout = open(self.defaultSavePath, 'w')
        fout.write(self.art)
        fout.close()

        print("ASCII art saved at: %s" % self.defaultSavePath)
    def ZoomInSignal(self):
        self.defaultFontSize += 1
        fixed_font = QtGui.QFont("monospace", self.defaultFontSize)
        fixed_font.setStyleHint(QtGui.QFont.TypeWriter)
        self.art_label.setFont(fixed_font)
        print("zoom in")
    def ZoomOutSignal(self):
        self.defaultFontSize -= 1
        if self.defaultFontSize < 1:
            self.defaultFontSize += 1
        fixed_font = QtGui.QFont("monospace", self.defaultFontSize)
        fixed_font.setStyleHint(QtGui.QFont.TypeWriter)
        self.art_label.setFont(fixed_font)
        print("zoom out")
    def ResUpSignal(self):
        int(self.defaultRes)
        self.defaultRes += 100
        print(self.defaultRes)
        self.line_edit_res.setText(str(self.defaultRes))
        
        self.art = asc.main(self.defaultImgPath, int(self.defaultRes), self.mode, float(self.defaultScale))
        self.art_label.setPlainText(self.art)
    def ResDownSignal(self):
        int(self.defaultRes)
        self.defaultRes -= 100
        if self.defaultRes < 50:
            self.defaultRes += 100
        print(self.defaultRes)
        self.line_edit_res.setText(str(self.defaultRes))

        self.art = asc.main(self.defaultImgPath, int(self.defaultRes), self.mode, float(self.defaultScale))
        self.art_label.setPlainText(self.art)    
    def SetRes(self):
        self.defaultRes = int(self.line_edit_res.text())
        print(self.defaultRes)
        
        self.art = asc.main(self.defaultImgPath, int(self.defaultRes), self.mode, float(self.defaultScale))
        self.art_label.setPlainText(self.art)
    def ToggleMode(self):
        if self.mode:
            self.mode_button.setText("Low")
            self.mode = False
        else:
            self.mode_button.setText("High")
            self.mode = True

        self.art = asc.main(self.defaultImgPath, int(self.defaultRes), self.mode, float(self.defaultScale))
        self.art_label.setPlainText(self.art)
        print("toggle mode")
        print(self.defaultImgPath)
        print(self.defaultRes)
        print(self.mode)
    def ScaleUpSignal(self):
        int(self.defaultScale)
        self.defaultScale += 0.1
        print(self.defaultScale)
        self.line_edit_scale.setText(str(self.defaultScale))

        self.art = asc.main(self.defaultImgPath, int(self.defaultRes), self.mode, float(self.defaultScale))
        self.art_label.setPlainText(self.art)
    def ScaleDownSignal(self):
        int(self.defaultScale)
        self.defaultScale -= 0.1
        if self.defaultScale < 0.1:
            self.defaultScale += 0.1
        print(self.defaultScale)
        self.line_edit_scale.setText(str(self.defaultScale))

        self.art = asc.main(self.defaultImgPath, int(self.defaultRes), self.mode, float(self.defaultScale))
        self.art_label.setPlainText(self.art)
    def SetScale(self):
        self.defaultScale = float(self.line_edit_scale.text())
        print(self.defaultScale)
        self.art = asc.main(self.defaultImgPath, int(self.defaultRes), self.mode, float(self.defaultScale))
        self.art_label.setPlainText(self.art)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = SEC_WINDOW("hello", "C:/Users/Arif Ahmed/Pictures/Arts/7cxunfcbuzl11.jpg")
    mainWindow.show()
    sys.exit(app.exec())

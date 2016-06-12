import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.initUI()

    def initToolbar(self):
        self.toolbar  = self.addToolBar("options")
        #Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatBar(self):

        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

    def initUI(self):
        
        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)

        self.initToolbar()
        self.initFormatBar()
        self.initMenubar()

        #Initialize a stutus bar for the window
        self.statusbar = self.statusBar()
    
        #x an y coordinate on screen
        self.setGeometry(100,100,1030,800)

        self.setWindowTitle("Writer")

def main():

    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    main()

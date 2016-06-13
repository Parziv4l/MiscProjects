import sys
from PyQt5 import QtGui, QtCore, QtWidgets, QtPrintSupport
from PyQt5.QtCore import Qt

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.filename = ""
        self.initUI()

    def initToolbar(self):
        self.newAction = QtWidgets.QAction(QtGui.QIcon("Icons/new.png"), "New", self)
        self.newAction.setStatusTip("Create a new Document from scratch.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)
        
        self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.toolbar  = self.addToolBar("options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.saveAction)
        self.toolbar.addAction(self.openAction)


        #Makes the next toolbar appear underneath this 
        self.addToolBarBreak()

    def initFormatBar(self):

        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):
        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

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


    def new(self):
        spawn = Main(self)
        spawn.show()


    def open(self):
        #Get filename and show only .txt files
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.writer)")

        if self.filename:
            with open(self.filename, "rt") as file:
                self.text.setText(file.read())
                
    def save(self):
        #Only Open this dialog if there is no filename yet
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save File")
        #Add the appropriate extension if not currently in place
        if not self.filename.endswith(".writer"):
            self.filename += ".writer"

        #Store Contents and format in html format which QT does a nice job of implementing for us already
        with open(self.filename,"wt") as file:
            file.write(self.text.toHtml())


def main():

    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__=="__main__":
    main()

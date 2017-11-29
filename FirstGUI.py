import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Comparison')
        self.resize(600,400)
        self.statusBar().showMessage('Put into two files')

        menu = self.menuBar()
        file_menu = menu.addMenu('Files')
        exit_action = QAction('Close', self)
        exit_action.setStatusTip('Close it!')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # label1 = QLabel('First File',self)
        # label1.move(100,20)

        label2 = QLabel('Second File',self)
        label2.move(400,20)

        button1 = QPushButton('Compare!',self)
        button1.move(450,350)

        DropBox = DropLabel('First File', self)
        DropBox.move(100,20)






class DropLabel(QLabel):
    def __init__(self,title,parent):
        super().__init__(title,parent)
        self.setAcceptDrops(True)
    def dragEnterEvent(self,e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()
    def GetUrl(self,e):
        for url in e.mimeData().urls():
            path =  url.toLocalFile()
        return print(path)
    # def getURL(self,e):
    #     for url in e.mimeData().urls():
    #         self.path = url.toLocalFile()
    #     return print(url)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainGUI = GUI()
    mainGUI.show()

    sys.exit(app.exec_())

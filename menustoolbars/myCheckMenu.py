# myCheckMenu.py

#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This program creates a checkable menu.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QAction


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')
        exitMenu = menubar.addMenu('Exit')

        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
       
        exitStatAct = QAction('Exit Appplication', self, checkable=True)
        exitStatAct.setStatusTip('Exit Application')
        exitStatAct.setChecked(True)
        exitStatAct.triggered.connect(self.exitMenu)
        
        viewMenu.addAction(viewStatAct)
        viewMenu.addAction(exitStatAct)
    
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Check menu')
        self.show()


    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def exitMenu(self, state):

        if state:
            exit()
        
def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
